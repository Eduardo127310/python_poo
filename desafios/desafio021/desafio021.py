from rich import print
class Pen:
    colors={"vermelho":"red","azul":"blue","verde":"green"}
    def __init__(self,color):
        self.color=color.lower().strip()
        self.true=False
    
    def uncork(self):
        self.true=True
    
    def to_write(self,phrase):
        if self.color in Pen.colors:
            if self.true == True:
                print(f"[{self.colors[self.color]}]{phrase}[/]",end="")
            else:
                print(f":no_entry_sign: A caneta está tampada!")
           
    def break_line(self,number):
        print(number * "\n")
    
    def cover(self):
        self.true=False

    

p1=Pen("azul")
p2=Pen("vermelho")
p3=Pen("verde")
p1.uncork()
p3.uncork()
p2.uncork()
p3.uncork()
p1.to_write("Olá, tudo bem? ")
p1.break_line(2)
p2.to_write("Olá, Gafanhoto! ")
p3.to_write("vamos exercitar! ")
