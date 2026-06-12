class Gafanhotos:
    '''
    Essa classe cria um gafanhoto,que é uma pessoa que tem nome é idade
    
    Para criar uma nova pessoa,use 
    variavel=Gafanhoto(nome,idade   )
    '''
    def __init__(self,n = "vazio",i = 0): # atributos
        self.nome=n
        self.idade=i

    # Metodos de Istancia
    def aniversario(self): # metodos
        self.idade=self.idade+1
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    def __str__(self):
     return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    def __getstate__(self):
       return f"Estado: nome = {self.nome}  : idade = {self.idade}"
g1=Gafanhotos("Maria",17)
g1.aniversario()
print(g1.mensagem())
g2=Gafanhotos("Mauro",53)
g2.aniversario()
print(g2.mensagem())
g3=Gafanhotos()
print(g3.mensagem())
print(g1.__doc__)
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
g2=Gafanhotos("Mauro",54)
print(g2)
print(g2.__getstate__())
print(g1.__class__)