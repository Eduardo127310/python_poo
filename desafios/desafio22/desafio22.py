from rich import print
from rich.panel import Panel

class RemotControl:
    def  __init__(self):
        self.channel=1
        self.volume=1
        self.on_of=False
        self.command=None
    
    def inputIuser(self,command):
        self.command=command
   
    def simulate(self): # mostar 
        formatting={
           1:f"[on dark_green]{1*" "}[/][on gray30]{4*" "}[/]",
           2:f"[on dark_green]{2*" "}[/][on gray30]{3*" "}[/]",
           3:f"[on dark_green]{3*" "}[/][on gray30]{2*" "}[/]",
           4:f"[on dark_green]{4*" "}[/][on gray30]{1*" "}[/]",
           5:f"[on dark_green]{5*" "}[/]"}
        formatting2={1:f"[on gold3] 1 [/] 2 3 4 5",
             2:f"1 [on gold3] 2 [/] 3 4 5",
             3:f"1 2 [on gold3] 3 [/] 4 5",
             4:f"1 2 3 [on gold3] 4 [/] 5",
             5:f"1 2 3 4 [on gold3] 5 [/]"}
        
        if self.on_of == False:
            box=Panel(":no_entry_sign: [red]A TV está desligada[/]",title="[ TV ]",width=30)
            print(box)
        if self.on_of == True:
            box=Panel(f"CANAL  = {formatting2[self.channel]}\nVOLUME = {formatting[self.volume]}",title="[ TV ]",width=35)
            print(box)
    def changeChannel(self):
        if self.command == ">" and self.channel < 5:
            self.channel=self.channel+1
        else:
            self.channel = 1
    def changeVolume (self):
        if self.command == "+" and self.volume < 5:
            self.volume = self.volume + 1
        if self.command == "-" and self.volume > 1:
            self.volume=self.volume-1
    def turnOnOFF(self):
        if self.on_of == False and self.command == "@":
            self.on_of=True
        elif self.on_of == True and self.command == "@":
            self.on_of=False
       
        


  

            
   
r=RemotControl()
while True:
    v=input(f"< CH{r.channel} >  - VOL{r.volume} + ")
    r.inputIuser(v)
    r.turnOnOFF()
    r.changeChannel()
    r.changeVolume()
    r.simulate()
    if v == "0":
        break



