class Graph:
    
    def __init__(self):
        self.vertex = defaultdict(set)
        self.size = 0
        

    def addEdge(self, src: int, dst: int) -> None:
        self.vertex[src].add(dst)
        if dst not in self.vertex:
            self.vertex[dst]
        

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.vertex and dst in self.vertex:
            self.vertex[src].remove(dst)
            return True
        return False

            

    def hasPath(self, src: int, dst: int) -> bool:
        stack = []
        hasSeen = set()
        for i in self.vertex[src]:
            stack.append(i)
            hasSeen.add(i)
        while stack:
            curr = stack[-1]
            stack.pop()
            if curr == dst:
                return True
            for j in self.vertex[curr]:
                if j not in hasSeen:
                    stack.append(j)
                    hasSeen.add(j)
        return False
                
