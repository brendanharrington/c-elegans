import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

import functions as fnc

def purgatory():
    purgatory = True

def main():
    g = gt.collection.data["celegansneural"]
    state = gt.minimize_blockmodel_dl(g)



if __name__ == "__main__":
    main()