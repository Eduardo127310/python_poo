from rich import print
from rich.traceback import install
install()
import time
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
        self.start=1
        self.controller=1
        print(f":book: [blue]Você acabou de abrir o livro '[red]{self.title}[/]' que tem [green]{self.pages} páginas[/] no total. Você agora está na [/][yellow]página 1[yellow]")
    
    def advance_page(self,amount):
        comparision=self.start+amount
        if comparision <= self.pages:
            self.start=self.start+amount
            for i in range(self.controller,self.start):
                print(f"Pág{i+1} :play_button:",end="  ")
                time.sleep(0.2)
            print(f"[blue]Você avançou {amount} páginas e agora está na[/] [yellow]página {self.start}[/]")
            self.controller = i+1
            
       
        else:
            desconto=comparision - self.pages
            amount=amount-desconto
            self.start=self.start+amount
            for i in range(self.controller,self.start):
                print(f"Pág{i+1} :play_button:",end="  ")
                time.sleep(0.2)
            print(f"[blue]Você avançou {amount} páginas e agora está na[/] [yellow]página {self.start}[/]")
            print(f":closed_book: [red]Você chegou ao final do livro '{self.title}'[/]")




b=Book("10 coisas que aprendi",20) 

b.advance_page(5)
b.advance_page(10)
b.advance_page(100)


b2=Book("viadagem",20) 
b2.advance_page(10)
