#!/usr/bin/env python3
import path


class Pathfinder(object):
    def __init__(self, node_map, begin, goal):
        self.node_map = node_map
        self.queue = []
        self.complete = []

        self.begin = begin
        self.goal = goal

        self.solution = None
        self.first_run = True

        self.queue.append(path.Path(self.goal, self.begin))

    def step(self):
        if len(self.queue) == 1 and not self.first_run:
            self.solution = self.queue.pop()
            return self.solution
        elif self.first_run:
            self.first_run = False

        path = self.queue.pop()
        node = path[-1]
        new_paths = []
        for nb in node.neighbours:
            # Don't go backwards
            if nb in path:
                continue
            new_path = path.add_node(nb)
            add_nb = True

            # Stop if we have gone too far
            for c_path in self.complete:
                if new_path.total_distance > c_path.total_distance:
                    add_nb = False

            for q_path in self.queue:
                if nb in q_path:
                    q_path_to_nb = q_path.sub_path(nb)
                    # If the other way to this nb is shorter, pick that.
                    if path.total_distance > q_path_to_nb.total_distance:
                        add_nb = False
                    # Otherwise, remove that path from the queue.
                    elif q_path_to_nb.total_distance > path.total_distance:
                        self.queue.pop(self.queue.index(q_path))

            if add_nb:
                new_paths.append(new_path)

        self.queue.extend(new_paths)

        # Sort queue by absolute distance
        self.queue.sort(key=lambda path: path.absolute_distance)
        return None

    def run(self):
        while True:
            s = self.step()
            if s is not None:
                return s


if __name__ == '__main__':
    import random
    import random_field

    node_map = random_field.main(100, 20, 20, 10, 10)
    start = random.choice(node_map)
    dest = random.choice(node_map)
    while start is dest:
        dest = random.choice(node_map)

    pf = Pathfinder(node_map, start, dest)
    path = pf.run()
    print(path)
