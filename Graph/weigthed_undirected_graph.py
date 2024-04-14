from weighted_graph import weighted_graph

# class for weighted and undirected graphs


class weighted_undirected_graph(weighted_graph):
    def add_edge(self, from_node, to_node, cost):
        weighted_graph.add_edge(self, from_node, to_node)
        if to_node in self.graph[from_node].keys():
            if cost not in self.graph[from_node][to_node]:
                self.graph[from_node][to_node].append(cost)
        else:
            self.graph[from_node][to_node] = [cost]
        if from_node in self.graph[to_node].keys():
            if cost not in self.graph[to_node][from_node]:
                self.graph[to_node][from_node].append(cost)
        else:
            self.graph[to_node][from_node] = [cost]

    def delete_edge(self, from_node, to_node):
        if from_node in self.graph.keys() and to_node in self.graph.keys():
            self.graph[from_node].pop(to_node, None)
            self.graph[to_node].pop(from_node, None)

    # to remove a particular edge with a particular weight
    def delete_edge(self, from_node, to_node, cost):
        if from_node in self.graph.keys() and to_node in self.graph.keys():
            self.graph[from_node][to_node].remove(cost)
            self.graph[to_node][from_node].remove(cost)
