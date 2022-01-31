import random

class Atm(object):
    def __init__(self, BankName, BankLocation, Admin,):
      
        self.BankName = BankName
        self.BankLocation = BankLocation
        self.Admin = Admin
        print("Bank Name : " + self.BankName    )
        print("Bank location" +  self.BankLocation)
        print("Admin Name : " + self.Admin)
    
    def cashWithdrawl(self):
        print("Withdraw Cash")
    def balanceEnquiry(self):
        print("Enquiry on Balance")
        
Sbi = Atm("State Bank of India", "State Bank of India L B NAGAR HYDERABA", "Kevin")
print(Sbi.__init__(Sbi.BankName, Sbi.BankLocation, Sbi.Admin))

Number=random.randint(100,100000)
name = input("Enter your Name")
cardNo = int(input("Enter your Card N.O " + name))
pinNo = int(input("Enter your Pin N.O " + name))
pay = input(name + "Do you want see and draw your money")
print("You are left with " , Number)


    