import path

def find(begin, goal):
    queue = []
    complete = []

    queue.append(path.Path(goal, begin))


    while True:
        path = queue.pop()
        node = path[-1]
        for nb in node.neighbours:
            # don't go backwards
            if nb in path: continue
            new_path = path.add_node(nb)

            # stop if we have gone too far
            for c_path in complete:
                if path.absolute_distance > c_path.absolute_distance: break

            for q_path in queue:
                if nb in q_path:
                    path_to_node = q_path.sub_path(nb)
                    if path.absolute_distance > path_to_node.absolute_distance: continue
                    elif path_to_node > path:
                        queue.pop(queue.index(q-path))

            queue.sort()

