class MyGraph:
    def __init__(self) -> None:
        self.noOfNode = 0
        self.adjacencyList = {}

    def addVertex(self, node):
        self.adjacencyList[node] = []
        self.noOfNode += 1
        return None
    
    def addEdges(self, node1, node2):
        self.adjacencyList[node1].append(node2)
        self.adjacencyList[node2].append(node1)
        return None
    
graph = MyGraph()
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(0)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)

graph.addEdges(0, 1)
graph.addEdges(0, 2)
graph.addEdges(3, 1)
graph.addEdges(2, 1)
graph.addEdges(2, 4)
graph.addEdges(3, 4)
graph.addEdges(5, 4)
graph.addEdges(5, 6)

print(graph.adjacencyList)