import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

import functions as fnc

def purgatory():
    return "probably nothing"

def main():
    g = gt.collection.data["celegansneural"]
    reciprocity = gt.edge_reciprocity(g, weight=g.ep.value)
    print(reciprocity)
    

if __name__ == "__main__":
    main()