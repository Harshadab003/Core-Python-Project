from accmngt import Accountmanagement
from account import Account

if(__name__ == "__main__"):
    choice = 0
    while(choice!=7):
        print("\t\t1.Create Account")
        print("\t\t2.Login")
        print("\t\t3.Check balance")
        print("\t\t4.Deposit")
        print("\t\t5.Withdraw")
        print("\t\t6.Transfer")
        print("\t\t7.Exit")
        
        choice = int(input("Enter your choice"))
        if(choice == 1):
            accno = int(input("Enter your Account number"))
            name = input("Enter your name")
            balance = int(input("Enter the balance"))
            id = input("Enter your Id")
            password = input("Enter your password")
            a = Account(accno,name,balance,id,password)
            Accountmanagement.createAccount(a)

        elif(choice == 2):
            id = input("Enter your Id")
            password = int(input("Enter your password"))
            Accountmanagement.login(id,password)

        
        elif(choice == 3):
            accno = int(input("Enter your Account number"))
            Accountmanagement.viewBalance (accno)

        elif(choice == 4):
            accno = int(input("Enter your Account Number"))
            Accountmanagement.deposit(accno)
        
        elif(choice == 5):
            accno = int(input("Enter your Account Number"))
            Accountmanagement.withdraw(accno)
        
        elif(choice == 6):
            accno1 = int(input("Enter your account number"))
            accno2 = int(input("Enter the account you want to transact money"))
            Accountmanagement.transfer(accno1,accno2)
        
        elif(choice == 7): 
            print("--------------End of Program----------------")