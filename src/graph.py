import math
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, rate):
        self.graph[from_vertex][to_vertex] = rate

    def update_edge(self, from_vertex, to_vertex, new_rate):
        if from_vertex in self.graph and to_vertex in self.graph[from_vertex]:
            self.graph[from_vertex][to_vertex] = new_rate
        else:
            print(f"No existing edge from {from_vertex} to {to_vertex} to update.")

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def detect_arbitrage(self):
        dist = {
            v: {w: float("inf") if v != w else 0 for w in self.graph}
            for v in self.graph
        }
        pred = {v: {w: None for w in self.graph} for v in self.graph}

        for u in self.graph:
            for v, weight in self.graph[u].items():
                dist[u][v] = -math.log(weight)

        for t in self.graph:
            for u in self.graph:
                for v in self.graph:
                    if dist[u][v] > dist[u][t] + dist[t][v]:
                        dist[u][v] = dist[u][t] + dist[t][v]
                        pred[u][v] = pred[t][v]

        for u in self.graph:
            if dist[u][u] < 0:
                arbitrage_cycle = self._reconstruct_path(pred, u)
                return True, arbitrage_cycle

        return False, []

    def _reconstruct_path(self, predecessors, start_vertex):
        path = []
        current = start_vertex
        while current is not None:
            path.append(current)
            current = predecessors[start_vertex][current]
            if current == start_vertex:
                break
        return path

    def compute_arbitrage_value(self, path, initial_investment):
        value = initial_investment
        for i in range(len(path) - 1):
            from_vertex = path[i]
            to_vertex = path[i + 1]
            value *= self.graph[from_vertex][to_vertex]
        return value
