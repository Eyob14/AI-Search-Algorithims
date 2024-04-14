from graph import Graph
# class for unweighted and directed graphs


class unweighted_directed_graph(Graph):
    def add_edge(self, from_node, to_node):
        Graph.add_edge(self, from_node, to_node)
        # since the graph is unweighted the cost is initialized as None
        self.graph[from_node][to_node] = None

    def delete_edge(self, from_node, to_node):
        if from_node in self.graph.keys() and to_node in self.graph.keys():
            self.graph[from_node].pop(to_node, None)
