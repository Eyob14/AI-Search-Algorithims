import math

from Graph.node import Node
from Graph.weigthed_undirected_graph import weighted_undirected_graph


class City(Node):
    def __init__(self, value=None, position=None):
        super().__init__(value)
        self.position = position

    @staticmethod
    def heuristic(city1, city2):
        earth_radius = 6371
        lat1, lon1, lat2, lon2 = map(math.radians, [
                                     city1.position[0], city1.position[1], city2.position[0], city2.position[1]])
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        # apply the Haversine formula
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * \
            math.cos(lat2) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance_km = earth_radius * c
        return distance_km


# Data for the romanian cities
# dictionary of latitude and longitude of the cites
position_dict = {}
with open('city.txt', 'r') as file:
    for line in file:
        position = line.split(',')
        city, lat, lon = position
        position_dict[city] = [float(lat), float(lon)]
# array containing a city node with their name and position
cities = [City("Arad", position_dict["Arad"]), City("Zerind", position_dict["Zerind"]),
          City("Oradea", position_dict["Oradea"]), City(
              "Sibiu", position_dict["Sibiu"]),
          City("Timisoara", position_dict["Timisoara"]), City(
              "Lugoj", position_dict["Lugoj"]),
          City("Mehadia", position_dict["Mehadia"]), City(
              "Drobeta", position_dict["Drobeta"]),
          City("Craiova", position_dict["Craiova"]), City(
              "Rimnicu Vilcea", position_dict["Rimnicu Vilcea"]),
          City("Pitesti", position_dict["Pitesti"]), City(
              "Fagaras", position_dict["Fagaras"]),
          City("Bucharest", position_dict["Bucharest"]), City(
              "Giurgiu", position_dict["Giurgiu"]),
          City("Urziceni", position_dict["Urziceni"]), City(
              "Neamt", position_dict["Neamt"]),
          City("Iasi", position_dict["Iasi"]), City(
              "Vaslui", position_dict["Vaslui"]),
          City("Hirsova", position_dict["Hirsova"]), City("Eforie", position_dict["Eforie"])]

# Initializing Graph with the edges and costs
edges = [
    (cities[0], cities[1], 75), (cities[0],
                                 cities[4], 118), (cities[0], cities[3], 140),
    (cities[1], cities[2], 71), (cities[2],
                                 cities[3], 151), (cities[3], cities[11], 99),
    (cities[3], cities[9], 80), (cities[4],
                                 cities[5], 111), (cities[5], cities[6], 70),
    (cities[6], cities[7], 75), (cities[7],
                                 cities[8], 120), (cities[8], cities[9], 146),
    (cities[8], cities[10], 138), (cities[9],
                                   cities[10], 97), (cities[10], cities[12], 101),
    (cities[11], cities[12], 211), (cities[12],
                                    cities[13], 90), (cities[12], cities[14], 85),
    (cities[14], cities[17], 142), (cities[14],
                                    cities[18], 98), (cities[15], cities[16], 87),
    (cities[16], cities[17], 92), (cities[18], cities[19], 86)
]

graph = weighted_undirected_graph()

for edge in edges:
    from_node, to_node, cost = edge
    graph.add_edge(from_node, to_node, cost)
    
def view_graph(graph):
    for node in graph.graph:
        neighbors=[];
        for neighbor in graph.graph[node]:
            neighbors.append([neighbor.value,*graph.graph[node][neighbor]])
        print(node.value," : ",neighbors)
        
view_graph(graph)
