Net_balance = 0.0  #Counter for user amount

#Atm function called after successfull login
def atm(user_name):
    from datetime import datetime
    print(datetime.now(),"\nATM Service! \n\nWelcome",user_name)
    #User input for selection
    Opr = input("Please Type Any Option Provided Below And Press Enter. \n1. Check Account Balance \n2. Deposit \n3. Withdraw \n0. Exit \n")

    #Starts the loop
    while int(Opr) != 0:
        global Net_balance
        if int(Opr) == 1:   #Prints amount in counter
            print ("\nYour Acount Balance = Rs",Net_balance,"\n")

        elif int(Opr) == 2:
            deposit()       #Deposit function is called

        elif int(Opr) == 3:
            withdraw()      #Withdraw function is called

        else:
            print ("Wrong Option!")

        #Incase above condition(s) get meet
        #Loop continues untill input equals '0'
        Opr = input("1. Check Account Balance \n2. Deposit \n3. Withdraw \n0. Exit \n")
    print ("Thanks For Using ATM! \nWe Hope You Are Satisfied With Our Service.\nHave A Nice Day Ahead.")
    return

#Deposit funtion starts when called by atm function
def deposit():
    #User input for deposit amount
    deposit = float(input("Enter Amount In Rupees: ")) #Input is converted to float

    if float(deposit) >= 0: #Check for negetive values
        global Net_balance
        Net_balance += float(deposit)  #Deposit amount is incremented in counter
        return
    else:
        print ("\nPlease Enter Right Amount! \n") #If user inputs negetive amount
        return deposit()

#deposit funtion starts when called by atm function
def withdraw():
    global Net_balance
    #If amount is zero returns to atm function
    if float(Net_balance) <= 0:
        print ("\nWithdrawl Impossible! \nYour Account Balance = Rs",Net_balance,"\nPlease Deposit Amount First!\n")
        return
    #If amount is not zero
    else:
        withdraw = float(input("Enter Amount In Rupees: "))
        #Checks if amount in withdraw is less than amount in counter
        if float(withdraw) <= float(Net_balance):
            if float(withdraw) > 0:
                Net_balance -= float(withdraw)
                return
            else:
                print ("\nPlease Enter Right Amount! \n")
                return withdraw()

        else:
            print ("\nWithdrawl Impossible! \nYour Acount Balance = Rs",Net_balance,"\n")
            return withdraw()
