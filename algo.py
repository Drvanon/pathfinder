import path

def find(begin, goal):
    queue = []
    complete = []

    queue.append(path.Path(goal, begin))

    while True:
        cur_path = queue.pop()
        node = cur_path[-1]
        for nb in node.neighbours:
            # don't go backwards
            if nb in cur_path: continue
            new_path = cur_path.add_node(nb)

            # stop if we have gone too far
            for c_path in complete:
                if cur_path.absolute_distance > c_path.absolute_distance: break

            for q_path in queue:
                if nb in q_path:
                    path_to_node = q_path.sub_path(nb)
                    if cur_path.absolute_distance > path_to_node.absolute_distance: continue
                    elif path_to_node > cur_path:
                        queue.pop(queue.index(q_path))

            queue.sort()

if __name__ == '__main__':
    import random_field, random

    map = random_field.main(100, 20, 20, 10, 10)
    start = random.choice(map)
    dest = random.choice(map)
    while start is dest:
        dest = random.choice(map)

    find(start, dest)
