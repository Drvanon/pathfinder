class Path(object):
    def __init__(self, goal, nodes=None):
        self.nodes = []
        self.total_distance = 0
        self.absolute_distance = 0
        try: # If list is given:
            iter(nodes)
            self.nodes = nodes
        except TypeError: # Else: start with the given node
            if nodes:
                self.start(nodes)
        self.goal = goal
        self.calc_distance()

    def calc_distance(self):
        for i in range(len(self.nodes)-1):
            self.total_distance += self.nodes[i].measure_distance(self.nodes[i+1])
        if self.nodes:
            self.absolute_distance = self.nodes[-1].measure_distance(self.goal)

    def add_node(self, node):
        neighbour_exists = False
        for my_node in self.nodes:
            if node in my_node.neighbours:
                neighbour_exists = True
        assert neighbour_exists

        new_nodes = self.nodes
        new_nodes.append(node)
        path = Path(self.goal, new_nodes)
        return path

    def sub_path(self, node):
        if not node in self:
            raise LookupError('No such node ({}) in this path.'.format(node))
        return Path(self.nodes[:self.nodes.index(node)])

    def start(self, node):
        self.nodes.append(node)

    def __iter__(self):
        return self.nodes.__iter__()

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, key):
        return self.nodes[key]
