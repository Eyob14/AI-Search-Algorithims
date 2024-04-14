from util import PriorityQueue
from graph import Graph
# this class contains the common implementation for weighted graphs


class weighted_graph(Graph):
    # implementation of uniform cost search
    def ucs(self, start_node, goal_node):
        queue = PriorityQueue()
        visited = set()
        path = {start_node: [None, 0]}
        queue.put(0, start_node)
        while not queue.empty():
            cumulativeCost, current = queue.get()
            visited.add(current)
            if current == goal_node:
                return [len(visited), self.construct_path(path, start_node, goal_node), cumulativeCost]
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    cost = min(self.graph[current][neighbour])
                    if neighbour not in path:
                        queue.put(cumulativeCost+cost, neighbour)
                        path[neighbour] = [current, cumulativeCost+cost]
                    else:
                        prevCost = path[neighbour][1]
                        if prevCost > cumulativeCost+cost:
                            queue.put(cumulativeCost+cost, neighbour)
                            path[neighbour] = [current, cumulativeCost+cost]
        return [len(visited)]

    # implementation for bidirectional search
    def bidirectional_search(self, start_node, goal_node):
        # queue for a forward search
        queueF = PriorityQueue()
        # queue for a backward search
        queueB = PriorityQueue()
        queueF.put(0, start_node)
        queueB.put(0, goal_node)
        # dictionary to hold path of a forward traversal
        pathF = {start_node: [None, 0]}
        # dictionary to hold path of a Backward traversal
        pathB = {goal_node: [None, 0]}
        # set to hold visited nodes by forward traversal
        visitedF = set()
        # set to hold visited nodes by backward traversal
        visitedB = set()
        while not queueF.empty() and not queueB.empty():
            cumulativeCost, current = queueF.get()
            visitedF.add(current)
            for neighbour in self.graph[current]:
                if neighbour not in visitedF:
                    cost = min(self.graph[current][neighbour])
                    if neighbour not in pathF:
                        totalCost = cumulativeCost+cost
                        pathF[neighbour] = [current, totalCost]
                        queueF.put(totalCost, neighbour)
                    else:
                        prevCost = pathF[neighbour][1]
                        totalCost = cumulativeCost+cost
                        if prevCost > totalCost:
                            pathF[neighbour] = [current, totalCost]
                            queueF.put(totalCost, neighbour)
                if neighbour in visitedB:
                    return [len(visitedF)+len(visitedB), self.construct_path(pathF, start_node, neighbour)+self.construct_path(pathB, goal_node, neighbour)[::- 1][1:], pathF[neighbour][-1]+pathB[neighbour][-1]]
            cumulativeCost, current = queueB.get()
            visitedB.add(current)
            for neighbour in self.graph[current]:
                if neighbour not in visitedB:
                    cost = min(self.graph[current][neighbour])
                    if neighbour not in pathB:
                        totalCost = cumulativeCost+cost
                        pathB[neighbour] = [current, totalCost]
                        queueB.put(totalCost, neighbour)
                    else:
                        prevCost = pathB[neighbour][1]
                        totalCost = cumulativeCost+cost
                        if prevCost > totalCost:
                            pathB[neighbour] = [current, totalCost]
                            queueB.put(totalCost, neighbour)
                if neighbour in visitedF:
                    return [len(visitedF)+len(visitedB), self.construct_path(pathF, start_node, neighbour)+self.construct_path(pathB, goal_node, neighbour)[::- 1][1:], pathF[neighbour][-1]+pathB[neighbour][-1]]
        return [len(visitedF)+len(visitedB)]
    # implementation for greedy search

    def greedy(self, start_node, goal_node):
        visited = set()
        path = {}
        cost = 0
        current = (start_node.heuristic(start_node, goal_node), start_node)
        while current:
            queue = PriorityQueue()
            visited.add(current[1])
            if current[1] == goal_node:
                return [len(visited), self.construct_path(path, start_node, goal_node), cost]
            for neighbour in self.graph[current[-1]]:
                if neighbour not in visited:
                    priority = neighbour.heuristic(neighbour, goal_node)
                    queue.put(priority, neighbour)
                    path[neighbour] = current[-1]
            if not queue.empty():
                best = queue.get()
            else:
                return [len(visited)]
            cost += min(self.graph[current[-1]][best[-1]])
            current = best
        return [len(visited)]
    # implementation for A* search

    def astar(self, start_node, goal_node):
        visited = set()
        path = {start_node: [None, 0]}
        queue = PriorityQueue()
        result = None
        queue.put(start_node.heuristic(start_node, goal_node), start_node)
        while not queue.empty():
            cost, currentNode = queue.get()
            visited.add(currentNode)
            if currentNode == goal_node:
                if result:
                    if result[-1] > path[currentNode][-1]:
                        result = [len(visited), self.construct_path(
                            path, start_node, currentNode), path[currentNode][-1]]
                        continue
                else:
                    result = [len(visited), self.construct_path(
                        path, start_node, currentNode), path[currentNode][-1]]
                    continue
            for neighbour in self.graph[currentNode]:
                if neighbour not in visited:
                    totalCost = min(
                        self.graph[currentNode][neighbour])+path[currentNode][-1]
                    if neighbour not in path:
                        path[neighbour] = [currentNode, totalCost]
                        queue.put(
                            totalCost+neighbour.heuristic(neighbour, goal_node), neighbour)
                    else:
                        prevCost = path[neighbour][-1]
                        if prevCost > totalCost:
                            path[neighbour] = [currentNode, totalCost]
                            queue.put(
                                totalCost+neighbour.heuristic(neighbour, goal_node), neighbour)
        return result if result else [len(visited)]
