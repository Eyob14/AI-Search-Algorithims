#Test for centrality

from data import graph
import numpy as np
#Generate adgacency matrix from a graph
def adj_matrix(graph):
    adjacency_matrix=[];
    for nodeA in graph.graph:
        row=[]
        for nodeB in graph.graph:
            #if nodeB is a neighbour of nodeA
            if nodeB in graph.graph[nodeA]:
                row.append(1)
            else:
                row.append(0)
        adjacency_matrix.append(row)
    return adjacency_matrix
#implementation for degree centrality
def degree_centrality(graph):
    return_dict={};
    for node in graph.graph:
        return_dict[node.value]=len(graph.graph[node])
    return return_dict
#implementation for closeness centrality
def closeness_centrality(graph):
    return_dict={};
    for nodeA in graph.graph:
        Sum=0
        for nodeB in graph.graph:
            if nodeB==nodeA:
                continue;
            totalVisited,path,cost=graph.ucs(nodeA,nodeB);
            Sum+=cost;
        return_dict[nodeA.value]=1/Sum;
    return return_dict
#implementation for betweeness centrality
def betweeness_centrality(graph):
    return_dict={};
    all_short_paths=[];
    visited=set();
    for nodeA in graph.graph:
        for nodeB in graph.graph:
            if nodeB==nodeA or nodeB in visited:
                continue
            totalVisited,path,cost=graph.ucs(nodeA,nodeB)
            all_short_paths.append(path);
        visited.add(nodeA)
    for node in graph.graph:
        Sum=0
        for path in all_short_paths:
            if node.value in path:
                if node.value!=path[0] and node.value!=path[-1]:
                    Sum+=1;
        return_dict[node.value]=Sum;
    return return_dict
#implementation for eigenvector centrality
def eigenvector_centrality(graph):
    adjacency_matrix=adj_matrix(graph);
    adjacency_matrix=np.array(adjacency_matrix).transpose()
    eigenvalues,eigenvectors=np.linalg.eig(adjacency_matrix)
    #find the index of the max value from eigenvalues
    max_eigenvalue_index = np.argmax(eigenvalues)
    #find the column with the given max_value_index
    #to get the eigenvector corresponding to the max
    #eigen value
    max_eigenvector = eigenvectors[:, max_eigenvalue_index]
    #normalize eigenvector centrality by dividing it by the max eigenvalue
    eigenvector_centrality = max_eigenvector / max(eigenvalues)
    result={k.value:v for k,v in zip(graph.graph.keys(),eigenvector_centrality)}
    return result
#implementation for katz centrality
def katz_centrality(graph,alpha=0.1,beta=1.0):
    adjacency_matrix=adj_matrix(graph);
    adjacency_matrix=np.array(adjacency_matrix).transpose()
    len_matrix=len(adjacency_matrix);
    eigenvalues, eigenvectors = np.linalg.eig(adjacency_matrix)
    max_eigenvalue = max(eigenvalues)
    #in order for katz centrality to work this
    #is a condition that must be respected
    if alpha<1/max_eigenvalue:
        #the katz matrix is computed by (I-alpha*A^T)^-1
        #at the end we subtract an identity vector to normalize 
        #the result then finally the resulting matrix is multiplied 
        #by beta to find the katz_centrality
        katz_matrix=np.linalg.inv(np.eye(len_matrix)-alpha*adjacency_matrix)-np.eye(len_matrix)
        katz_centrality=beta*np.dot(katz_matrix,np.ones(len_matrix))
        return {k.value:v for k,v in zip(graph.graph.keys(),katz_centrality)}
#implementation for pageRank centrality
def pageRank_centrality(graph,alpha=0.1,beta=1.0):
    adjacency_matrix=adj_matrix(graph);
    adjacency_matrix=np.array(adjacency_matrix).transpose()
    len_matrix=len(adjacency_matrix);
    #diagonal matrix that contains number of outgoing edges for each node
    Diag=np.diag(np.sum(adjacency_matrix,axis=1))
    eigenvalues, eigenvectors=np.linalg.eig(np.dot(adjacency_matrix,np.linalg.inv(Diag)))
    max_eigenvalue=max(eigenvalues)
    #in order for pageRank centrality to work this
    #is a condition that must be respected
    if alpha<1/max_eigenvalue:
        pageRank_matrix=np.linalg.inv(np.eye(len_matrix)-alpha*np.dot(adjacency_matrix,np.linalg.inv(Diag)));
        pageRank_centrality=beta*np.dot(pageRank_matrix,np.ones(len_matrix));
        return {k.value:v for k,v in zip(graph.graph.keys(),pageRank_centrality)}