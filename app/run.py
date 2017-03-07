from utils.load_data import load_flights_to_dict
from utils.networkx_graph import generate_graph

start_city, flights_dict, destinations = load_flights_to_dict()

# get_cheapest_path(start_city, flights_dict, destinations)

generate_graph(flights_dict, destinations)

print('Done!')
