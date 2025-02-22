class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance=self.balance+dep_amt
        print(f"added {dep_amt} to the balance")
    def withdrawal(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance=self.balance-wd_amt
            print("with drawal accepted")
        else:
            print("sorry not enough balance")
    def __str__(self):
        return f"owner:{self.owner} \nbalance:{self.balance}"
a=Account('nani',500)
a.owner
a.balance
a.deposit(100)
a.withdrawal(300)
print(a)

        
            
    
        
        