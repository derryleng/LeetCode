# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

class Graph:
    def __init__(self, default_missing_weight: float = -1.0, default_self_edge_weight: float = 1.0):
        self.graph: Dict[str, Dict[str, float]] = {}
        self.default_missing_weight: float = default_missing_weight
        self.default_self_edge_weight: float = default_self_edge_weight

    def add_node(self, node: str) -> None:
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, edge: List[str], weight: float) -> None:
        source, destination = edge
        self.add_node(source)
        self.add_node(destination)
        self.graph[source][destination] = weight
        self.graph[destination][source] = 1/weight

    def get_edge_weight(self, edge: List[str]) -> float:
        source, destination = edge
        if source not in self.graph or destination not in self.graph:
            return self.default_missing_weight
        return self.dfs(source, destination, set())
    
    def dfs(self, current: str, destination: str, visited: set) -> float:
        if current == destination:
            return 1.0
        visited.add(current)
        for neighbour, edge_weight in self.graph.get(current, {}).items():
            if neighbour not in visited:
                result = self.dfs(neighbour, destination, visited)
                if result != self.default_missing_weight:
                    return edge_weight * result
        return self.default_missing_weight

    def __str__(self) -> str:
        graph_str = ""
        for node, edges in self.graph.items():
            graph_str += f"Node: {node}\n"
            for neighbor, weight in edges.items():
                graph_str += f"  -> Neighbor: {neighbor}, Weight: {weight}\n"
        return graph_str

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = Graph()
        for equation, value in zip(equations, values):
            graph.add_edge(equation, value)
        ans = [graph.get_edge_weight(query) for query in queries]
        return ans
