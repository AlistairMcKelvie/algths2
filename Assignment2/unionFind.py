class UnionFind:
    """
    Class that implements the union-find structure with
    union by rank and find with path compression
    """
     
    def __init__(self, n):
        self.parent = list(range(n))
        self.root_count = len(self.parent)
        self.rank = [0 for x in range(n)]
 
    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
 
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        self.root_count -= 1
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1
