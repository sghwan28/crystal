class Coordinate(object):

    def __init__(self,x,y,z):
        self.coordinate = (x,y,z)

    def add(self,other):
        self.coordinate = tuple((sum(i) for i in zip(self.coordinate, other.coordinate)))

    def multiple(self,factor):
        self.coordinate = tuple((i*factor for i in self.coordinate))

    def get_coordinate(self):
        return self.coordinate

class Rectiliner():
    def __init__(self,a:Coordinate,b:Coordinate,c:Coordinate):
        self.edge_a = a
        self.edge_b = b
        self.edge_c = c

    def make_vector(self,x,y,z):
        return (x*self.edge_a, y*self.edge_b, z*self.edge_c)

# a = Rectiliner()
# print(a.make_vector(0.5,0.5,0.5))

a = Coordinate(1,1,2)
b = Coordinate(1,2,3)
a.add(b)
a.multiple(2)
print(a.get_coordinate())