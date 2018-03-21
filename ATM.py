import os
net_balance = 0.0  #Counter for user amount

directory = "Data"	#Path for file
name = "usersdata.txt"						#name of file
filename = os.path.join(directory, name)	#joining directory with file for further use

#Atm function called after successfull login
def atm(user_name,Net_balance,Pin):
    from datetime import datetime
    print(datetime.now(),"\nATM Service! \n\nWelcome",user_name)
    #User input for selection
    Opr = input("Please Type Any Option Provided Below And Press Enter. \n1. Check Account Balance \n2. Deposit \n3. Withdraw \n0. Exit \n")

    #Starts the loop
    while int(Opr) != 0:
        global net_balance
        net_balance += Net_balance
        if int(Opr) == 1:   #Prints amount in counter
            print ("\nYour Acount Balance = Rs",net_balance,"\n")

        elif int(Opr) == 2:
            deposit(net_balance)       #Deposit function is called

        elif int(Opr) == 3:
            withdraw(net_balance)      #Withdraw function is called

        else:
            print ("Wrong Option!")

        #Incase above condition(s) get meet
        #Loop continues untill input equals '0'
        Opr = input("1. Check Account Balance \n2. Deposit \n3. Withdraw \n0. Exit \n")
    print ("Thanks For Using ATM! \nWe Hope You Are Satisfied With Our Service.\nHave A Nice Day Ahead.")

    with open(filename,'a+') as ap:
        re_new = "\n"+user_name+":"+str(Pin)+","+str(net_balance)
        ap.write(re_new)
        ap.close()
    return

#Deposit funtion starts when called by atm function
def deposit(Net_balance):
    global net_balance
    #User input for deposit amount
    deposit = float(input("Enter Amount In Rupees: ")) #Input is converted to float

    if float(deposit) >= 0: #Check for negetive values
        net_balance += float(deposit)  #Deposit amount is incremented in counter
        return net_balance
    else:
        print ("\nPlease Enter Right Amount! \n") #If user inputs negetive amount
        return deposit(net_balance)

#deposit funtion starts when called by atm function
def withdraw(Net_balance):
    global net_balance
    #If amount is zero returns to atm function
    if float(net_balance) <= 0.0:
        print ("\nWithdrawl Impossible! \nYour Account Balance = Rs",net_balance,"\nPlease Deposit Amount First!\n")
        return
    #If amount is not zero
    else:
        with_draw = float(input("Enter Amount In Rupees: "))
        #Checks if amount in withdraw is less than amount in counter
        if with_draw <= net_balance:
            if float(with_draw) > 0.0:
                net_balance -= float(with_draw)
                return net_balance
            else:
                print ("\nPlease Enter Right Amount! \n")
                return withdraw(net_balance)

        else:
            print ("\nWithdrawl Impossible! \nYour Acount Balance = Rs",net_balance,"\n")
        return withdraw(net_balance)
