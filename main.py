class Element(object):

    def __init__(self, element: str):
        self.element = element
        print(self.element)


class Atom(Element):

    def __init__(self,element):
        super().__init__(element)
        self.y = 1
        print(self.y)


c = Element('C')
c1 = Atom('O')
