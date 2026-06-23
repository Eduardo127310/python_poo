from rich import print
from abc import ABC,abstractmethod

class HotDrink(ABC):
    def prepare(self):

        print("[red]--- Iniciando o Preparo ---[/]")
        self.boilWater()
        self.mix()
        self.serve()
        print("[red]--- Bebida Pronta ---[/]\n")

    def boilWater(self):
        print("[white]1. Fervendo água a 100 Celsius[/]")
    @ abstractmethod
    def mix(self):
        pass
    @abstractmethod
    def serve(self):
        pass




class Coffe(HotDrink):
    def mix(self):
        print("[white]2. Passando água pressurizada pelo pó de café moído[white]")
    def serve(self):
        print("[white]3. Servindo em xícara pequena.[white]")

class Tea(HotDrink):

    def mix(self):
        print("[white]2. Mergulhando o sachê ervas de ervas na água.[/]")
    def serve(self):
        print("[white]3. Servindo na caneca de porcelana com limão.[/]")

class Milk(HotDrink):
    def mix(self):
        print("[white]2. Passando água pressurizada pelo bico do leite.[/]")
    def serve(self):
        print("[white]3. [white]Servindo na caneca grande, já com café.[/]")


def main():
    c=Coffe()
    c.prepare()
    t=Tea()
    t.prepare()
    m=Milk()
    m.prepare()


if __name__ == "__main__":
    main()