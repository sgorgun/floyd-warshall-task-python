"""Template for programming assignment: Finding all-pairs shortest paths."""
from typing import List, Tuple


def get_sum_of_all_pairs_shortest_paths(n: int, adj_matrix: List[List[int]]) -> Tuple[int, int]:
    """
    Returns the tuple, where the first value is the sum of all-pairs shortest paths between all achievable vertices
    and the second is the number of the unachievable pairs of vertices in an undirected weighted graph.
    The weight of (u,v)-edge represents a distance between 'u' and 'v' and vice versa.

    Edges are stored as an adjacency matrix, where 0 means no edge and a positive value means edge presence and
    reflects its weight.
    Expected algorithm complexity is O(N^3), where N - number of vertices.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. there is a graph with 4 vertices from 0 to 2 and adjacency matrix:
    [[0, 10, 5], [10, 0, 6], [5, 6, 0]]
    The expected result is (42, 0).

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        adj_matrix (List[List[int]]): adjacency matrix with weights
    Returns:
        Tuple [int, int]: the sum of all-pairs shortest paths between all achievable vertices
        and the number of the unachievable pairs of vertices
    """
    pass
