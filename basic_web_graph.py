"""
For this question, you will create a generic Graph class 
that provides a more abstract way of representing the web graph.
"""

"""
Graph module.
"""

class Graph(object):
    """
    Represents a directed graph.
    """

    def __init__(self):
        """
        Initializes the Graph to an empty graph with no nodes or edges.
        """
        self._graph = {}

    def add_node(self, node):
        """
        If node is already in the graph, returns False and does not modify the graph.
        Otherwise, adds node to the graph and returns True.
        """
        if node not in self._graph:
            self._graph[node] = []
            return True
        return False

    def has_node(self, node):
        """
        Returns True if node is a node in the graph.
        """
        if node in self._graph:
            return True
        return False


    def add_edge(self, node1, node2):
        """
        Requires: node1 and node2 are nodes in self.
        Modifies: self
        Adds an edge from node1 to node2 to self.
        """
        if node1 in self._graph:
            if node2 in self._graph:
                self._graph[node1].append(node2)

    def get_nodes(self):
        """
        Returns a frozenset containing the nodes in the graph.
        """
        return frozenset(self._graph.keys())

    def get_outlinks(self, node):
        """
        Requires: node is a node in self.
        Returns a frozenset of the nodes to which node is connected.
        """
        if node in self._graph:
            return frozenset(self._graph[node])

    def get_inlinks(self, target):
        """
        Requires: node is a node in self.
        Returns a set of the nodes that are connected by an edge to node.
        """
        nodes = set()
        if target in self._graph:
            for element in self._graph:
                if target in self._graph[element]:
                    nodes.add(element)
        return nodes
    
    def __str__(self):
        """
        Returns a string representation of the graph. 
        """
        return "This is a basic web graph"