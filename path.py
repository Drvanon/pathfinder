class Path(object):
    def __init__(self, goal, nodes=None):
        self.nodes = []
        if nodes:
            self.nodes = Nodes
        self.total_distance = 0
        for i in range(len(self.nodes)):
            self.total_distance += self.nodes[i].measure_distance(self.nodes[i+1])
        self.absolute_distance = self.nodes[-1].measure_distance(goal)

    def add_node(node):
        new_nodes = self.nodes
        new_nodes.append(node)
        path = Path(new_nodes)
        return path

    def sub_path(node):
        if not node in path:
            return False
        path = []
        for i in self:
            if i != node:
                path.append(node)
            else:
                return path

    def __iter__(self):
        return self.nodes.__iter__()
