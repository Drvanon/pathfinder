class Path(object):
    def __init__(self, goal, nodes=None):
        self.nodes = []
        try: # If list is given:
            iter(nodes)
            self.nodes = Nodes
        except TypeError: # Else: start with the given node
            if nodes:
                self.start(nodes)
        self.total_distance = 0
        self.calc_distance()
        self.goal = goal

    def calc_distance(self):
        for i in range(len(self.nodes)):
            self.total_distance += self.nodes[i].measure_distance(self.nodes[i+1])
        self.absolute_distance = self.nodes[-1].measure_distance(goal)

    def add_node(self, node):
        new_nodes = self.nodes
        new_nodes.append(node)
        path = Path(new_nodes)
        return path

    def sub_path(self, node):
        if not node in path:
            raise LookupError('No such node ({}) in this path.'.format(node))
        return Path(self.nodes[:self.nodes.index(node)])

    def start(self, node):
        self.nodes.append(node)
        self.calc_distance()

    def __iter__(self):
        return self.nodes.__iter__()
