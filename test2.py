import math
import time as Time
import random
import csv
from Graph.weigthed_undirected_graph import weighted_undirected_graph


class Node:
    def __init__(self, value=None, position=None):
        self.value = value
        self.position = position

    @staticmethod
    def heuristic():
        pass


class randomNodes(Node):
    @staticmethod
    def heuristic(randomNode1, randomNode2):
        return math.sqrt((abs(randomNode1.position[0]-randomNode2.position[0])**2)+(abs(randomNode1.position[1]-randomNode2.position[1])**2))

    def manhattanCost(randomNode1, randomNode2):
        return abs(randomNode1.position[0]-randomNode2.position[0])+abs(randomNode1.position[1]-randomNode2.position[1])


def test(nodes_to_create, prob_of_edges, random_choice_num, repitition):
    # an array to  hold all the new random nodes to be created
    node_array = []
    for i in range(nodes_to_create):
        # creating random with values as integers and position as a random number for both
        # x and y
        node_array.append(randomNodes(
            i, [random.uniform(0, 10), random.uniform(0, 10)]))

    graph = weighted_undirected_graph()
    for node in node_array:
        graph.add_node(node)
    # a set to check that we dont run over the same edge twice
    # when creating random edges with different probabilities
    visited = set()
    for node_from in node_array:
        for node_to in node_array:
            if node_from == node_to or node_to in visited:
                continue
            if (random.uniform(0, 1) < prob_of_edges):
                # cost between nodes is taken as the manhattan distance between them
                graph.add_edge(node_from, node_to,
                               randomNodes.manhattanCost(node_from, node_to))
        visited.add(node_from)
    # from all the nodes generated choose certain amount randomly
    random_Nodes = random.sample(node_array, random_choice_num)
    # a set to check we run the tests for each node only once with every
    # other node
    visited = set()
    # array to hold time it takes to find solution by d/t search algorithms
    times = []
    # array to hold path length obtained by d/t search algorithm
    Solns = []
    # dictionary to reference the search algorithms
    algorithms = {
        0: graph.dfs,
        1: graph.bfs,
        2: graph.ucs,
        3: graph.greedy,
        4: graph.iterative_deepening,
        5: graph.bidirectional_search,
        6: graph.astar
    }
    for nodeA in random_Nodes:
        for nodeB in random_Nodes:
            if nodeA == nodeB or nodeB in visited:
                continue
            for i in range(repitition):
                # array to hold time taken to find a path between 2
                # nodes for different search algorithms
                tempTime = [f'{nodeA.value} to {nodeB.value}']
                # array to hold path length of a path between 2
                # nodes for different search algorithms
                tempSolnSize = [f'{nodeA.value} to {nodeB.value}']
                for j in range(len(algorithms)):
                    start_time = Time.perf_counter()
                    # result is an array whose first value is number of nodes visited
                    # second value is the path between the nodes if there is a path
                    # or else result only contains one value the number of nodes visited
                    # the third value holds cost of the path for algorithms that consider
                    # cost of the path
                    result = algorithms[j](nodeA, nodeB)  # running dfs algo
                    end_time = Time.perf_counter()
                    duration = (end_time-start_time)*1000
                    tempTime.append(duration)
                    # result[1] holds path between two nodes
                    # its length gives us path length
                    tempSolnSize.append(
                        len(result[1]) if len(result) > 1 else None)
                times.append(tempTime)
                Solns.append(tempSolnSize)
        visited.add(nodeA)
    return [Solns, times]
# num_of_nodes=[10,20,30,40];
# prob_of_edges=[0.2,0.4,0.6,0.8]
# for num in num_of_nodes:
#     for prob in prob_of_edges:
#         Solns,times=test(num,prob,10,5);
#         with open(f'{num} nodes {prob}_randomNode_time_test.csv', mode='a', newline='') as file:

#             # create a writer object
#             writer = csv.writer(file)

#             # write the data to the file
#             writer.writerow(['path','dfs','bfs','ucs','greedy','iterative deepening','bidirectional search','A* search'])
#             for row in times:
#                 writer.writerow(row)
#         with open(f'{num} nodes {prob}_randomNode_solnLength_test.csv', mode='a', newline='') as file:

#             # create a writer object
#             writer = csv.writer(file)

#             # write the data to the file
#             writer.writerow(['path','dfs','bfs','ucs','greedy','iterative deepening','bidirectional search','A* search'])
#             for row in Solns:
#                 writer.writerow(row)
