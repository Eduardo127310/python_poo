from rich import print,inspect
from abc import ABC,abstractmethod
class Polygon(ABC):
    def __init__(self,nbr_of_sides):
        self.nbr_of_sides=nbr_of_sides
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def circle(self):
        pass



class Square(Polygon):
    def __init__(self,nbr_of_sides,side):
      super().__init__(nbr_of_sides)
      self.side=side
    def perimeter(self):
        pass
    def circle(self):
        pass


class Circle(Polygon):
    def __init__(self,nbr_of_sides,ray):
        super().__init__(nbr_of_sides)
        self.ray=ray
    def perimeter(self):
        pass
    def circle(self):
        pass   




