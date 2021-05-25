class Coordinate(object):

    def __init__(self, x, y, z, atom=None):
        self.atom = atom
        self.cx = x
        self.cy = y
        self.cz = z
        self.vector = [x,y,z]

    def add(self, other):
        self.cx += other.cx
        self.cy += other.cy
        self.cz += other.cz

    def multiply(self, factor):
        self.cx *= factor
        self.cy *= factor
        self.cz *= factor

    def __getitem__(self, item):
        return self.vector[item]

    def dot(self, other):
        return (self.cx * other.cx) + (self.cy * other.cy) + (self.cz * other.cz)

    def __add__(self, other):  # 这个有必要吗？
        return Coordinate(self.cx + other.cx, self.cy + other.cy, self.cz + other.cz)

    def __mul__(self, other):  # refers to cross product  叉乘，返回一个新向量
        c = [self[1] * other[2] - self[2] * other[1],
             self[2] * other[0] - self[0] * other[2],
             self[0] * other[1] - self[1] * other[0]]
        return c

    def __eq__(self, other):
        return self.get_coordinate() == other.get_coordinate()

    def get_coordinate(self):
        return self.cx, self.cy, self.cz   # return a tuple

t = Coordinate(1,2,3)
t2 = Coordinate(0,1,2)
t3 = t*t2
print(t3)

# class Element(object):
#
#     def __init__(self, element: str):
#         self.element = element


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

    def get_max_distance(self):
        pass

    def get_edges(self):
        pass
