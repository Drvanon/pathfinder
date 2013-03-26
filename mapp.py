import nodes, random

class Map(object):
    def __init__(self, amount_of_nodes, max_x, max_y, list_of_nodes=None):
        if not list_of_nodes:
            self.map = [nodes.Node(random.randint(0, max_x),
                random.randint(0, max_y)) for i in range(amount_of_nodes)]
        else:
            self.map = list_of_nodes

    def __iter__(self):
        return self.map.__iter__()

    def __repr__(self):
        stri = '<Map (\n'
        for i in self:
            stri += '  ' + i.long_repr() + '\n'
        stri += ')>'
        return stri

    def __getitem__(self, key):
        return self.map[key]

    def __len__(self):
        return len(self.map)
