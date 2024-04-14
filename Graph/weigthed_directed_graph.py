from weighted_graph import weighted_graph
# class for weighted and directed graphs


class weighted_directed_graph(weighted_graph):
    def add_edge(self, from_node, to_node, cost):
        weighted_graph.add_edge(self, from_node, to_node)
        if to_node in self.graph[from_node].keys():
            self.graph[from_node][to_node].append(cost)
        else:
            self.graph[from_node][to_node] = [cost]

    def delete_edge(self, from_node, to_node):
        if from_node in self.graph.keys() and to_node in self.graph.keys():
            self.graph[from_node].pop(to_node, None)
            
    # to remove a particular edge with a particular weight
    def delete_edge(self, from_node, to_node, cost):
        if from_node in self.graph.keys() and to_node in self.graph.keys():
            self.graph[from_node][to_node].remove(cost)
