class Unit_Cell(object):
    index = 0
    def __init__(self):
        self.atoms = []

    def add_atoms(self,type,location):
        self.atoms.append((self.index,type,location))
        self.index += 1

    def clear(self):
        self.atoms = []

    def search_by_index(self,index):
        return self.atoms[index]

    def get_degree_of_freedom(self):
        pass

    def get_maximum_distance(self):
        pass

    def get_num_of_atoms(self):
        return len(self.atoms)
