from rich import print
from rich.panel import Panel
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show_label(self):
        center=f"{self.name.center(30," ")}"
        center=center+f"{30*"."}" 
        price_format=f"{self.price:.2f}"
        center=center+price_format.center(32,".")

        box=Panel(f"{center}",title="Produto",width=35)
        return box

p1=Product("iPhone 17 Pro Max",2580085)
p2=Product("Nootebook Gamer",8000)
print(p1.show_label())
print(p2.show_label())