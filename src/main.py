import graph_tool.all as gt

def main():
    g = gt.Graph()
    v1 = g.add_vertex()
    v2 = g.add_vertex()
    gt.graph_draw(g, vertex_text=g.vertex_index, output="two-nodes.svg")
    
if __name__ == "__main__":
    main()