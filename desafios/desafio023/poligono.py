from rich import print,inspect
from abc import ABC,abstractmethod
import math

class Polygon(ABC):
    def __init__(self,nbr_of_sides):
        self.nbr_of_sides=nbr_of_sides
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass



class Square(Polygon):
    def __init__(self,side = 1):
      super().__init__(4)
      self.side=side
    def perimeter(self):
        return 4*self.side
    def area(self):
        return self.side**2


class Circle(Polygon):
    def __init__(self,ray = 1):
        super().__init__(0)
        self.ray=ray
    def perimeter(self):
        return math.pi * (2*self.ray)
    def area(self):
        return math.pi * (((2*self.ray)**2)/4)




def main():
    s=Square(12)
    print(f"Perimetro = {s.perimeter():.1f}")
    print(f"Aréa = {s.area():.1f}")
    c=Circle(20)
    print(f"Perimetro = {c.perimeter():.1f}")
    print(f"Aréa = {c.area():.1f}")
if __name__ == "__main__":
    main()


