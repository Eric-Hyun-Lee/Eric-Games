class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = []
    def addNeighbor(self, node):
        self.neighbors.append(node)
    def __str__(self):
        NodeString = "Node: " + self.key + "\nNeighbors: " 
        for neighbor in self.neighbors:
            NodeString+=neighbor.key + ", "
        return(NodeString)
Node1 = Node("Bob")
Node2 = Node("Robert")
Node3 = Node("Joebert")
'''
Node1.addNeighbor(Node2)
Node2.addNeighbor(Node1)
Node3.addNeighbor(Node2)
Node2.addNeighbor(Node3)

print(Node1)     
print(Node2)
print(Node3)
'''
class Graph:
    def __init__(self):
        self.graph = {}
    def addEdge(self, NodeUno, NodeDos):
        NodeUno.addNeighbor(NodeDos)
        NodeDos.addNeighbor(NodeUno)
    def addNode(self, Node ):
        self.graph[Node.key] = Node
    def __str__(self):
        GraphString = ""
        for key in self.graph:
            GraphString+=str(self.graph[key])
            GraphString+="\n"
        return GraphString
myGraph = Graph()
myGraph.addNode(Node1)
myGraph.addNode(Node2)
myGraph.addNode(Node3)
myGraph.addEdge(Node1, Node2)
myGraph.addEdge(Node3, Node2)
myGraph.addEdge(Node1, Node3)
print(myGraph)