# THIS FUNCTION IS CREATED TO GET THE INDEX OF THE DATE IN A LIST G
def get_index_of_date(G, date):
    if type(G) == list and date in G:
        index = G.index(date)
        return index
    return f"{date}"
