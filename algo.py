import path

def find(begin, goal):
    queue = []
    complete = []
    just_started = True

    queue.append(path.Path(goal, begin))

    while True:
        print(queue)
        if len(queue) == 1 and not just_started:
            return queue.pop()
        cur_path = queue.pop()
        node = cur_path[-1]
        new_paths = []
        for nb in node.neighbours:
            # don't go backwards
            if nb in cur_path: continue
            new_path = cur_path.add_node(nb)

            # stop if we have gone too far
            for c_path in complete:
                if new_path.absolute_distance > c_path.absolute_distance: break

            for q_path in queue:
                if nb in q_path:
                    path_to_node = q_path.sub_path(nb)
                    if cur_path.absolute_distance > path_to_node.absolute_distance:
                        continue
                    elif path_to_node > cur_path:
                        queue.pop(queue.index(q_path))

            new_paths.append(new_path)

        sorted_new_paths = sorted(new_paths, key=lambda ppath:ppath.absolute_distance)
        sorted_new_paths.reverse()
        for pathh in sorted_new_paths:
            queue.insert(0, pathh)

        queue =  sorted(queue, key=lambda ppath:ppath.absolute_distance)
        just_started = False

if __name__ == '__main__':
    import random_field, random

    map = random_field.main(100, 20, 20, 10, 10)
    start = random.choice(map)
    dest = random.choice(map)
    while start is dest:
        dest = random.choice(map)

    find(start, dest)
