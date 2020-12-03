import os
import numpy as np
from collections import OrderedDict
from lol_graph_directed import *
import csv


class MultipartiteLol(DLGW):
    def __init__(self, groups_number=0, weighted=True):
        super().__init__(weighted=weighted)
        self.groups_number = groups_number
        self.nodes_type_dict = {}

    def convert_with_csv(self, files_name, graphs_directions=None, header=True):
        s = set()
        for t in graphs_directions:
            s.add(t[0])
            s.add(t[1])
        self.groups_number = len(s)

        # self._map_node_to_number = OrderedDict()
        graph = []
        for i in range(len(files_name)):
            file = files_name[i]
            with open(file, "r") as csvfile:
                datareader = csv.reader(csvfile)
                if header:
                    next(datareader, None)  # skip the headers
                for edge in datareader:
                    named_edge = [str(graphs_directions[i][0]) + "_" + edge[0],
                                  str(graphs_directions[i][1]) + "_" + edge[1]]
                    if self.is_weighted():
                        named_edge.append(float(edge[2]))
                    graph.append(named_edge)
                csvfile.close()
        self.convert(graph)

    def return_node_type(self, node):
        return self.nodes_type_dict[node]['type']

    def copy(self):
        new_mp_lol_graph = MultipartiteLol()
        new_mp_lol_graph.reversed_lol = self.reversed_lol.copy()
        new_mp_lol_graph.lol_directed = self.lol_directed.copy()
        new_mp_lol_graph.groups_number = self.groups_number
        new_mp_lol_graph.nodes_type_dict = self.nodes_type_dict.copy()
        return new_mp_lol_graph

    def set_nodes_type_dict(self):
        for node in self.nodes():
            node_type = int(node[0])
            type = [1 if i == node_type else 0 for i in range(self.groups_number)]
            self.nodes_type_dict[node] = {'type': type}

    def initialize_nodes_type_dict(self):
        for node in self.nodes():
            self.nodes_type_dict[node] = {}


if __name__ == '__main__':
    list_of_list_graph = MultipartiteLol()
    rootDir = os.path.join("PathwayProbabilitiesCalculation", "data", "toy_network_1")
    graph_filenames = [os.path.join(dirpath, file) for (dirpath, dirnames, filenames) in
                       os.walk(rootDir) for file in filenames]
    graph_filenames.sort()
    list_of_list_graph.convert_with_csv(graph_filenames, [(0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2)])
    print(list_of_list_graph.predecessors("1_3"))
