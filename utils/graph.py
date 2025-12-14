from dataclasses import dataclass
from queue import PriorityQueue, Queue
from typing import TypeVar, Generic

MAX_INT = 10 ** 30  # safer

T = TypeVar("T")


@dataclass(frozen=True)
class WeightedEdgeInfo(Generic[T]):
    to: T
    weight: int

class WeightedGraph(Generic[T]):
    edges: dict[T, list[WeightedEdgeInfo[T]]]

    def __init__(self, vertexes: list[T]):
        self.edges = {k: [] for k in vertexes}

    def add_edge(self, source: T, dest: T, weight: int):
        edges = self.edges[source]
        if any(edge.to == dest for edge in edges):
            raise Exception("Invalid edge added")
        if all(vertex != dest for vertex in self.edges.keys()):
            raise Exception("Invalid edge added")
        edges.append(WeightedEdgeInfo(dest, weight))

    def djikstra(self, start: T) -> dict[T, int]:
        distances: dict[T, int] = {k: MAX_INT for k in self.edges.keys()}
        distances[start] = 0
        
        #should use a priority queue here, but I don't know of an easy way to update priorities on the fly here
        queue = Queue()
        
        def push(node: T):
            queue.put(node)
        
        push(start)
        
        while not queue.empty():
            current = queue.get()
            current_distance = distances[current]
            edges = self.edges[current]
            for edge in edges:
                edge_distance = current_distance + edge.weight
                if edge_distance >= distances[edge.to]:
                    continue
                # shorter path found! update distance and enqueue
                distances[edge.to] = edge_distance
                push(edge.to)

        return distances
