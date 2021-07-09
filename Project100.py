def selectScreen():
    print("click 1 for Make Transaction ")
    print("click 2 for Too see Bank Balance ")
    v=int (input('select the number'))

    if (v==1):
        screen1()
    elif(v==2):
        screen2()
   


def screen1():
    print("you are in the transaction Screen")
    f=input("enter Your account number")
    i=input("enter the transfer account number")
    g=input("enter the IFC Code")
    h=input("enter the amount")
    
    
def screen2():
    print("you are in the balance Screen  ")
    a=input("Enter your ATM Card number  ")
    b=input("Enter Name (on the card)  ")
    c=input("Enter Regester Number ")
    print(b +"  your balance is 250 ₹")



selectScreen()