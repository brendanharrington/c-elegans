import graph_tool.all as gt
import functions as fnc

def main():
    g = gt.collection.data["celegansneural"]
    print("\nDataset for C. elegans loaded with", g.num_edges(), 'edges and', g.num_vertices(), 'vertices.')
    fnc.run_loop(g)
    
    
if __name__ == "__main__":
    main()