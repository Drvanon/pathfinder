import math

class Node(object):
    def __init__(self, x, y, neighbours=None):
        self.x = x
        self.y = y
        if neighbours:
            self.neigbours = neighbours
        else:
            self.neighbours = []

    def add_neighbour(self, neighbour):
        if neighbour is self:
            return
        if not neighbour in self.neighbours:
            self.neighbours.append(neighbour)
        if not self in neighbour.neighbours:
            neighbour.neighbours.append(self)

    def measure_distance(self, node):
        return math.sqrt(pow(self.x - node.x, 2)+ pow(self.y - node.y, 2))

    def __repr__(self):
        stri = '<Node {}, {} connected:\n'.format(self.x, self.y)
        for i in self.neighbours:
            stri += '    {0}, {1}\n'.format(i.x, i.y)
        return stri
