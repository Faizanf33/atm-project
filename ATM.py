from __future__ import print_function
import os
from encrypt import rot13
from Data import join

net_balance = 0.0  #Counter for user amount


# Using input() in python 2 or 3
try:
    # set raw_input as input in python2
    input = raw_input
except:
    pass


#Atm function called after successfull login
def atm(user_name,Net_balance,Pin):
    filename = join()
    import time,datetime
    print (time.strftime('Date:%d-%b-%Y \nTime:%I:%M %p  Today:%A\n'))
    print(("Dear"),user_name+("!"))
    print (("Welcome to YOB Service"),('\n'))
    #User input for selection
    global net_balance
    net_balance += Net_balance
    Opr = input("Please Select An Option Provided Below : \n1. Check Account Balance \n2. Deposit \n3. Withdraw \n0. Exit \n")    #Starts the loop
    os.system('cls' if os.name == 'nt' else 'clear')
    if not Opr.isdigit():
        return atm(user_name,Net_balance,Pin)
    while float(Opr) != 0.0:

        if float(Opr) == 1.0:   #Prints amount in counter
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Your Acount Balance = Rs",net_balance,"\n")

        elif float(Opr) == 2.0:
            os.system('cls' if os.name == 'nt' else 'clear')
            deposit(net_balance)       #Deposit function is called

        elif float(Opr) == 3.0:
            os.system('cls' if os.name == 'nt' else 'clear')
            withdraw(net_balance)      #Withdraw function is called

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Wrong Option!")

        #Incase above condition(s) get meet
        #Loop continues untill input equals '0'
        Opr = input("1. Check Account Balance \n2. Deposit \n3. Withdraw \n0. Exit \n")
        if not Opr.isdigit():
            Opr = 4
            os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Thanks For Using ATM! \nWe Hope You Are Satisfied With Our Service.\nHave A Nice Day Ahead.")

    with open(filename,'a+') as ap:
        #rot13() function is called for encoding
        enc = rot13(user_name)
        re_new = "\n"+enc+":"+str(Pin)+","+str(net_balance)
        ap.write(re_new)
        ap.close()
    return

#Deposit funtion starts when called by atm function
def deposit(Net_balance):
    global net_balance
    try:
        deposit_amount = input("Enter Amount In Rupees: ")

        if float(deposit_amount) >= 0: #Check for negetive values
            net_balance += float(deposit_amount)  #Deposit amount is incremented in counter
            print("You Have Successfully Depositted An Amount Of Rs",deposit_amount,'\n')
            return

        elif float(deposit_amount) < 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Please Enter Right Amount! \n") #If user inputs negetive amount
            return deposit(net_balance)

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Please Enter Right Amount! \n")
            return deposit(net_balance)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Please Enter Right Amount! \n")
        return
#deposit funtion starts when called by atm function
def withdraw(Net_balance):
    global net_balance
    #If amount is zero returns to atm function

    if float(net_balance) <= 0.0:
        print ("Withdrawl Impossible! \nYour Account Balance = Rs",net_balance,"\nPlease Deposit Amount First!\n")
        return
    #If amount is not zero
    else:
        try:
            with_draw = input("Enter Amount In Rupees: ")
            os.system('cls' if os.name == 'nt' else 'clear')

            #If user inputs negetive amount
            if float(with_draw) < 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("Please Enter Right Amount! \n")
                return withdraw(net_balance)

            #Checks if amount in withdraw is less than amount in counter
            elif float(with_draw) <= net_balance:
                net_balance -= float(with_draw)
                print("You Have Successfully Withdrawn An Amount Of Rs",with_draw,'\n')
                return

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("Withdrawl Impossible! \nYour Acount Balance = Rs",net_balance,"\n")
            return withdraw(net_balance)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Please Enter Right Amount! \n")
            return
