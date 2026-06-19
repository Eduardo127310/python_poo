from rich import print
from rich.panel import Panel
from rich.traceback import install
install()
class Gamer:
    def __init__(self,name,nick):
        self.name=name
        self.nick=nick
        self.dataBase=set()
    def record(self):
        concatenate=""
        display=list(self.dataBase)
        for i in display:
            concatenate = concatenate + f":video_game: [blue]{i}[/]\n"
        format_name=f"[dark_black]{self.name}[/]"
        box=Panel(f"Nome real: [black on white]{format_name}[/]\nJogos favoritos:\n{concatenate}",title=f"jogador <{self.nick}>",width=38)
        print(box)
            
    def add_favorites(self,game):
        self.dataBase.add(game)
        



j1=Gamer("Fabricio da Silva","detonator2025")
j1.add_favorites("Fortnit")
j1.add_favorites("God of War")
j1.add_favorites("Mario Bros")
j1.add_favorites("Sonic")
j1.record()

j2=Gamer("Olivia Souza","peach_raivosa")
j2.add_favorites("Mario Bros")
j2.add_favorites("Call of Duty")
j2.record()
