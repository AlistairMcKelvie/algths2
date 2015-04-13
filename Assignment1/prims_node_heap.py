from heapq import heapify, heappush, heappop
import time

def prims(file):
    start_time = time.time()
    min_spanning_tree = []

    total_cost = 0
    with open(file, 'r') as f:
        node_count, edge_count = [int(i) for i in f.readline().split()]
        nodes = [[] for i in range(node_count)]
        # for both nodes in each edge, add other edge and its cost to it's index in the node list
        # subtract 1 to make the edges base 0 to match list indices
        for i in range(edge_count):
            node1, node2, cost = f.readline().split()
            nodes[int(node1)-1].append({'node': int(node2) - 1, 'cost': int(cost)})
            nodes[int(node2)-1].append({'node': int(node1) - 1, 'cost': int(cost)})

    X = {1}
    # rem
    costed_nodes = []
    for node in nodes:
        recalculate_node_cost_and_push_to_heap(node, costed_nodes)

    heapify(recosted_nodes)
    print recosted_nodes

    # while len(X) < node_count:
        
        
        
def recalculate_node_cost_and_push_to_heap(node, heap):
    recosted_edges = []
    for edge in node:
        if edge['node'] in X:
            recosted_edges.append((edge['cost'], edge['node']))
        else:
            recosted_edges.append((999999, edge['node']))
    print node
    print recosted_edges
    raw_input("Press Enter to continue...")