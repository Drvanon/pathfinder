queue = []
complete = []

while True:
    path = queue.pop()
    node = path[-1]
    for nb in node.neighbours:
        # don't go backwards
        if nb in path: continue
        new_path = path.add_node(nb)

        # stop if we have gone too far
        for c_path in complete:
            if path > c_path: break # TODO path.length, is already a iterable rl(9)

        for q_path in queue:
            if nb in q_path:
                path_to_node = q_path.sub_path(nb)
                if path > path_to_node: continue # TODO same as rl(14)
                elif path_to_node > path:
                    queue.pop(queue.index(q-path))

        queue.sort()

