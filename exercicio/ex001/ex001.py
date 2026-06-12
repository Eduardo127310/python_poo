class Gafanhotos:
    def __init__(self): # atributos
        self.nome=""
        self.idade=0

    # Metodos de Istancia
    def aniversario(self): # metodos
        self.idade=self.idade+1
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

g1=Gafanhotos()
g1.nome="Maria"
g1.idade=17
g1.aniversario()
g1.aniversario()
print(g1.mensagem())
g2=Gafanhotos()
g2.nome="Mauro"
g2.idade=53
g2.aniversario()
g2.aniversario()
g2.aniversario()
g2.aniversario()
g2.aniversario()
g2.aniversario()

print(g2.mensagem())