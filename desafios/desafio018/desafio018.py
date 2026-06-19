from rich import print
from rich.panel import Panel
class Barbecue:
    price = 82.40
    consumpation=0.4
    def __init__(self,title,people):
        self.title=title
        self.people=people
    def  to_Analyzy(self):
        quantity_of_meeat=Barbecue.consumpation*self.people
        total_cost=Barbecue.price * self.people  * Barbecue.consumpation
        per_person=total_cost / self.people
        return Panel(f"Analisando [green]{self.title}[/] com [blue]{self.people} convidados[/]\nRecomendo [blue]comprar {quantity_of_meeat:.3f}Kg[/] de carne\nO custo total será de [green]R${total_cost:.2f}[/]\nCada pessoa pagará [yellow]R${per_person:.2f}[/] para participar",title=self.title,width=60)
 

b1=Barbecue("Churass dos amigos",15)
print(b1.to_Analyzy())

