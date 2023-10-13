class Account:
    def __init__(self,accno,name,balance,id,password):
        self.accno = accno
        self.name = name
        self.balance = balance
        self.id = id
        self.password = password

    def __str__(self):
        return str(self.accno)+","+ self.name+","+str(self.balance)+","+self.id+","+self.password


