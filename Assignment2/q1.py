from unionFind import UnionFind

def q1(file, target_clusters):
    with open(file, 'r') as f:
        node_count = int(f.readline())
        edges = []
        for row in f:
            node1, node2, cost = row.split()
            edges.append((int(node1) - 1, int(node2) - 1, int(cost)))

    edges.sort(key = lambda x: x[2])
    uf = UnionFind(node_count)
    for edge in edges:
        uf.union(edge[0], edge[1])
        if uf.root_count < target_clusters:
            return edge[2]

