#!/usr/bin/env python3
import path


class Pathfinder(object):
    def __init__(self, node_map, begin, goal):
        self.node_map = node_map
        self.queue = []
        self.complete = None

        self.begin = begin
        self.goal = goal

        self.solution = None
        self.first_run = True

        self.queue.append(path.Path(self.goal, self.begin))

    def save_self(self):
        # Do not know why I have to do this, but so be it
        if not self.queue: # If queue is empty but no ways where found, try again
            self.queue.append(path.Path(self.goal, [self.begin]))


    def print(self):
        if self.complete:
            print("len queue: " + str(len(self.queue)) + "\n" + \
                    "found solution? yes")
        else:
            print("len queue: " + str(len(self.queue)) + "\n" + \
                    "found solution? no")
        print("-------------------------------------")


    def step(self):
        self.print()
        if not self.first_run and self.complete:
            return True
        elif self.first_run:
            self.first_run = False

        self.save_self()

        path = self.queue.pop()
        node = path[-1]
        new_paths = []
        for nb in node.neighbours:
            # Don't go backwards
            if nb in path:
                continue
            new_path = path.add_node(nb)
            add_nb = True

            if nb is self.goal:
                print('goal reached')
                if self.complete:
                    if new_path.total_distance > self.complete.total_distance:
                        break
                self.complete = new_path
                break

            # Stop if we have gone too far
            if self.complete:
                if self.complete.total_distance < new_path.total_distance:
                    add_nb = False

            for q_path in self.queue:
                if nb in q_path:
                    q_path_to_nb = q_path.sub_path(nb)
                    # If the other way to this nb is shorter, pick that.
                    if path.total_distance > q_path_to_nb.total_distance:
                        add_nb = False
                    # Otherwise, remove that path from the queue.
                    else:
                        self.queue.pop(self.queue.index(q_path))

            if add_nb:
                new_paths.append(new_path)

        self.queue.extend(new_paths)
        if not new_paths:
            print('No new path could be found')
            self.queue.pop(0)
            return True

        # Sort queue by absolute distance
        self.queue.sort(key=lambda path: path.absolute_distance + path.total_distance)

        return None

    def run(self):
        while True:
            s = self.step()
            if s:
                return self.complete


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
    print('\n\n\n\n\n\n\n\n\n\n')
    print('nodes: '+ str(len(path.nodes)))
    print('distance: ' + str(start.measure_distance(dest)))
