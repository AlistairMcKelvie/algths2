import time

def prims_basic(file):
    start_time = time.time()
    min_spanning_tree = []
    total_cost = 0
    with open(file, 'r') as f:
        node_count, edge_count = [int(i) for i in f.readline().split()]
        edges = []
        for i in range(edge_count):
            node1, node2, cost = f.readline().split()
            edges.append({'node1': int(node1), 'node2': int(node2), 'cost': int(cost)})
    X = {1}
    Y = set()
    for i in range(2, node_count + 1):
        Y.add(i)

    while Y:
        crossing_edges = []
        for edge in edges:
            # Check if one end of edge is inside X and one outside
            if (edge['node1'] in X) ^ (edge['node2'] in X):
                crossing_edges.append(edge)
                min_edge=min(crossing_edges, key=lambda x: x['cost'])
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
