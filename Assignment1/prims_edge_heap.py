from heapq import heapify, heappush, heappop
import time

def prims_edge_heap(file):
    start_time = time.time()
    min_spanning_tree = []
    total_cost = 0
    with open(file, 'r') as f:
        node_count, edge_count = [int(i) for i in f.readline().split()]
        edges = []
        for i in range(edge_count):
            node1, node2, cost = f.readline().split()
            edges.append((int(cost),{'node1': int(node1), 'node2': int(node2), 'cost': int(cost)}))
    heapify(edges)
    X = {1}
    Y = set()
    for i in range(2, node_count + 1):
        Y.add(i)

    while Y:
        cross_found = False
        popped_edges = []

        # Pop off heap till crossing edge found
        while not cross_found:
            edge = heappop(edges) 
            # Check if one end of edge is inside X and one outside
            if (edge[1]['node1'] in X) ^ (edge[1]['node2'] in X):
                min_edge = edge[1]
                cross_found = True
            else:
                popped_edges.append(edge)
        
        # Put unused edges back in heap
        for edge in popped_edges:
            heappush(edges, edge)
                
        if min_edge['node1'] in X:
            Y.remove(min_edge['node2'])
            X.add(min_edge['node2'])
        else:
            Y.remove(min_edge['node1'])
            X.add(min_edge['node1'])
        min_spanning_tree.append(min_edge)
        total_cost += min_edge['cost']
    print 'run time: {}'.format(time.time() - start_time)
    return total_cost
