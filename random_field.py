import random
import mapp, nodes

def main(amount_of_nodes, max_x, max_y, max_range, max_connections, readymap=None):
    mymap = mapp.Map(amount_of_nodes, max_x, max_y, readymap) 
    for node in mymap:
        all_nodes_within_range = []
        for node2 in mymap:
            if node.measure_distance(node2) < max_range:
                all_nodes_within_range.append(node2)
        if len(all_nodes_within_range) == 0:
            continue

        chosen_nodes = []
        amount_of_nodes_possible = range(max_connections)
        chosen_aofnp = random.choice(amount_of_nodes_possible)
        for i in range(chosen_aofnp):
            if len(all_nodes_within_range) == 0:
                break
            chosen_node = random.choice(all_nodes_within_range)
            all_nodes_within_range.remove(chosen_node)
            chosen_nodes.append(chosen_node)
        if not chosen_nodes:
            print('ALERT: This node has no connections')
        for node2 in chosen_nodes:
            node2.add_neighbour(node)
            
    return mymap

print(main(100, 20, 20, 10, 10))
