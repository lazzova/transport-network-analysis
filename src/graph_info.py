#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx


def dict_to_sorted_list (dictionary):
    """Utilitiy - builds sorted (by value) list of tuples out of dictionary"""
    dict_list = [item for item in dictionary.items()]
    dict_list.sort(key = lambda tup: tup[1], reverse = True)
    return dict_list


def output_basic_info (graph, path):
    """Output basic information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
    """
    with open(path, 'w') as out:
        out.write('***Basic***\n')
        out.write(nx.info(graph))


def output_conectivity_info (graph, path):
    """Output connectivity information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
    """
    with open(path, 'w') as out:
        out.write('***Conectivity***\n')
        out.write('Is weakly connected: %s\n' % nx.is_weakly_connected(graph))
        out.write('Number of weakly connected components: %d\n' % nx.number_weakly_connected_components(graph))
        out.write('Is strongly connected: %s\n' % nx.is_strongly_connected(graph))
        out.write('Number of strongly connected components: %d' % nx.number_strongly_connected_components(graph))


def output_aperiodicity_info (graph, path):
    """Output aperiodicity information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
    """
    with open(path, 'w') as out:
        out.write('***Aperiodicity***\n')
        out.write('Is aperiodic: %s' % nx.is_aperiodic(graph))


def output_indegree_centrality_info (graph, path, nodes_dict):
    """Output In-degree centrality information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
       nodes_dict: (dictionary) maps node id to node name
    """
    indeg_dict = nx.in_degree_centrality(graph)
    indeg_dict = dict((nodes_dict[key], indeg_dict[key]) for key in nodes_dict)
    indeg_list = dict_to_sorted_list(indeg_dict)

    with open(path, 'w') as out:
        out.write('***In-Degree Centrality***\n')
        out.write('Node\tLayer\tIn-degree centrality\n')
        for element in indeg_list:
            out.write('%d\t%d\t%f\n' % (element[0][0], element[0][1], element[1]))


def output_outdegree_centrality_info (graph, path, nodes_dict):
    """Output Out-degree centrality information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
       nodes_dict: (dictionary) maps node id to node name
    """
    outdeg_dict = nx.out_degree_centrality(graph)
    outdeg_dict = dict((nodes_dict[key], outdeg_dict[key]) for key in nodes_dict)
    outdeg_list = dict_to_sorted_list(outdeg_dict)

    with open(path, 'w') as out:
        out.write('***Out-Degree Centrality***\n')
        out.write('Node\tLayer\tOut-degree centrality\n')
        for element in outdeg_list:
            out.write('%d\t%d\t%f\n' % (element[0][0], element[0][1], element[1]))


def output_closeness_centrality_info (graph, path, nodes_dict):
    """Output Closeness centrality information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
       nodes_dict: (dictionary) maps node id to node name
    """
    closeness_dict = nx.closeness_centrality(graph, distance='weight')
    closeness_dict = dict((nodes_dict[key], closeness_dict[key]) for key in nodes_dict)
    closeness_list = dict_to_sorted_list(closeness_dict)

    with open(path, 'w') as out:
        out.write('***Closeness Centrality***\n')
        out.write('Node\tLayer\tCloseness centrality\n')
        for element in closeness_list:
            out.write('%d\t%d\t%f\n' % (element[0][0], element[0][1], element[1]))


def output_betweeness_centrality_info (graph, path, nodes_dict):
    """Output Betweeness centrality information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
       nodes_dict: (dictionary) maps node id to node name
    """
    betweeness_dict = nx.betweenness_centrality(graph, weight='weight', endpoints=True)
    betweeness_dict = dict((nodes_dict[key], betweeness_dict[key]) for key in nodes_dict)
    betweeness_list = dict_to_sorted_list(betweeness_dict)

    with open(path, 'w') as out:
        out.write('***Betweeness Centrality***\n')
        out.write('Node\tLayer\tBetweeness centrality\n')
        for element in betweeness_list:
            out.write('%d\t%d\t%f\n' % (element[0][0], element[0][1], element[1]))