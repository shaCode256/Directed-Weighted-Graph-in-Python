import unittest
import src
from src import GraphInterface
from tokenize import Double
from typing import List, Collection
from collections import deque
from src import GraphAlgoInterface, GraphInterface, DiGraph, NodeData
from src.DiGraph import DiGraph
from src.GraphAlgo import  GraphAlgo
import src.GraphAlgo


class MyTestCase(unittest.TestCase):
    graph = DiGraph()

    def setUp(self):  # initializes the nodes counter before each test to be 0.
        NodeData.counter = 0;
        g = DiGraph()
        for n in range(4): # initializes a graph for some tests to use.
            g.add_node(n)
        g.add_edge(0, 1, 17)
        g.add_edge(3, 1, 23)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.8)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.graph = g

    def test_something(self):
        #self.assertEqual(True, False)
        print("graph is", self.graph.get_all_v())
        print("graph size is", self.graph.v_size())
      #  print("pupu", self.graph.all_out_edges_of_node(1).get(3))

    def test_getGraph(self):
        #return -> GraphInterface:
        """
        Test getGraph method.
        """

    def get_graph_in_class(self):
        #retuen -> DiGraph:
        """
        Test getGraph method.
        """

    def test_load_from_json(self, file_name: str):
        #return -> bool:
        """
        Test load to json method
        """

    def test_save_to_json(self, file_name: str):
        # return -> bool:
        """
        Test save to json method
        """

    def test_shortest_path_a(self, src, dest):
        """
        Test shortest_path_ method
        """

    def test_shortest_path_dist(self, src, dest):
        self
        """
        Test shortest_path_dist method
        """

    def test_shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Test shortest_path method
        """

    def test_dfs(self, G):
        """
        Test dfs method
        """

    def test_reverse_graph(self) -> DiGraph:
        """
        Test reverse_graph method
        """

    def test_DFSVISIT(self, G, vertex):
        """
        Test DFSVISIT method (first DFS travesal, which updates the tropological list of nodes)
        """

    def test_reverse_graph(self):
        """
        Test reversing the graph method
        """

    def test_dfsTropologic(self, G):
        """
        Test DFS method (on the tropoligcal list of nodes)
        """

    def test_DFSVISITTropoligic(self, G, vertex):
        """
        Test Test DFSVISIT method (on the tropoligcal list of nodes)
        """

    def test_connected_componentsA(self, id1: int):
        #return list
        """
        Test id Finding the Strongly Connected Component(SCC) that node id1 is a part of works OK.
        """

    def test_connected_componentsB(self):
        #return -> list[list]:
        """
        Test if Finding all the Strongly Connected Component(SCC) in the graph works OK.
        """

    def test_plot_graph(self):
        """
        Test plot_graph method
        """


if __name__ == '__main__':
    unittest.main()
