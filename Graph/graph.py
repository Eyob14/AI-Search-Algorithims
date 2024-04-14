from collections import deque
# This Graph class acts as an interface from which other graphs types could
# be extended


class Graph:
    def __init__(self):
        # The graph is represented inside a dictionary
        self.graph = {}
    # adding a node creates a new key with node given and
    # the value is initialized by an empty dictionary
    # which will hold the neighbours (and their action
    # costs in the case of a weighted graph).
    def add_node(self, node): self.graph[node] = {}
    # delete node not only deletes the node from the dictionary
    # keys but also removes it from others nodes where it is registered
    # as a neighbour

    def delete_node(self, node):
        if node in self.graph.keys():
            del self.graph[node]
            for nodes in self.graph.keys():
                if node in self.graph[nodes].keys():
                    del self.graph[nodes][node]
    # This search method returns true if node being searched is in the
    # graph and false if otherwise

    def search_node(self, node):
        if node in self.graph.keys():
            return True
        return False
    # This add edge method isnot the actual implementation to add edges
    # it only contains a code that is shared by all the other graph class
    # that extend this graph class

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph.keys():
            self.add_node(from_node)
        if to_node not in self.graph.keys():
            self.add_node(to_node)

    # delete edge method to be implemented by the extending classes
    def delete_edge(self, from_node, to_node):
        pass

    # this construct_path method constructs path for the different search algorithms using
    # backtracking
    def construct_path(self, path, start_node, goal_node):
        node = goal_node
        result = [node.value]
        while node != start_node:
            if (not isinstance(path[node], list)):
                node = path[node]
            else:
                node, cost = path[node]
            result.append(node.value)
        result.reverse()
        return result

    # implementation for depth first Search
    def dfs(self, start_node, goal_node):
        stack = [start_node]
        visited = set()
        path = {}
        while stack:
            current = stack.pop()
            visited.add(current)
            if current == goal_node:
                return [len(visited), self.construct_path(path, start_node, goal_node)]
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    path[neighbour] = current
        return [len(visited)]

    # implementation for breadth first search
    def bfs(self, start_node, goal_node):
        queue = deque([start_node])
        visited = set()
        visited.add(start_node)
        path = {}

        while queue:
            current = queue.popleft()
            if current == goal_node:
                return [len(visited), self.construct_path(path, start_node, goal_node)]
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    path[neighbour] = current
        return [len(visited)]

    # implementation for iterative deepening
    def iterative_deepening(self, start_node, goal_node):
        depth = 0
        total_visited = 0
        path = {}

        def depth_limited_search(start_node, goal_node, depth):
            path.clear()
            result = None
            stack = [(start_node, 0)]
            visited = set()
            while stack:
                node = stack.pop()
                if node[0] == goal_node:
                    visited.add(node[0])
                    return (node[0], len(visited))
                if node[1] > depth:
                    result = "cutoff"
                else:
                    visited.add(node[0])
                    for neighbour in self.graph[node[0]].keys():
                        if neighbour not in visited:
                            path[neighbour] = node[0]
                            stack.append((neighbour, node[1]+1))
            return (result, len(visited))

        while True:
            result = depth_limited_search(start_node, goal_node, depth)
            total_visited += result[1]
            if result[0]:
                if result[0] != 'cutoff':
                    return [total_visited, self.construct_path(path, start_node, goal_node)]
            else:
                return [total_visited]
            depth += 1
