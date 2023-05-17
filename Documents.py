import networkx as nx
from networkx import number_of_nodes, number_of_edges
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import collections


# THIS FUNCTION IS CREATED TO GET THE INDEX OF THE DATE IN A LIST G
def get_index_of_date(G, date):
    if type(G) == list and date in G:
        index = G.index(date)
        return index
    return f"{date}"


# COMMENT THE SCRIPT BELOW THIS LINE BEFORE RUNNING APPLICATION
# THIS SCRIPT CONTAINS THE CODE USED TO CREATE THE STATIC GRAPHS

G = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
     2017, 2018, 2019, 2020, 2021, 2022]

# THE DATA IS EXTRACTED FROM THE PANDAS DATAFRAME AND PASSED INTO THE UNDIRECTED GRAPH
# G[0] = nx.Graph()  # creates an undirected graph
# df = pd.read_excel(f"files/F1998.xlsx")  # pandas is used to extract the data from the file
# G[0] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# COMPUTES THE NETWORK SIZE, NUMBER OF LINKS, NUMBER OF PROVIDER AND PEER LINKS, AND THE LINK DENSITY PROPERTY OF THE GRAPH
# count_1998 = number_of_nodes(G[0])
# print(f"1998: {count_1998}")
# edges_1998 = number_of_edges(G[0])
# print(f"1998_edges: {edges_1998}")
# rel_count_1998 = nx.get_edge_attributes(G[0], "relationship")
# peer_1998 = 0
# provider_1998 = 0
# for key in rel_count_1998:
#     if rel_count_1998[key] == 0:
#         peer_1998 += 1
#     elif rel_count_1998[key] == -1:
#         provider_1998 += 1
#
# print(f"peer_1998: {peer_1998}")
# print(f"provider_1998: {provider_1998}")
#
# density_1998 = nx.density(G[0])
# print(f"density_1998: {density_1998}")
#
# EDGE COLORS ARE ASSIGNED DEPENDING ON THE RELATIONSHIP ATTRIBUTE VALUE
# color_map_1998 = nx.get_edge_attributes(G[0], "relationship")
#
# for key in color_map_1998:
#     if color_map_1998[key] == 0:
#         color_map_1998[key] = "blue"
#     elif color_map_1998[key] == -1:
#         color_map_1998[key] = "red"
# #
# rel_colors_1998 = [color_map_1998.get(edge) for edge in G[0].edges()]
#
# # create a second graph to append nodes meeting the degree requirement
# degree_1998 = dict(G[0].degree)
# nx.set_node_attributes(G[0], degree_1998, "Degree")
# value_1998 = nx.get_node_attributes(G[0], "Degree")
# H_1998 = nx.Graph()
# for node1, node2 in G[0].edges():
#     if value_1998[node2] > 130:
#         H_1998.add_edge(node1, node2)
#
# degree_sequence = sorted([d for n, d in G[0].degree()], reverse=True)
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
#
# fig, ax = plt.subplots()
# plt.plot(deg, cnt, color="r", marker="o")
# plt.title("Degree Distribution")
# plt.ylabel("Number of Nodes")
# plt.xlabel("Degree")
# plt.show()

# # construct and save graph
# pos_1998 = nx.spring_layout(H_1998)
# nx.draw(H_1998, pos_1998, with_labels=True, edge_color=rel_colors_1998)
# plt.plot(figsize=(20, 15))
# plt.savefig("static/graph/G1998.png")
# plt.close()


# G[1] = nx.Graph()
# df = pd.read_excel(f"files/F1999.xlsx")
# G[1] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_1999 = number_of_nodes(G[1])
# print(f"1999: {count_1999}")
# edges_1999 = number_of_edges(G[1])
# print(f"1999_edges: {edges_1999}")
# rel_count_1999 = nx.get_edge_attributes(G[1], "relationship")
# peer_1999 = 0
# provider_1999 = 0
# for key in rel_count_1999:
#     if rel_count_1999[key] == 0:
#         peer_1999 += 1
#     elif rel_count_1999[key] == -1:
#         provider_1999 += 1
#
# print(f"peer_1999: {peer_1999}")
# print(f"provider_1999: {provider_1999}")
#
# density_1999 = nx.density(G[1])
# print(f"density_1999: {density_1999}")


# G[2] = nx.Graph()
# df = pd.read_excel(f"files/F2000.xlsx")
# G[2] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2000 = number_of_nodes(G[2])
# print(f"2000: {count_2000}")
# edges_2000 = number_of_edges(G[2])
# print(f"2000_edges: {edges_2000}")
# rel_count_2000 = nx.get_edge_attributes(G[2], "relationship")
# peer_2000 = 0
# provider_2000 = 0
# for key in rel_count_2000:
#     if rel_count_2000[key] == 0:
#         peer_2000 += 1
#     elif rel_count_2000[key] == -1:
#         provider_2000 += 1
#
# print(f"peer_2000: {peer_2000}")
# print(f"provider_2000: {provider_2000}")
#
# density_2000 = nx.density(G[2])
# print(f"density_2000: {density_2000}")


# G[3] = nx.Graph()
# df = pd.read_excel(f"files/F2001.xlsx")
# G[3] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2001 = number_of_nodes(G[3])
# print(f"2001: {count_2001}")
# edges_2001 = number_of_edges(G[3])
# print(f"2001_edges: {edges_2001}")
# rel_count_2001 = nx.get_edge_attributes(G[3], "relationship")
# peer_2001 = 0
# provider_2001 = 0
# for key in rel_count_2001:
#     if rel_count_2001[key] == 0:
#         peer_2001 += 1
#     elif rel_count_2001[key] == -1:
#         provider_2001 += 1
#
# print(f"peer_2001: {peer_2001}")
# print(f"provider_2001: {provider_2001}")
#
# density_2001 = nx.density(G[3])
# print(f"density_2001: {density_2001}")


# G[4] = nx.Graph()
# df = pd.read_excel(f"files/F2002.xlsx")
# G[4] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2002 = number_of_nodes(G[4])
# print(f"2002: {count_2002}")
# edges_2002 = number_of_edges(G[4])
# print(f"2002_edges: {edges_2002}")
# rel_count_2002 = nx.get_edge_attributes(G[4], "relationship")
# peer_2002 = 0
# provider_2002 = 0
# for key in rel_count_2002:
#     if rel_count_2002[key] == 0:
#         peer_2002 += 1
#     elif rel_count_2002[key] == -1:
#         provider_2002 += 1
#
# print(f"peer_2002: {peer_2002}")
# print(f"provider_2002: {provider_2002}")
#
# density_2002 = nx.density(G[4])
# print(f"density_2002: {density_2002}")


# G[5] = nx.Graph()
# df = pd.read_excel(f"files/F2003.xlsx")
# G[5] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2003 = number_of_nodes(G[5])
# print(f"2003: {count_2003}")
# edges_2003 = number_of_edges(G[5])
# print(f"2003_edges: {edges_2003}")
# rel_count_2003 = nx.get_edge_attributes(G[5], "relationship")
# peer_2003 = 0
# provider_2003 = 0
# for key in rel_count_2003:
#     if rel_count_2003[key] == 0:
#         peer_2003 += 1
#     elif rel_count_2003[key] == -1:
#         provider_2003 += 1
#
# print(f"peer_2003: {peer_2003}")
# print(f"provider_2003: {provider_2003}")
#
# density_2003 = nx.density(G[5])
# print(f"density_2003: {density_2003}")


# G[6] = nx.Graph()
# df = pd.read_excel(f"files/F2004.xlsx")
# G[6] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2004 = number_of_nodes(G[6])
# print(f"2004: {count_2004}")
# edges_2004 = number_of_edges(G[6])
# print(f"2004_edges: {edges_2004}")
# rel_count_2004 = nx.get_edge_attributes(G[6], "relationship")
# peer_2004 = 0
# provider_2004 = 0
# for key in rel_count_2004:
#     if rel_count_2004[key] == 0:
#         peer_2004 += 1
#     elif rel_count_2004[key] == -1:
#         provider_2004 += 1
#
# print(f"peer_2004: {peer_2004}")
# print(f"provider_2004: {provider_2004}")
#
# density_2004 = nx.density(G[6])
# print(f"density_2004: {density_2004}")


# G[7] = nx.Graph()
# df = pd.read_excel(f"files/F2005.xlsx")
# G[7] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2005 = number_of_nodes(G[7])
# print(f"2005: {count_2005}")
# edges_2005 = number_of_edges(G[7])
# print(f"2005_edges: {edges_2005}")
# rel_count_2005 = nx.get_edge_attributes(G[7], "relationship")
# peer_2005 = 0
# provider_2005 = 0
# for key in rel_count_2005:
#     if rel_count_2005[key] == 0:
#         peer_2005 += 1
#     elif rel_count_2005[key] == -1:
#         provider_2005 += 1
#
# print(f"peer_2005: {peer_2005}")
# print(f"provider_2005: {provider_2005}")
#
# density_2005 = nx.density(G[7])
# print(f"density_2005: {density_2005}")


# G[8] = nx.Graph()
# df = pd.read_excel(f"files/F2006.xlsx")
# G[8] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2006 = number_of_nodes(G[8])
# print(f"2006: {count_2006}")
# edges_2006 = number_of_edges(G[8])
# print(f"2006_edges: {edges_2006}")
# rel_count_2006 = nx.get_edge_attributes(G[8], "relationship")
# peer_2006 = 0
# provider_2006 = 0
# for key in rel_count_2006:
#     if rel_count_2006[key] == 0:
#         peer_2006 += 1
#     elif rel_count_2006[key] == -1:
#         provider_2006 += 1
#
# print(f"peer_2006: {peer_2006}")
# print(f"provider_2006: {provider_2006}")
#
# density_2006 = nx.density(G[8])
# print(f"density_2006: {density_2006}")


# G[9] = nx.Graph()
# df = pd.read_excel(f"files/F2007.xlsx")
# G[9] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2007 = number_of_nodes(G[9])
# print(f"2007: {count_2007}")
# edges_2007 = number_of_edges(G[9])
# print(f"2007_edges: {edges_2007}")
# rel_count_2007 = nx.get_edge_attributes(G[9], "relationship")
# peer_2007 = 0
# provider_2007 = 0
# for key in rel_count_2007:
#     if rel_count_2007[key] == 0:
#         peer_2007 += 1
#     elif rel_count_2007[key] == -1:
#         provider_2007 += 1
#
# print(f"peer_2007: {peer_2007}")
# print(f"provider_2007: {provider_2007}")
#
# density_2007 = nx.density(G[9])
# print(f"density_2007: {density_2007}")


# G[10] = nx.Graph()
# df = pd.read_excel(f"files/F2008.xlsx")
# G[10] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2008 = number_of_nodes(G[10])
# print(f"2008: {count_2008}")
# edges_2008 = number_of_edges(G[10])
# print(f"2008_edges: {edges_2008}")
# rel_count_2008 = nx.get_edge_attributes(G[10], "relationship")
# peer_2008 = 0
# provider_2008 = 0
# for key in rel_count_2008:
#     if rel_count_2008[key] == 0:
#         peer_2008 += 1
#     elif rel_count_2008[key] == -1:
#         provider_2008 += 1
#
# print(f"peer_2008: {peer_2008}")
# print(f"provider_2008: {provider_2008}")
#
# density_2008 = nx.density(G[10])
# print(f"density_2008: {density_2008}")


# G[11] = nx.Graph()
# df = pd.read_excel(f"files/F2009.xlsx")
# G[11] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2009 = number_of_nodes(G[11])
# print(f"2009: {count_2009}")
# edges_2009 = number_of_edges(G[11])
# print(f"2009_edges: {edges_2009}")
# rel_count_2009 = nx.get_edge_attributes(G[11], "relationship")
# peer_2009 = 0
# provider_2009 = 0
# for key in rel_count_2009:
#     if rel_count_2009[key] == 0:
#         peer_2009 += 1
#     elif rel_count_2009[key] == -1:
#         provider_2009 += 1
#
# print(f"peer_2009: {peer_2009}")
# print(f"provider_2009: {provider_2009}")
#
# density_2009 = nx.density(G[11])
# print(f"density_2009: {density_2009}")


# G[12] = nx.Graph()
# df = pd.read_excel(f"files/F2010.xlsx")
# G[12] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2010 = number_of_nodes(G[12])
# print(f"2010: {count_2010}")
# edges_2010 = number_of_edges(G[12])
# print(f"2010_edges: {edges_2010}")
# rel_count_2010 = nx.get_edge_attributes(G[12], "relationship")
# peer_2010 = 0
# provider_2010 = 0
# for key in rel_count_2010:
#     if rel_count_2010[key] == 0:
#         peer_2010 += 1
#     elif rel_count_2010[key] == -1:
#         provider_2010 += 1
#
# print(f"peer_2010: {peer_2010}")
# print(f"provider_2010: {provider_2010}")
#
# density_2010 = nx.density(G[12])
# print(f"density_2010: {density_2010}")


# G[13] = nx.Graph()
# df = pd.read_excel(f"files/F2011.xlsx")
# G[13] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2011 = number_of_nodes(G[13])
# print(f"2011: {count_2011}")
# edges_2011 = number_of_edges(G[13])
# print(f"2011_edges: {edges_2011}")
# rel_count_2011 = nx.get_edge_attributes(G[13], "relationship")
# peer_2011 = 0
# provider_2011 = 0
# for key in rel_count_2011:
#     if rel_count_2011[key] == 0:
#         peer_2011 += 1
#     elif rel_count_2011[key] == -1:
#         provider_2011 += 1
#
# print(f"peer_2011: {peer_2011}")
# print(f"provider_2011: {provider_2011}")
#
# density_2011 = nx.density(G[13])
# print(f"density_2011: {density_2011}")


# G[14] = nx.Graph()
# df = pd.read_excel(f"files/F2012.xlsx")
# G[14] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2012 = number_of_nodes(G[14])
# print(f"2012: {count_2012}")
# edges_2012 = number_of_edges(G[14])
# print(f"2012_edges: {edges_2012}")
# rel_count_2012 = nx.get_edge_attributes(G[14], "relationship")
# peer_2012 = 0
# provider_2012 = 0
# for key in rel_count_2012:
#     if rel_count_2012[key] == 0:
#         peer_2012 += 1
#     elif rel_count_2012[key] == -1:
#         provider_2012 += 1
#
# print(f"peer_2012: {peer_2012}")
# print(f"provider_2012: {provider_2012}")
#
# density_2012 = nx.density(G[14])
# print(f"density_2012: {density_2012}")


# G[15] = nx.Graph()
# df = pd.read_excel(f"files/F2013.xlsx")
# G[15] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2013 = number_of_nodes(G[15])
# print(f"2013: {count_2013}")
# edges_2013 = number_of_edges(G[15])
# print(f"2013_edges: {edges_2013}")
# rel_count_2013 = nx.get_edge_attributes(G[15], "relationship")
# peer_2013 = 0
# provider_2013 = 0
# for key in rel_count_2013:
#     if rel_count_2013[key] == 0:
#         peer_2013 += 1
#     elif rel_count_2013[key] == -1:
#         provider_2013 += 1
#
# print(f"peer_2013: {peer_2013}")
# print(f"provider_2013: {provider_2013}")
#
# density_2013 = nx.density(G[15])
# print(f"density_2013: {density_2013}")


# G[16] = nx.Graph()
# df = pd.read_excel(f"files/F2014.xlsx")
# G[16] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2014 = number_of_nodes(G[16])
# print(f"2014: {count_2014}")
# edges_2014 = number_of_edges(G[16])
# print(f"2014_edges: {edges_2014}")
# rel_count_2014 = nx.get_edge_attributes(G[16], "relationship")
# peer_2014 = 0
# provider_2014 = 0
# for key in rel_count_2014:
#     if rel_count_2014[key] == 0:
#         peer_2014 += 1
#     elif rel_count_2014[key] == -1:
#         provider_2014 += 1
#
# print(f"peer_2014: {peer_2014}")
# print(f"provider_2014: {provider_2014}")
#
# density_2014 = nx.density(G[16])
# print(f"density_2014: {density_2014}")


# G[17] = nx.Graph()
# df = pd.read_excel(f"files/F2015.xlsx")
# G[17] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2015 = number_of_nodes(G[17])
# print(f"2015: {count_2015}")
# edges_2015 = number_of_edges(G[17])
# print(f"2015_edges: {edges_2015}")
# rel_count_2015 = nx.get_edge_attributes(G[17], "relationship")
# peer_2015 = 0
# provider_2015 = 0
# for key in rel_count_2015:
#     if rel_count_2015[key] == 0:
#         peer_2015 += 1
#     elif rel_count_2015[key] == -1:
#         provider_2015 += 1
#
# print(f"peer_2015: {peer_2015}")
# print(f"provider_2015: {provider_2015}")
#
# density_2015 = nx.density(G[17])
# print(f"density_2015: {density_2015}")


# G[18] = nx.Graph()
# df = pd.read_excel(f"files/F2016.xlsx")
# G[18] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2016 = number_of_nodes(G[18])
# print(f"2016: {count_2016}")
# edges_2016 = number_of_edges(G[18])
# print(f"2016_edges: {edges_2016}")
# rel_count_2016 = nx.get_edge_attributes(G[18], "relationship")
# peer_2016 = 0
# provider_2016 = 0
# for key in rel_count_2016:
#     if rel_count_2016[key] == 0:
#         peer_2016 += 1
#     elif rel_count_2016[key] == -1:
#         provider_2016 += 1
#
# print(f"peer_2016: {peer_2016}")
# print(f"provider_2016: {provider_2016}")
#
# density_2016 = nx.density(G[18])
# print(f"density_2016: {density_2016}")


# G[19] = nx.Graph()
# df = pd.read_excel(f"files/F2017.xlsx")
# G[19] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2017 = number_of_nodes(G[19])
# print(f"2017: {count_2017}")
# edges_2017 = number_of_edges(G[19])
# print(f"2017_edges: {edges_2017}")
# rel_count_2017 = nx.get_edge_attributes(G[19], "relationship")
# peer_2017 = 0
# provider_2017 = 0
# for key in rel_count_2017:
#     if rel_count_2017[key] == 0:
#         peer_2017 += 1
#     elif rel_count_2017[key] == -1:
#         provider_2017 += 1
#
# print(f"peer_2017: {peer_2017}")
# print(f"provider_2017: {provider_2017}")
#
# density_2017 = nx.density(G[19])
# print(f"density_2017: {density_2017}")


# G[20] = nx.Graph()
# df = pd.read_excel(f"files/F2018.xlsx")
# G[20] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2018 = number_of_nodes(G[20])
# print(f"2018: {count_2018}")
# edges_2018 = number_of_edges(G[20])
# print(f"2018_edges: {edges_2018}")
# rel_count_2018 = nx.get_edge_attributes(G[20], "relationship")
# peer_2018 = 0
# provider_2018 = 0
# for key in rel_count_2018:
#     if rel_count_2018[key] == 0:
#         peer_2018 += 1
#     elif rel_count_2018[key] == -1:
#         provider_2018 += 1
#
# print(f"peer_2018: {peer_2018}")
# print(f"provider_2018: {provider_2018}")
#
# density_2018 = nx.density(G[20])
# print(f"density_2018: {density_2018}")


# G[21] = nx.Graph()
# df = pd.read_excel(f"files/F2019.xlsx")
# G[21] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2019 = number_of_nodes(G[21])
# print(f"2019: {count_2019}")
# edges_2019 = number_of_edges(G[21])
# print(f"2019_edges: {edges_2019}")
# rel_count_2019 = nx.get_edge_attributes(G[21], "relationship")
# peer_2019 = 0
# provider_2019 = 0
# for key in rel_count_2019:
#     if rel_count_2019[key] == 0:
#         peer_2019 += 1
#     elif rel_count_2019[key] == -1:
#         provider_2019 += 1
#
# print(f"peer_2019: {peer_2019}")
# print(f"provider_2019: {provider_2019}")
#
# density_2019 = nx.density(G[21])
# print(f"density_2019: {density_2019}")


# G[22] = nx.Graph()
# df = pd.read_excel(f"files/F2020.xlsx")
# G[22] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2020 = number_of_nodes(G[22])
# print(f"2020: {count_2020}")
# edges_2020 = number_of_edges(G[22])
# print(f"2020_edges: {edges_2020}")
# rel_count_2020 = nx.get_edge_attributes(G[22], "relationship")
# peer_2020 = 0
# provider_2020 = 0
# for key in rel_count_2020:
#     if rel_count_2020[key] == 0:
#         peer_2020 += 1
#     elif rel_count_2020[key] == -1:
#         provider_2020 += 1
#
# print(f"peer_2020: {peer_2020}")
# print(f"provider_2020: {provider_2020}")
#
# density_2020 = nx.density(G[22])
# print(f"density_2020: {density_2020}")


# G[23] = nx.Graph()
# df = pd.read_excel(f"files/F2021.xlsx")
# G[23] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2021 = number_of_nodes(G[23])
# print(f"2021: {count_2021}")
# edges_2021 = number_of_edges(G[23])
# print(f"2021_edges: {edges_2021}")
# rel_count_2021 = nx.get_edge_attributes(G[23], "relationship")
# peer_2021 = 0
# provider_2021 = 0
# for key in rel_count_2021:
#     if rel_count_2021[key] == 0:
#         peer_2021 += 1
#     elif rel_count_2021[key] == -1:
#         provider_2021 += 1
#
# print(f"peer_2021: {peer_2021}")
# print(f"provider_2021: {provider_2021}")
#
# density_2021 = nx.density(G[23])
# print(f"density_2021: {density_2021}")


# G[24] = nx.Graph()
# df = pd.read_excel(f"files/F2022.xlsx")
# G[24] = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='relationship')
# count_2022 = number_of_nodes(G[24])
# print(f"2022: {count_2022}")
# edges_2022 = number_of_edges(G[24])
# print(f"2022_edges: {edges_2022}")
# rel_count_2022 = nx.get_edge_attributes(G[24], "relationship")
# peer_2022 = 0
# provider_2022 = 0
# for key in rel_count_2022:
#     if rel_count_2022[key] == 0:
#         peer_2022 += 1
#     elif rel_count_2022[key] == -1:
#         provider_2022 += 1
#
# print(f"peer_2022: {peer_2022}")
# print(f"provider_2022: {provider_2022}")
#
# density_2022 = nx.density(G[24])
# print(f"density_2022: {density_2022}")


## PLOTS THE AS COUNT GRPAH BY YEAR
# x = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
#      2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# y = [count_1998, count_1999, count_2000, count_2001, count_2002, count_2003, count_2004, count_2005, count_2006,
#      count_2007, count_2008, count_2009, count_2010, count_2011, count_2012, count_2013, count_2014, count_2015,
#      count_2016, count_2017, count_2018, count_2019, count_2020, count_2021, count_2022]
# plt.plot(x, y)
# plt.title("Autonomous System Count (1998-2022)")
# plt.xticks(x, rotation="vertical")
# plt.grid(True)
# plt.savefig("static/yearly_count.png")
# plt.close()
#
## PLOTS BOTH THE AS COUNT AND DENSITY PROPERTY OF THE GRAPH BY YEAR IN ONE CHART
# x4 = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
#       2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# y4 = [density_1998, density_1999, density_2000, density_2001, density_2002, density_2003, density_2004,
#       density_2005, density_2006, density_2007, density_2008, density_2009, density_2010, density_2011,
#       density_2012, density_2013, density_2014, density_2015, density_2016, density_2017, density_2018,
#       density_2019, density_2020, density_2021, density_2022]
# plt.plot(x4, y4)
# plt.title("Link Density (1998-2022)")
# plt.xticks(x4, rotation="vertical")
# plt.grid(True)
# plt.savefig("static/density.png")
# plt.close()

## PLOTS THE TOTAL NUMBER OF EDGES, THE COUNT OF EDGES TAGGED AS PROVIDER-CUSTOMER,
## AND THE COUNT OF EDGES TAGGED AS PEER-PEER BY YEAR ON ONE CHART
# x1 = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
#       2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# y1 = [edges_1998, edges_1999, edges_2000, edges_2001, edges_2002, edges_2003, edges_2004, edges_2005, edges_2006,
#       edges_2007, edges_2008, edges_2009, edges_2010, edges_2011, edges_2012, edges_2013, edges_2014, edges_2015,
#       edges_2016, edges_2017, edges_2018, edges_2019, edges_2020, edges_2021, edges_2022]
# y2 = [provider_1998, provider_1999, provider_2000, provider_2001, provider_2002, provider_2003, provider_2004,
#       provider_2005, provider_2006, provider_2007, provider_2008, provider_2009, provider_2010, provider_2011,
#       provider_2012, provider_2013, provider_2014, provider_2015, provider_2016, provider_2017, provider_2018,
#       provider_2019, provider_2020, provider_2021, provider_2022]
# y3 = [peer_1998, peer_1999, peer_2000, peer_2001, peer_2002, peer_2003, peer_2004, peer_2005, peer_2006,
#       peer_2007, peer_2008, peer_2009, peer_2010, peer_2011, peer_2012, peer_2013, peer_2014, peer_2015,
#       peer_2016, peer_2017, peer_2018, peer_2019, peer_2020, peer_2021, peer_2022]
# fig, ax = plt.subplots()
# ax.plot(x1, y1, color="green", label="All")
# ax.plot(x1, y2, color="red", label="Provider-Customer")
# ax.plot(x1, y3, color="blue", label="Peer-Peer")
# plt.title("Autonomous System Relationships (1998-2022)")
# plt.xticks(x1, rotation="vertical")
# plt.grid(True)
# ax.legend(loc="upper left")
# plt.savefig("static/relationship.png")
# plt.close()


## PLOTS THE COUNT OF NODES WHICH WERE ADDED AND REMOVED BETWEEN 2 CONSECUTIVE YEARS
# COMPUTES THE ADDED NODES BYEACH PERIOD
# new1 = []
# node0 = G[0].nodes()
# node1 = G[1].nodes()
# for n in node1:
#     if n not in node0:
#         new1.append(n)
# output1 = len(new1)
#
# new2 = []
# node2 = G[2].nodes()
# for n in node2:
#     if n not in node1:
#         new2.append(n)
# output2 = len(new2)
#
# new3 = []
# node3 = G[3].nodes()
# for n in node3:
#     if n not in node2:
#         new3.append(n)
# output3 = len(new3)
#
# new4 = []
# node4 = G[4].nodes()
# for n in node4:
#     if n not in node3:
#         new4.append(n)
# output4 = len(new4)
#
# new5 = []
# node5 = G[5].nodes()
# for n in node5:
#     if n not in node4:
#         new5.append(n)
# output5 = len(new5)
#
# new6 = []
# node6 = G[6].nodes()
# for n in node6:
#     if n not in node5:
#         new6.append(n)
# output6 = len(new6)
#
# new7 = []
# node7 = G[7].nodes()
# for n in node7:
#     if n not in node6:
#         new7.append(n)
# output7 = len(new7)
#
# new8 = []
# node8 = G[8].nodes()
# for n in node8:
#     if n not in node7:
#         new8.append(n)
# output8 = len(new8)
#
# new9 = []
# node9 = G[9].nodes()
# for n in node9:
#     if n not in node8:
#         new9.append(n)
# output9 = len(new9)
#
# new10 = []
# node10 = G[10].nodes()
# for n in node10:
#     if n not in node9:
#         new10.append(n)
# output10 = len(new10)
#
# new11 = []
# node11 = G[11].nodes()
# for n in node11:
#     if n not in node10:
#         new11.append(n)
# output11 = len(new11)
#
# new12 = []
# node12 = G[12].nodes()
# for n in node12:
#     if n not in node11:
#         new12.append(n)
# output12 = len(new12)
#
# new13 = []
# node13 = G[13].nodes()
# for n in node13:
#     if n not in node12:
#         new13.append(n)
# output13 = len(new13)
#
# new14 = []
# node14 = G[14].nodes()
# for n in node14:
#     if n not in node13:
#         new14.append(n)
# output14 = len(new14)
#
# new15 = []
# node15 = G[15].nodes()
# for n in node15:
#     if n not in node14:
#         new15.append(n)
# output15 = len(new15)
#
# new16 = []
# node16 = G[16].nodes()
# for n in node16:
#     if n not in node15:
#         new16.append(n)
# output16 = len(new16)
#
# new17 = []
# node17 = G[17].nodes()
# for n in node17:
#     if n not in node16:
#         new17.append(n)
# output17 = len(new17)
#
# new18 = []
# node18 = G[18].nodes()
# for n in node18:
#     if n not in node17:
#         new18.append(n)
# output18 = len(new18)
#
# new19 = []
# node19 = G[19].nodes()
# for n in node19:
#     if n not in node18:
#         new19.append(n)
# output19 = len(new19)
#
# new20 = []
# node20 = G[20].nodes()
# for n in node20:
#     if n not in node19:
#         new20.append(n)
# output20 = len(new20)
#
# new21 = []
# node21 = G[21].nodes()
# for n in node21:
#     if n not in node20:
#         new21.append(n)
# output21 = len(new21)
#
# new22 = []
# node22 = G[22].nodes()
# for n in node22:
#     if n not in node21:
#         new22.append(n)
# output22 = len(new22)
#
# new23 = []
# node23 = G[23].nodes()
# for n in node23:
#     if n not in node22:
#         new23.append(n)
# output23 = len(new23)
#
# new24 = []
# node24 = G[24].nodes()
# for n in node24:
#     if n not in node23:
#         new24.append(n)
# output24 = len(new24)
#
# # COMPUTES THE REMOVED NODES FOR EACH PERIOD
# removed0 = []
# for n in node0:
#     if n not in node1:
#         removed0.append(n)
#
# result0 = len(removed0)
#
# removed1 = []
# for n in node1:
#     if n not in node2:
#         removed1.append(n)
#
# result1 = len(removed1)
#
# removed2 = []
# for n in node2:
#     if n not in node3:
#         removed2.append(n)
#
# result2 = len(removed2)
#
# removed3 = []
# for n in node3:
#     if n not in node4:
#         removed3.append(n)
#
# result3 = len(removed3)
#
# removed4 = []
# for n in node4:
#     if n not in node5:
#         removed4.append(n)
#
# result4 = len(removed4)
#
# removed5 = []
# for n in node5:
#     if n not in node6:
#         removed5.append(n)
#
# result5 = len(removed5)
#
# removed6 = []
# for n in node6:
#     if n not in node7:
#         removed6.append(n)
#
# result6 = len(removed6)
#
# removed7 = []
# for n in node7:
#     if n not in node8:
#         removed7.append(n)
#
# result7 = len(removed7)
#
# removed8 = []
# for n in node8:
#     if n not in node9:
#         removed8.append(n)
#
# result8 = len(removed8)
#
# removed9 = []
# for n in node9:
#     if n not in node10:
#         removed9.append(n)
#
# result9 = len(removed9)
#
# removed10 = []
# for n in node10:
#     if n not in node11:
#         removed10.append(n)
#
# result10 = len(removed10)
#
# removed11 = []
# for n in node11:
#     if n not in node12:
#         removed11.append(n)
#
# result11 = len(removed11)
#
# removed12 = []
# for n in node12:
#     if n not in node13:
#         removed12.append(n)
#
# result12 = len(removed12)
#
# removed13 = []
# for n in node13:
#     if n not in node14:
#         removed13.append(n)
#
# result13 = len(removed13)
#
# removed14 = []
# for n in node14:
#     if n not in node15:
#         removed14.append(n)
#
# result14 = len(removed14)
#
# removed15 = []
# for n in node15:
#     if n not in node16:
#         removed15.append(n)
#
# result15 = len(removed15)
#
# removed16 = []
# for n in node16:
#     if n not in node17:
#         removed16.append(n)
#
# result16 = len(removed16)
#
# removed17 = []
# for n in node17:
#     if n not in node18:
#         removed17.append(n)
#
# result17 = len(removed17)
#
# removed18 = []
# for n in node18:
#     if n not in node19:
#         removed18.append(n)
#
# result18 = len(removed18)
#
# removed19 = []
# for n in node19:
#     if n not in node20:
#         removed19.append(n)
#
# result19 = len(removed19)
#
# removed20 = []
# for n in node20:
#     if n not in node21:
#         removed20.append(n)
#
# result20 = len(removed20)
#
# removed21 = []
# for n in node21:
#     if n not in node22:
#         removed21.append(n)
#
# result21 = len(removed21)
#
# removed22 = []
# for n in node22:
#     if n not in node23:
#         removed22.append(n)
#
# result22 = len(removed22)
#
# removed23 = []
# for n in node23:
#     if n not in node24:
#         removed23.append(n)
#
# result23 = len(removed23)
#
# # PLOTS THE ADDED AND REMOVED NODE COUNT BY EACH PERIOD
# x5 = ["'98-'99", "'99-'00", "'00-'01", "'01-'02", "'02-'03", "'03-'04", "'04-'05", "'05-'06", "'06-'07", "'07-'08",
#       "'08-'09", "'09-'10", "'10-'11", "'11-'12", "'12-'13", "'13-'14", "'14-'15", "'15-'16", "'16-'17", "'17-'18",
#       "'18-'19", "'19-'20", "'20-'21", "'21-'22"]
# y5 = [output1, output2, output3, output4, output5, output6, output7, output8, output9, output10, output11, output12,
#       output13, output14, output15, output16, output17, output18, output19, output20, output21, output22, output23, output24]
# y6 = [result0, result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11,
#       result12, result13, result14, result15, result16, result17, result18, result19, result20, result21, result22, result23]
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.plot(x5, y5, color="blue", label="Added ASs")
# ax.plot(x5, y6, color="red", label="Removed ASs")
# plt.title("Added/Removed Autonomous Systems (1998-2022)")
# plt.xticks(x5, rotation="vertical")
# plt.grid(True)
# ax.legend(loc="upper left")
# plt.savefig("static/add_remove.png")
# plt.close()

