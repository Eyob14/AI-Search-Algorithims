# initialize import

import math
import time as Time
import random
import csv
from data import graph, cities


def test(graph, cities, random_choice_num, repitition):
    #  Select random cities from the array to get started with
    randomCities = random.sample(cities, random_choice_num)
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
    for cityA in randomCities:
        for cityB in randomCities:
            if cityA == cityB or cityB in visited:
                continue
            for i in range(repitition):
                # array to hold time taken to find a path between 2
                # nodes for different search algorithms
                tempTime = [f'{cityA.value} to {cityB.value}']
                # array to hold path length of a path between 2
                # nodes for different search algorithms
                tempSolnSize = [f'{cityA.value} to {cityB.value}']
                for j in range(len(algorithms)):
                    start_time = Time.perf_counter()
                    # result is an array whose first value is number of nodes visited
                    # second value is the path between the nodes if there is a path
                    # or else result only contains one value the number of nodes visited
                    # the third value holds cost of the path for algorithms that consider
                    # cost of the path
                    # running all algo's sequentially
                    result = algorithms[j](cityA, cityB)
                    end_time = Time.perf_counter()
                    duration = (end_time-start_time)*1000
                    tempTime.append(duration)
                    # result[1] holds path between two nodes
                    # its length gives us path length
                    tempSolnSize.append(
                        len(result[1]) if len(result) > 1 else None)
                times.append(tempTime)
                Solns.append(tempSolnSize)
        visited.add(cityA)
    return [Solns, times]

# Solns,times=test(graph,cities,10,10);
# with open('city_time_test.csv', mode='a', newline='') as file:

#         # create a writer object
#         writer = csv.writer(file)

#         # write the data to the file
#         writer.writerow(['path','dfs','bfs','ucs','greedy','iterative deepening','bidirectional search','A* search'])
#         for row in times:
#             writer.writerow(row)
# with open('city_solnLength_test.csv', mode='a', newline='') as file:

#     # create a writer object
#     writer = csv.writer(file)

#     # write the data to the file
#     writer.writerow(['path','dfs','bfs','ucs','greedy','iterative deepening','bidirectional search','A* search'])
#     for row in Solns:
#         writer.writerow(row)
