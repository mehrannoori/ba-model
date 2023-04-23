import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random

G = []

def readData(filename):
    fileObj = open(filename)
    while True:
        line = fileObj.readline()
        if not line: break
        r = line.split(',')
        r2 = []
        for i in r[:-1]:
            r2.append(int(i))
        G.append(r2)
    plt.show()


def draw():
    A = np.array(G)
    Graph = nx.from_numpy_matrix(A)
    nx.draw(Graph, node_size=10)
    plt.show()

readData('adj100.txt')
draw()