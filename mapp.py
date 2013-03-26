import nodes, random

class Map(object):
    def __init__(self, amount_of_nodes, max_x, max_y, list_of_nodes=None):
        if not list_of_nodes:
            self.map = [nodes.Node(random.randint(-max_x, max_x), 
                random.randint(-max_y, max_y)) for i in range(amount_of_nodes)]
        else:
            self.map = list_of_nodes

    def __iter__(self):
        return self.map.__iter__()

    def __repr__(self):
        stri = '<Map (\n'
        for i in self:
            stri += '  '+str(i)+'\n'
        stri += ')>'
        return stri
