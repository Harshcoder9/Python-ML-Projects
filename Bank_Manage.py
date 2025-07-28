import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an exception occurred as {err}")
        
    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
    
    def createaccount(self):
        info = {
            "name": input("Tell your name :-"),
            "age": int(input("Tell your age :-")),
            "email": input("Tell your email :-"),
            'pin': int(input("Tell your 4 number pin :-")),
            'accountNo.': Bank.__accountgenerate(),
            'balance': 0
        }
        
        if info['age'] < 18 or len(str(info['pin'])) !=4:
            print("Sorry you cant create your account")
        else:
            print("Your account has been created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please note down your account no. properly")    
            Bank.data.append(info)
            Bank.__update()
            
    def depositmoney(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Please tell your pin aswell :-"))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Sorry no data found for consumer")
            
        else:
             amount = int(input("How much you want to deposit :-"))
             if amount > 100000 or amount <0:
                 print("Sorry the amount is too much you can deposit below 1L or above 0")       
             else:
                
                 userdata[0]['balance'] += amount
                 Bank.__update()
                 print("Amount has been deposited successfully!💕")
                 
    def withdrawmoney(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Please tell your pin aswell :-"))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Sorry no data found for consumer")
            
        else:
            amount = int(input("How much you want to withdraw :-"))
            if userdata[0]['balance'] < amount:
                 print("Sorry you dont have enough balance to withdraw 😮")
            else:
                print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully 👌")
                
    def showdetails(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Please tell your pin :-"))
        
        userdata= [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your info. is:- \n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")
            
    def update_details(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Please tell your pin :-"))
        
        userdata= [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata==False:
            print("no such user found")
        else:
            print("you cant change age, account number, balance")
            print("Fill details for change or leave it empty if no change")
            
            newdata={
                'name': input("please tell new name or press enter to skip:"),
                'email':input("please tell your email  or press enter to skip: "),
                'pin': input("please tell your pin or press enter to skip:")
            }
            
            if newdata['name']=="":
                newdata['name']=userdata[0]['name']
            if newdata['email']=="":
                newdata['email']=userdata[0]['email']
            if newdata['pin']=="":
                newdata['pin']=userdata[0]['pin']
                
            newdata['age']=userdata[0]['age']
            newdata['accountNo.']=userdata[0]['accountNo.']
            newdata['balance']=userdata[0]['balance']    
             
            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])
                
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print("Consumer details have been updated successfully enjoy our banking system 💕")  
            
    def Delete_acc(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Please tell your pin :-"))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No such user found")
        else:
            Bank.data.remove(userdata[0])
            Bank.__update()
            print("Account deleted successfully!")


user = Bank()
print("press 1 for creating account")
print("press 2 for Depositing money in bank")
print("press 3 for withdrawing money from bank")
print("press 4 for details of account")
print("press 5 for updating details of account")
print("press 6 for deleting account")

check = int(input("Tell your response :-"))

if check==1:
    user.createaccount()
    
if check==2:
    user.depositmoney()
    
if check==3:
    user.withdrawmoney()
    
if check==4:
    user.showdetails()
    
if check==5:
    user.update_details()
    
if check==6:
    user.Delete_acc()