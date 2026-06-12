class  BankAccount:
  '''
  Creating a bank account allows you criar make withdrawals and deposits
  '''
  def __init__ (self,id,name,balance = 0):
    self.id =id
    self.holder=name
    self.balance=balance
    print(f"Account {self.id} created succesfully.Current balance of ${self.balance:.2f}")
          
  def __str__(self):
   return f"The account {self.id} of {self.holder} has a balance of R${self.balance:.2f}"
  def deposit(self,value):
    self.balance=self.balance+value
    print(f"Deposit of ${value} authorized in account {self.id}")
  def withdraw(self,value):
    if value >  self.balance:
        print(f"Withdrawal denied of ${value:.2f} froom account {self.id}: INSUFFICIENT FUNDS.")
    else:
        self.balance=self.balance-value 



a1=BankAccount(122,"Gustavo",3000)
a1.deposit(500)
a1.withdraw(2000000000000)
print(a1)

