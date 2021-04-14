class Coordinate(object):

    def __init__(self, x, y, z):
        self.cx = x
        self.cy = y
        self.cz = z

    def add(self, other):
        self.cx += other.cx
        self.cy += other.cy
        self.cz += other.cz

    def multiply(self, factor):
        self.cx *= factor
        self.cy *= factor
        self.cz *= factor

    def dot(self,other):
        return (self.cx * other.cx) + (self.cy * other.cy) + (self.cz * other.cz)

    def __add__(self, other):
        return Coordinate(self.cx + other.cx, self.cy + other.cy, self.cz + other.cz)

    def __mul__(self, other):  # refers to cross product
        # place holder here
        pass

    def __eq__(self, other):
        return self.get_coordinate() == other.get_coordinate()

    def get_coordinate(self):
        return self.cx, self.cy, self.cz   # return a tuple


class UnitCell(object):
    def __init__(self):
        self.atom_number = 0
        self.atom_list = dict()

    def add_atom(self):
        pass

    def get_atom_list(self):
        pass

    def get_atom_numbers(self):
        return self.atom_number

    def __iter__(self):
        pass

    def __str__(self):
        pass