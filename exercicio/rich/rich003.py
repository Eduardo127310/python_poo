from rich import  print
from rich.table import Table

table =Table(title="tabela de pressos",style="purple")
table.add_column("Nome",justify="right",style="red")
table.add_column("Preço",justify="center",style="blue")
table.add_row("Lapis","R$1.50")
table.add_row("Borracha","R$ 5,00")
print(table)