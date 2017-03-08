import networkx as nx


def generate_graph(flights_dict, cities):
    graph = nx.DiGraph()

    for i in range(0, len(flights_dict)):
        for d in cities:
            graph.add_node(d + str(i))

        for day, departures in flights_dict.items():
            for dep_airport, destinations in departures.items():
                for t in destinations:
                    graph.add_edge(dep_airport + str(day), t[0] + str(day), weight=t[1])

    nx.write_gexf(graph, "network.gexf")
