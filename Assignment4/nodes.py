#!/usr/bin/env python2
import networkx as nx

nodes = [70,100,500,1000,4000,6000,10000,100000]

z_deg = 13
for n in nodes:
	p = 1.0*z_deg/(n-1)
	G = nx.fast_gnp_random_graph(n, p, seed=123)
	print p,n
	print nx.is_connected(G)




# Z average degree
#G = fast_gnp_random_graph(n, p, seed=123)
#average_shortest_path_length(G, weight=None)
# Check if the graph is complete

# watts_strogatz_graph(n, k, p, seed=None)
# k = 4
# n = constant
# change p paramater [0.0001 to 1]
# Averagre shortest path 
# Average Clustering coefficient


# Many the avg_cluster, shortest path


#G = nx.erdos_renyi_graph(n, p, seed=123)
#  O(n^2)
# z_deg = (n - 1) * p

