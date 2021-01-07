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

    global is_not_connected
    global connected
    global algo

    def setUp(self):
        g = DiGraph()
        for n in range(15):
            g.add_node(n)
        g.add_edge(0, 9, 2.5)
        g.add_edge(1, 9, 6.7)
        g.add_edge(4, 9, 40)
        g.add_edge(3, 10, 7)
        g.add_edge(3, 13, 27)
        g.add_edge(3, 2, 4.5)
        g.add_edge(14, 5, 21)
        g.add_edge(14, 8, 41)
        g.add_edge(11, 2, 17)
        self.is_not_connected = g

        graph = DiGraph()
        for n in range(10):
            graph.add_node(n)
        graph.add_edge(0, 1, 12)
        graph.add_edge(1, 2, 67)
        graph.add_edge(2, 3, 43)
        graph.add_edge(3, 4, 17)
        graph.add_edge(4, 5, 27)
        graph.add_edge(5, 6, 4.5)
        graph.add_edge(6, 7, 21)
        graph.add_edge(7, 8, 41)
        graph.add_edge(8, 9, 11.23)
        graph.add_edge(9, 0, 13.765649959)
        self.connected = graph

        self.algo = GraphAlgo(self.connected)
        """The methode create 2 graphs for this unittest. connected graph and the other one isn't connected"""

    def test_save_load(self):
        print("algo is operating now on connected:" + str(self.algo.get_graph().as_dict()))
        print()
        self.assertFalse(self.algo.save_to_json(""))
        self.assertTrue(self.algo.save_to_json("OurGraph"))
        self.algo.__init__(self.is_not_connected)
        print("algo is operating now on is _not_connected:" + str(self.algo.get_graph().as_dict()))
        print()
        self.assertFalse(self.algo.load_from_json(""))
        self.assertFalse(self.algo.load_from_json("fakefile"))
        self.assertTrue(self.algo.load_from_json("OurGraph"))
        self.assertFalse(self.algo.get_graph().__eq__(self.is_not_connected))
        self.assertTrue(self.algo.get_graph().__eq__(self.connected))
        print("algo is operating now on connected:" + str(self.algo.get_graph().as_dict()))
        print()
        """Initialization algo on Connected. Then, save Connected in file whose name is "OurGraph".
        After this, replace the graph of algo to is_not_onnected.
        Load algo on "myGraph" file. Now, algo operates Connected again, instead of is_not_onnected."""

    # def test_getGraph(self):
    #     #return -> GraphInterface:
    #     """
    #     Test getGraph method.
    #     """
    #
    # def get_graph_in_class(self):
    #     #retuen -> DiGraph:
    #     """
    #     Test getGraph method.
    #     """
    #
    # def test_shortest_path_a(self, src, dest):
    #     """
    #     Test shortest_path_ method
    #     """
    #
    # def test_shortest_path_dist(self, src, dest):
    #     self
    #     """
    #     Test shortest_path_dist method
    #     """
    #
    # def test_shortest_path(self, id1: int, id2: int) -> (float, list):
    #     """
    #     Test shortest_path method
    #     """
    #
    # def test_dfs(self, G):
    #     """
    #     Test dfs method
    #     """
    #
    # def test_reverse_graph(self) -> DiGraph:
    #     """
    #     Test reverse_graph method
    #     """
    #
    # def test_DFSVISIT(self, G, vertex):
    #     """
    #     Test DFSVISIT method (first DFS travesal, which updates the tropological list of nodes)
    #     """
    #
    # def test_reverse_graph(self):
    #     """
    #     Test reversing the graph method
    #     """
    #
    # def test_dfsTropologic(self, G):
    #     """
    #     Test DFS method (on the tropoligcal list of nodes)
    #     """
    #
    # def test_DFSVISITTropoligic(self, G, vertex):
    #     """
    #     Test Test DFSVISIT method (on the tropoligcal list of nodes)
    #     """
    #
    # def test_connected_componentsA(self, id1: int):
    #     #return list
    #     """
    #     Test id Finding the Strongly Connected Component(SCC) that node id1 is a part of works OK.
    #     """
    #
    # def test_connected_componentsB(self):
    #     #return -> list[list]:
    #     """
    #     Test if Finding all the Strongly Connected Component(SCC) in the graph works OK.
    #     """
    #
    # def test_plot_graph(self):
    #     """
    #     Test plot_graph method
    #     """


if __name__ == '__main__':
    unittest.main()
