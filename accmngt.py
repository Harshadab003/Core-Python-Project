from account import Account
import os
class Accountmanagement:
    def createAccount(a):
        with open("accountdata.txt","a") as fp:
            fp.write(str(a))
            fp.write("\n")
    
    def login(id,password):
        if(os.path.exists("accountdata.txt")): 
            with open("accountdata.txt","r") as fp:
                allAccount = []
                found = True
                for account in fp:
                    account = account.split(",")
                    if account[3] == id and int(account[4]) == password :
                        print("Login Sucessful")
                        break
                else:
                    print("inavalid credentials")                             

    def viewBalance(accno):
        if(os.path.exists("accountdata.txt")): 
            with open("accountdata.txt","r") as fp:
                allAccount = []
                found = False
                for account in fp:
                    account = account.split(",")
                    #print(account)
                    if(int(account[0]) == accno):
                        print("Balance =",account[2])
                        break
                else:
                    print("Account not present")
    def deposit(accno):
        if(os.path.exists("accountdata.txt")):
            with open("accountdata.txt","r") as fp:
                allAccount = []
                found = False
                for account in fp:
                    try:
                        account.index(str(accno),0,2)
                    except:
                        pass
                    else:
                        found = True 
                        account = account.split(",") 
                        account[2] = float(account[2])
                        amount = float(input("Enter the amount you want to deposit"))
                        account[2] = account[2] + amount
                        account[2] = str(account[2])
                        account = ",".join(account)
                    finally:
                        allAccount.append(account)         
            if(found):
                with open("accountData.txt","w") as fp:
                    for account in allAccount:
                        fp.write(account)
            else:
                print("Record not found")
        else:
            print("File is not present")

    def withdraw(accno):
            if(os.path.exists("accountdata.txt")):
                with open("accountdata.txt","r") as fp:
                    allAccount = []
                    found = False
                    for account in fp:
                        try:
                            account.index(str(accno),0,2)
                            amount = float(input("Enter the amount you want to withdraw"))
                            found = True
                        except:
                            pass
                        else:
                                account = account.split(",") 
                                if (float(account[2])-amount)>0:
                                    account[2] = float(account[2]) - amount
                                    account[2] = str(account[2])
                                    account = ",".join(account)
                                else:
                                    print("Balance is insufficent")
                                    account = ",".join(account)
                        
                        finally:
                                allAccount.append(account)         
                if(found):
                    with open("accountData.txt","w") as fp:
                        for account in allAccount:
                            fp.write(account) 
                else:
                    print("Record not found")
            else:
                print("File is not present")
    
    def transfer(accno1 , accno2 ):
        if(os.path.exists("accountdata.txt")):
            with open('accountdata.txt','r') as fp:
                allAccount =[]
                found = False
                for account in fp:
                    try:
                        account.index(str(accno1) , 0 , 4)
                    except:
                        pass
                    else:
                        found = True
                        account = account.split(",")
                        balance = float(account[2])
                        transaction = float(input(" Enter Transaction amount : "))

                        if(balance > transaction):
                            total = balance - transaction
                            account[2] = total
                            account[2] = str(account[2])+"\n"
                            account = ",".join(account)
                            print("Now your account balance is :", total)
                        else:
                            print("You don't Have enough money for transactions!!")
                            print("Try transactions with less money than",balance)
                            account = ",".join(account)
                    finally:
                        allAccount.append(account)
            if(found):
                with open("accountdata.txt", "r+") as fp:
                    for account in allAccount:
                        fp.write(account)
            else:
                print("Record Not Found")

        if(os.path.exists("accountdata.txt")):
            with open('accountdata.txt','r') as fp:
                allAccount =[]
                found = False        
                for account in fp:
                    try:
                        account.index(str(accno2) , 0 , 4)
                    except:
                        pass
                    else:
                        found = True
                        account = account.split(",")
                        balance = float(account[2])
                        total = balance + transaction
                        account[2] = total
                        account[2] = str(account[2])
                        
                        account = ",".join(account)  
                        with open ("transactions.txt","a") as fp:
                            details = str(accno1)+","+str(accno2)+","+str(transaction)+","+"\n"    
                            fp.write(details)

                    finally:
                        allAccount.append(account)
            if(found):
                with open("accountdata.txt", "r+") as fp:
                    for account in allAccount:
                            fp.write(account)
            else:
                print("Record Not Found")
        else:
            print("File Is Not Present!!")