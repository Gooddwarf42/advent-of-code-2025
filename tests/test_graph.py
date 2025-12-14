import pytest

from utils.graph import WeightedGraph, WeightedEdgeInfo


def test_add_edge():
    #arrange
    nodes = [1,2,3,4]
    graph = WeightedGraph(nodes)
    
    #act
    graph.add_edge(2,3,1)
    graph.add_edge(2,1,2)
    
    #assert
    assert graph.edges == {
        1: [],
        2: [WeightedEdgeInfo(to=3, weight=1), WeightedEdgeInfo(to=1, weight=2)],
        3: [],
        4: [],
    }


def test_add_edge_rises_when_adding_already_existing_edge():
    # arrange
    nodes = [1, 2, 3, 4]
    graph = WeightedGraph(nodes)

    # act
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 1, 2)

    # assert
    with pytest.raises(Exception):
        graph.add_edge(2, 1, 4)
        
def test_add_edge_rises_when_adding_edge_to_invalid_vertex():
    # arrange
    nodes = [1, 2, 3, 4]
    graph = WeightedGraph(nodes)

    # act
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 1, 2)

    # assert
    with pytest.raises(Exception):
        graph.add_edge(2, 44, 4)


def test_djikstra():
    # Create a simple graph
    g = WeightedGraph(vertexes=["A", "B", "C", "D"])
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)

    # Run Dijkstra from "A"
    distances = g.djikstra("A")

    # Expected shortest distances from A
    expected = {
        "A": 0,
        "B": 1,
        "C": 3,  # A->B->C is shorter than A->C
        "D": 4,  # A->B->C->D or A->B->D
    }

    assert distances == expected
