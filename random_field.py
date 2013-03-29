#!/usr/bin/env python3
import random
import node_map
import nodes


def main(amount_of_nodes, max_x, max_y, max_range, max_connections,
         readymap=None):
    mymap = node_map.NodeMap(amount_of_nodes, max_x, max_y, readymap)
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
            all_nodes = {}
            for node2 in mymap:
                all_nodes[node] = node.measure_distance(node2)
            chosen_nodes.append(min(all_nodes))
        for node2 in chosen_nodes:
            node2.add_neighbour(node)

    return mymap

if __name__ == '__main__':
    print(main(100, 20, 20, 10, 10))
