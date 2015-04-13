from rcdtype import *

Node = recordtype('Node', 'parent rank')

def read_data(file):
    nodes = UnionFind()
    with open(file, 'r') as f:
        __, bit_len = f.readline().split()
        bit_len = int(bit_len)
        for row in f:
            node = int(''.join(row.split()), 2)
            if node not in nodes:
                # set up each node with itself as a parent, and rank 0
                nodes.insert(node)
                # print 'adding ' + bin(node) + ' to nodes'
                # print 'cluster_count', nodes.cluster_count
                # print '-------'
            else:
                # If there are duplicate node, join them
                # and reduce cluster count by one
                # print bin(node) + ' already in node, not changing node_count'
                # print '-------'
                pass
    return nodes, bit_len
    
def generate_difs(bit_len):
    oneDif = []
    twoDif = []
    for i in range(bit_len - 1, -1, -1):
        a = ['0'] * bit_len
        a[i] = '1'
        oneDif.append(int(''.join(a), 2))
        
    for i in range(bit_len - 2, -1, -1):
        for j in range(bit_len - 1, i, -1):
            if j != i:
                a = ['0'] * bit_len
                a[i] = '1'
                a[j] = '1'
                twoDif.append(int(''.join(a), 2))
    return (oneDif, twoDif)

def q2(file):
    nodes, bit_len = read_data(file)
    #for i in nodes:
        # print bin(i)
    #    pass
    # print '----------'
    # Check if any node is one bit different from this node
    
    oneDif, twoDif = generate_difs(bit_len)
    
    for node in nodes:
        # Check if any node is one bit different from this node
        for dif in oneDif:
            other_node = node ^ dif
            if other_node in nodes:
                # print 'joining ' + bin(node) + ' and ' + bin(other_node)
                nodes.union(node, other_node)
                # print 'cluster_count', nodes.cluster_count
                # print '-------'
    # Check if any node is two bits different from this node
    for node in nodes:
        for dif in twoDif:
            other_node = node ^ dif
            if other_node in nodes:
                # print 'joining ' + bin(node) + ' and ' + bin(other_node)
                nodes.union(node, other_node)
                # print 'cluster_count', nodes.cluster_count
                # print '-------'
    return nodes.cluster_count

class UnionFind(dict):
    def __init__(self):
        self.cluster_count = 0

    def insert(self, node):
        self[node] = Node(node, 0)
        self.cluster_count += 1

    def find(self, node):
        if self[node].parent != node:
            self[node].parent = self.find(self[node].parent)
        return self[node].parent
 
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        self.cluster_count -= 1
        if self[xRoot].rank > self[yRoot].rank:
            self[yRoot].parent = xRoot
        else:
            self[xRoot].parent = yRoot
            if self[xRoot].rank == self[yRoot].rank:
                self[yRoot].rank += 1
