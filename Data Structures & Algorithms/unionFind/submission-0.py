class UnionFind:
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n


    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x


    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        forest1, forest2 = self.find(x), self.find(y)
        if forest1 == forest2:
            return False
        if self.size[forest1] < self.size[forest2]:
            forest1, forest2 = forest2, forest1
        self.parent[forest2] = forest1
        self.size[forest1] += self.size[forest2]
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
