from rich import print
from poligono import *
def main():
    p1=Square(20)
    print(f"Um quadrado de lado {p1.side} tem perímetro de {p1.perimeter():.1f} mm2")
    print(f"Um quadrado de lado {p1.side} tem área de {p1.area():.1f} mm2")
    p2=Circle(12)
    print(f"Um círculo de raio {p2.ray} cm tem perímetro de {p2.perimeter():.1f} cm")
    print(f"Um círculo de raio {p2.ray} cm tem área de {p2.area():.1f} cm2")
if __name__ == "__main__":
    main()
