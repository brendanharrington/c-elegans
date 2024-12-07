import graph_tool.all as gt

def run_loop(g):
    while True:
        print('\n========= OPTIONS =========')
        print('[0]: Print graph')
        print('[1]: Print blockmodel graph')
        print('[q]: Quit')
        
        choice = input('\nEnter the number of what you\'d like to do: ')

        match choice:
            case '0':
                gt.graph_draw(g)
            case '1':
                state = gt.minimize_blockmodel_dl(g)
                state.draw()
            case 'q':
                print('\nQuitting...')
                break
            case _:
                print('\nInvalid entry, try again.')


def average_shortest_path_length(g):
    """
    Calculate the average shortest path length using graph-tool.

    Parameters:
        g (Graph): A graph-tool Graph object.

    Returns:
        float: Average shortest path length.
    """
    # Compute all-pairs shortest distances
    total_length = 0
    total_pairs = 0

    distances = gt.shortest_distance(g, weights=g.ep.value).a

    

    # for v in g.vertices():
    #     distances = gt.shortest_distance(g, source=v, weights=g.ep.value).a  # Get as numpy array
    #     finite_distances = distances[distances < float("inf")]
    #     total_length += finite_distances.sum()
    #     total_pairs += len(finite_distances) - 1  # Exclude self-distances

    if total_pairs > 0:
        return total_length / total_pairs
    else:
        return float("inf")

def print_summmary_statistics(g):
    dist_unweighted, ends_unweighted = gt.pseudo_diameter(g)
    dist_weighted, ends_weighted =  gt.pseudo_diameter(g, weights=g.ep.value)
    c, num_triangles, num_triples = gt.global_clustering(g, weight=g.ep.value, ret_counts=True)
    
    print('\nDiameter (unweighted):', dist_unweighted)
    print('Pseudo-diameter: (weighted):', dist_weighted)
    print('Average shortest path length:', average_shortest_path_length(g))
    print('Clustering coefficient:', c[0], 'with standard deviation', c[1])
    print('Number of triangles:', num_triangles)
    print('Number of triples:', num_triples)

def print_motif_statistics(g):
    num_v_in_motif = 3
    motifs, num_motifs = gt.motifs(g, num_v_in_motif)
    print('Number of motifs:', num_motifs)