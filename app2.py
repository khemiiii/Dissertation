# import the packages required
from flask import Flask, render_template, request
import networkx as nx
from operator import itemgetter
from networkx import number_of_nodes
from Documents import get_index_of_date
import pandas as pd
import itertools
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')


app = Flask(__name__)  # initialise the app from the flask class


@app.route("/")
def home():
    return render_template("index.html")  # returns the template stored in the parenthesis


@app.route("/TopologyProperties")
def topologyproperties():
    return render_template("TopologyProperties.html")


@app.route("/CentralNodes")
def centralnodes():
    return render_template("CentralNodes.html")


@app.route("/DomainHierarchy")
def domainhierarchy():
    return render_template("DomainHierarchy.html")


@app.route("/DomainCount")
def domaincount():
    return render_template("DomainCountPerPeriod.html")


@app.route("/NewDomains")
def newdomains():
    return render_template("NewDomainPerPeriod.html")


@app.route("/RemovedDomains")
def olddomains():
    return render_template("RemovedDomainPerPeriod.html")


# the methods POST and GET are required to get the outputs of the form and to also post results to the html script
@app.route("/CNresult", methods=["POST", "GET"])
def centralnodesresult():
    form_output = request.form.to_dict()  # extracts the data from the forms on the webpage
    date = int(form_output["Period"])  # passes the input named "Period" into a variable "date"

    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]  # list of all the years available on the form
    index = int(get_index_of_date(G, date))  # gets the index of the year in the date variable from the list g

    G[index] = nx.Graph()  # NETWORKX IS USED TO CREATE AN UNDIRECTED GRAPH FOR THAT YEAR

    # PANDAS IS USED TO EXTRACT THE DATA FROM THE FILE
    # THE DATA IS EXTRACTED FROM THE PANDAS DATAFRAME AND PASSED INTO THE UNDIRECTED GRAPH
    # NODE1 IN THE FILE IS STORED IN THE COLUMN TITLED "SOURCE"
    # NODE2 IN THE FILE IS STORED IN THE COLUMN TITLED "TARGET"
    # THE RELATIONSHIP TYPES ARE STORED IN THE COLUMN TITLED "RELATIONSHIP"
    df = pd.read_excel(f"Files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # COMPUTES THE CENTRALITY MEASURES OF THE NODES AND SAVES THEM AS ATTRIBUTES OF THE NODES
    deg_c = dict(G[index].degree)
    btw_c = nx.betweenness_centrality(G[index])
    eigen_c = nx.eigenvector_centrality(G[index])
    nx.set_node_attributes(G[index], deg_c, 'Degree')
    nx.set_node_attributes(G[index], btw_c, 'Betweenness')
    nx.set_node_attributes(G[index], eigen_c, 'Eigenvector')

    # SORTS THE NODES BY THEIR CENTRALITY MEASURES IN AN ASCENDING MANNER
    degree = sorted(deg_c.items(), key=itemgetter(1), reverse=True)
    eigen = sorted(eigen_c.items(), key=itemgetter(1), reverse=True)
    btw = sorted(btw_c.items(), key=itemgetter(1), reverse=True)

    # THE DATE, CENTRALITY MEASURES VARIABLES WITH A LIMIT OF 10 ARE PASSED
    # INTO PLACEHOLDERS ON THE WEBPAGE AS THE OUTPUT
    return render_template("CNresult.html", date=date, degree=degree[:10], eigen=eigen[:10], btw=btw[:10])


# COMPUTES THE TIER AND TOPOLOGY PROPERTIES OF THE AS
@app.route("/TPresult", methods=["POST", "GET"])
def tpresult():
    form_output = request.form.to_dict()
    domain = int(form_output["domainID"])
    date = int(form_output["Period"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index = int(get_index_of_date(G, date))
    G[index] = nx.DiGraph()
    date = int(form_output["Period"])
    df = pd.read_excel(f"Files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship',
                                       create_using=nx.DiGraph())

    degree = dict(G[index].degree)
    btw_c = nx.betweenness_centrality(G[index])
    eigen_c = nx.eigenvector_centrality(G[index])
    nx.set_node_attributes(G[index], degree, 'Degree')
    nx.set_node_attributes(G[index], btw_c, 'Betweenness')
    nx.set_node_attributes(G[index], eigen_c, 'Eigenvector')
    attributes = dict(G[index].nodes[domain])

    H = nx.DiGraph()  # networkx is used to create a directed graph, H

    # edges with relationship attributes of "-1" are passed into the H graph
    for node1, node2, edge in G[index].edges(data=True):
        if edge['relationship'] == -1:
            H.add_edge(node1, node2, relationship=edge)

    in_degree = dict(H.in_degree)
    out_degree = dict(H.out_degree)
    nx.set_node_attributes(H, in_degree, 'In-degree')
    nx.set_node_attributes(H, out_degree, 'Out-degree')

    # for nodes in H, the tier attributes for each are assigned depending on their in-degree or out-degree
    for n, d in H.nodes(data=True):
        if d['In-degree'] < 1:
            tier = "Tier_1"
            H.nodes[n]['Tier'] = tier
        elif d['Out-degree'] < 1:
            tier = "Tier_3"
            H.nodes[n]['Tier'] = tier
        elif d['In-degree'] >= 1 and d['Out-degree'] >= 1:
            tier = "Tier_2"
            H.nodes[n]['Tier'] = tier

    attributes_h = H.nodes[domain]["Tier"]

    # the variables are passed into their placeholders on the webpage as the computed result
    return render_template("TPresult.html", domain=domain, date=date, attributes=attributes, attributes_h=attributes_h)


@app.route("/DHresult", methods=["POST", "GET"])
def dhresult():
    # checks if the filename exists, if yes, the file is deleted
    file_name = "static/images/graph.png"
    if os.path.isfile(file_name):
        os.remove(file_name)

    form_output = request.form.to_dict()
    domain = int(form_output["domainID"])
    date = int(form_output["Period"])
    c_degree = int(form_output["cutoff"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index = int(get_index_of_date(G, date))
    G[index] = nx.Graph()
    date = int(form_output["Period"])
    df = pd.read_excel(f"Files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship',
                                       create_using=nx.Graph())

    # a path list is created to store the nodes, path[1:] keeps all nodes except the first one which creates a self-loop
    path = []
    path.append(nx.single_target_shortest_path(G[index], domain, c_degree))  # c_degree stores the hop cut-off for links
    path = [tuple(val) for dic in path for key, val in dic.items()]
    path = path[1:]

    # an undirected graph P is created to plot the links and nodes in the path list
    P = nx.Graph()
    for node_tuple in path:
        P.add_edges_from(itertools.combinations(node_tuple, 2))

    # edge colors are assigned depending on the relationship attribute value
    color_map = nx.get_edge_attributes(G[index], "relationship")

    for key in color_map:
        if color_map[key] == 0:
            color_map[key] = "blue"
        elif color_map[key] == -1:
            color_map[key] = "red"

    rel_colors = [color_map.get(edge) for edge in G[index].edges()]

    # the graph P is generated with a spring layout and stored in the variable file_name
    # plt.close() prevents the graphs from generating a leyered plot on the previously generated plot
    pos = nx.spring_layout(P)
    nx.draw(P, pos, with_labels=True, edge_color=rel_colors)
    plt.savefig(file_name)
    plt.close()

    return render_template("DHresult.html", domain=domain, date=date, path=path)


@app.route("/Image")
def image():
    return render_template("Image.html")


@app.route("/DCresult", methods=["POST", "GET"])
def dcresult():
    form_output = request.form.to_dict()
    date = int(form_output["Period"])
    file = f"static/graph/G{date}.png"
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index = int(get_index_of_date(G, date))
    G[index] = nx.Graph()
    df = pd.read_excel(f"Files/F{date}.xlsx")
    G[index] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # computes the network size and density property of the graph
    count = number_of_nodes(G[index])
    density = nx.density(G[index])

    return render_template("DCresult.html", date=date, count=count, density=density, image=file)


@app.route("/NDresult", methods=["POST", "GET"])
def ndresult():
    form_output = request.form.to_dict()
    date1 = int(form_output["PeriodFrom"])
    date2 = int(form_output["PeriodTo"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index1 = int(get_index_of_date(G, date1))
    G[index1] = nx.Graph()
    df = pd.read_excel(f"Files/F{date1}.xlsx")
    G[index1] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    index2 = int(get_index_of_date(G, date2))
    G[index2] = nx.Graph()
    df = pd.read_excel(f"Files/F{date2}.xlsx")
    G[index2] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # creates a new list to store the nodes which exists in node2 but not node1
    new = []
    node1 = G[index1].nodes()
    node2 = G[index2].nodes()
    for n in node2:
        if n not in node1:
            new.append(n)

    result = len(new)  # counts the values in the "new" list
    count1 = number_of_nodes(G[index1])
    count2 = number_of_nodes(G[index2])
    return render_template("NDresult.html", result=result, date1=date1, date2=date2, count1=count1, count2=count2)


@app.route("/RDresult", methods=["POST", "GET"])
def rdresult():
    form_output = request.form.to_dict()
    date1 = int(form_output["PeriodFrom"])
    date2 = int(form_output["PeriodTo"])
    G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019, 2020, 2021, 2022]
    index1 = int(get_index_of_date(G, date1))
    G[index1] = nx.Graph()
    df = pd.read_excel(f"Files/F{date1}.xlsx")
    G[index1] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    index2 = int(get_index_of_date(G, date2))
    df = pd.read_excel(f"Files/F{date2}.xlsx")
    G[index2] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')

    # creates a removed list to store the nodes which exists in node1 but not node2
    removed = []
    node1 = G[index1].nodes()
    node2 = G[index2].nodes()
    for n in node1:
        if n not in node2:
            removed.append(n)

    result = len(removed)  # counts the values in the "removed" list
    count1 = number_of_nodes(G[index1])
    count2 = number_of_nodes(G[index2])
    return render_template("RDresult.html", result=result, date1=date1, date2=date2, count1=count1, count2=count2)


if __name__ == '__main__':
    app.run(debug=True, port=5005)  # the specific port is stated
