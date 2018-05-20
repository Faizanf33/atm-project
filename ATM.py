#IMPORTS
## USING PYTHON BUILT-IN LIBRARIES
from __future__ import print_function
from getpass import getpass as gp
import os, csv

##USING SOURCE FILES
from encrypt import rot13
from Data import join,data
from send_mail import sendmail
from acc_no_gen import code
#END OF IMPORTS

#Counter for user amount
net_balance = 0.0

# Using input() in python 2 or 3
try:
    # set raw_input as input in python2
    input = raw_input
except:
    pass


#Atm function called after successfull login
def atm(user_name,Net_balance,Pin,History,acc_no,address):
    filename = join()
    clear = ('cls' if os.name == 'nt' else 'clear')
    #input for change of pin
    # new_pin_opt = input("Change Pin : \n1. Yes \n2. No \n")
    # os.system(clear)
    # if (new_pin_opt == '1') or (new_pin_opt.lower().startswith('y')):

    import time,datetime
    print (time.strftime('Date:%d-%b-%Y \nTime:%I:%M %p  Today:%A\n'))
    print ("""
     Y     Y             000            BBBBBB
      Y   Y           00     00         B     B
       Y Y          00         00       B     B
        Y          00           00      BBBBBB
        Y           00         00       B     B
        Y             00     00         B     B
        Y                000            BBBBBB
    """)

    print(("DEAR"),(user_name.upper())+("!"))
    print("WELCOME TO YOB SERVICE \n")
    #User input for selection
    global net_balance
    net_balance += Net_balance
    Opr = input(":: Please Select An Option Provided Below : \n1. Check Account Balance \n2. Check Acount Number \n3. Deposit \n4. Withdraw \n5. Transfer Amount \n6. Last Acive Session \n7. Change Pin  \n8. Change/Verify Mail Address \n0. Exit \n")
    os.system(clear)

    if not Opr.isdigit():
        Opr = 9

    while int(Opr) != 0:

        if int(Opr) == 1:
            os.system(clear)
            print (":: Your Acount Balance = Rs","{:,} ::".format(net_balance),"\n")

        elif int(Opr) == 2:
            os.system(clear)
            print(":: Your Account Number =",acc_no,":: \n")

        #Deposit function is called
        elif int(Opr) == 3:
            os.system(clear)
            deposit(net_balance, address)

        #Withdraw function is called
        elif int(Opr) == 4:
            os.system(clear)
            withdraw(net_balance, address)

        #Amount Transfer function is called
        elif int(Opr) == 5:
            os.system(clear)
            if net_balance < 0.0:
                print (":: Amount Can Not Be Transferred! ::\n:: Your Acount Balance = Rs",balance,"::","\n")

            else:
                account_no = input('Enter 12-Digit Account Number : ')
                if (account_no == acc_no):
                    os.system(clear)
                    print(":: Amount Transfer Not Possible! ::")
                    print(":: Provided Account Number Is Yours! ::\n")
                else:
                    amount = amount_transfer(account_no, net_balance, acc_no, address)
                    net_balance -= float(amount)

        elif int(Opr) == 6:
            os.system(clear)
            print (":: Your Acount Was Previously Logged in on",History,"::","\n")

        #Change Pin function is called
        elif int(Opr) == 7:
            os.system(clear)
            Pin = change_pin(Pin, address)

        elif int(Opr) == 8:
            os.system(clear)
            Mail_address = input(":: Please Enter A Valid Email Address : ")
            conf = code()
            MSG = "Confirming Mail Address.\n\nAccount Number : "+acc_no+"\n\nYour Verification Code Is : '"+conf+"'"

            if Mail_address == address:
                os.system(clear)
                print(":: Your Email Address Is Verified! ::\n:: Want To Change Your Address ?")
                opt = input("1. Yes\n2. No \n")
                os.system(clear)

                if opt.lower().startswith("y") or opt == '1':
                    Mail_address = input(":: Please Enter A New Valid Email Address : ")

                    if Mail_address == address:
                        os.system(clear)
                        print(":: Email Address Already Verified! ::")

                    else:
                        verify = sendmail(Mail_address, MSG, "Confirmation Mail")

                        if (verify == True):
                            os.system(clear)
                            print("Verification Code Has Been Sent To Your Email Address!")
                            user_conf = input("Enter Provided Code : ")
                            if (user_conf.lower() == conf.lower()):
                                address = Mail_address
                                os.system(clear)
                                print("Email Address Verified And Changed Successfully!\n")

                            else:
                                os.system(clear)
                                print("Invalid Code!\nYour Email Could Not Be Verified.\nYou May Try Again Later!\n")

                        else:
                            os.system(clear)
                            print(verify)

                else:
                    print(":: Email Address Unchanged! ::")

            else:
                os.system(clear)
                verify = sendmail(Mail_address, MSG, "Confirmation Mail")

                if (verify == True):
                    os.system(clear)
                    print("Verification Code Has Been Sent To Your Email Address!")
                    user_conf = input("Enter Provided Code : ")
                    if (user_conf.lower() == conf.lower()):
                        address = Mail_address
                        os.system(clear)
                        print("Email Address Verified And Changed Successfully\n")

                    else:
                        os.system(clear)
                        print("Invalid Code!\nYour Email Could Not Be Verified.\nYou May Try Again Later!\n")

                else:
                    os.system(clear)
                    print(verify)

        else:
            os.system(clear)
            print (":: Invalid Selection! ::")

        #Incase above condition(s) get meet
        #Loop continues untill '0' is entered
        Opr = input(":: Please Select An Option Provided Below : \n1. Check Account Balance \n2. Check Acount Number \n3. Deposit \n4. Withdraw \n5. Transfer Amount \n6. Last Acive Session \n7. Change Pin  \n8. Change/Verify Mail Address \n0. Exit \n")
        if not Opr.isdigit():
            Opr = 9
            os.system(clear)

    os.system(clear)
    print ("::: Thanks For Using ATM! :::\n::: We Hope You Are Satisfied With Our Service. :::\n::: Have A Nice Day Ahead. :::")
    print ("About:")
    with open('About.txt','r') as infile:
        show = infile.read()
        print (show)

    with open(filename,'a+') as ap:
        #rot13() function is called for encoding
        enc = rot13(user_name.lower())
        re_new = [acc_no,enc,str(Pin),str(net_balance),time.strftime('%d-%b-%Y at %I:%M %p'),address]
        w = csv.writer(ap)
        w.writerow(re_new)
        ap.close()
    return

#Deposit funtion starts when called by atm function
def deposit(Net_balance, address):
    clear = ('cls' if os.name == 'nt' else 'clear')
    global net_balance
    print(":: Deposit ::")
    try:
        deposit_amount = input("Enter Amount In Rupees: ")

        #Check for negetive values
        if float(deposit_amount) >= 0.0:
            #check for extra large amount
            #limits amount towards power of e
            if (len(deposit_amount) > 14) or ((len(str(float(deposit_amount)+net_balance))) > 14):
                os.system(clear)
                print (':: Amount Limit Exceeded! ::')
                return

            #Deposit amount is incremented in counter
            else:
                net_balance += float(deposit_amount)
                os.system(clear)
                MSG = "You Have Successfully Depositted An Amount Of Rs "+str(deposit_amount)+"\n\nYour Net Account Balance is Rs "+str(net_balance)
                msg = sendmail(address, MSG)
                os.system(clear)
                if not (msg == True): print(msg)
                print(":: You Have Successfully Depositted An Amount Of Rs",deposit_amount,"::",'\n')
                return

        elif float(deposit_amount) < 0.0:
            os.system(clear)
            #If user inputs negetive amount
            print (":: Please Enter Right Amount! ::\n")
            return deposit(net_balance, address)

        else:
            os.system(clear)
            print (":: Please Enter Right Amount! ::\n")
            return deposit(net_balance, address)

    except ValueError:
        os.system(clear)
        print (":: Please Enter Right Amount! ::\n")
        return deposit(net_balance, address)

#deposit funtion starts when called by atm function
def withdraw(Net_balance, address):
    clear = ('cls' if os.name == 'nt' else 'clear')
    global net_balance
    print(":: Withdraw ::")
    #If amount is zero returns to atm function
    if float(net_balance) <= 0.0:
        print (":: Withdrawl Impossible! ::\n:: Your Account Balance = Rs",net_balance,"::","\n:: Please Deposit Amount First! ::\n")
        return

    else:
        try:
            with_draw = input("Enter Amount In Rupees: ")
            os.system(clear)

            #If user inputs negetive amount
            if float(with_draw) < 0.0:
                os.system(clear)
                print (":: Please Enter Right Amount! ::\n")
                return withdraw(net_balance, address)

            #Checks if amount in withdraw is less than amount in counter
            elif float(with_draw) <= net_balance:
                net_balance -= float(with_draw)
                MSG = "You Have Successfully Withdrawn An Amount Of Rs "+str(with_draw)+"\n\nYour Net Account Balance is Rs "+str(net_balance)
                msg = sendmail(address, MSG)
                os.system(clear)
                if not (msg == True): print(msg)
                print(":: You Have Successfully Withdrawn An Amount Of Rs",with_draw,"::",'\n')
                return

            else:
                os.system(clear)
                print (":: Withdrawl Impossible! ::\n:: Your Acount Balance = Rs",net_balance,"::","\n")
            return withdraw(net_balance, address)

        except ValueError:
            os.system(clear)
            print (":: Please Enter Right Amount! ::\n")
            return withdraw(net_balance, address)


def change_pin(Pin, address):
    clear = ('cls' if os.name == 'nt' else 'clear')
    os.system(clear)
    pin_count = 0
    print(":: Create Your Own Pin....::")
    while pin_count != 3:
        print(":: Entries left :",(3-pin_count),"::")
        pin = str(gp ("Enter 4-Digit Pin : "))
        os.system(clear)

        if (len(pin) == 4) and (pin.isdigit() == True):
            if not pin == Pin:
                os.system(clear)
                confirm_pin = str(gp ("Confirm Pin : "))

                if pin == confirm_pin:
                    Pin = pin
                    os.system(clear)
                    MSG = "You Have Successfully Changed Your Pin"
                    msg = sendmail(address, MSG)
                    os.system(clear)
                    if not (msg == True): print(msg)
                    print(':: Pin Changed Successfully! ::\n')
                    return(Pin)

                else:
                    os.system(clear)
                    print(":: Pin Change Unsuccessful! ::")
                    print (":: Your Pin Did Not Match! ::\n")
                    pin_count +=1

            else:
                pin_count += 1
                os.system(clear)
                print(":: Pin Change Unsuccessful! ::")
                print(":: Please Enter A New Pin ::\n")


        else:
            pin_count += 1
            os.system(clear)
            print(":: Pin Change Unsuccessful! ::")
            print(":: Invalid Pin! ::\n")
    return(Pin)

def amount_transfer(account_no, balance, acc_no, address):
    import time,datetime
    clear = ('cls' if os.name == 'nt' else 'clear')
    os.system(clear)

    d = data()
    filename = join()
    amount = 0.0

    print (":: Amount Transfer ::")
    Inactive_account = str('#'+account_no)

    if Inactive_account in d.keys():
        os.system(clear)
        print (":: Provided Account Number Is Not Active! ::")
        return amount

    elif account_no in d.keys():
        try:
            amount = input("Enter Amount In Rupees: ")

            if float(amount) < 0.0 or ('-' in amount):
                os.system(clear)
                print (":: Please Enter Right Amount! ::\n")
                return amount_transfer(account_no, balance, acc_no, address)

            elif float(amount) > float(balance):
                os.system(clear)
                print (":: Amount Can Not Be Transferred! ::\n:: Your Acount Balance = Rs",balance,"::","\n")
                return amount_transfer(account_no, balance, acc_no, address)

            else:
                os.system(clear)
                print(":: Account Number :",account_no,"::")
                print(":: Name :",d[account_no][0],"::")
                print(":: Amount Transfer = Rs","{:,} ::".format(float(amount)),"\n")

                confirm = input("Please Confirm \n1. Yes \n2. No \n")

                if (confirm == '1') or (confirm.lower().startswith('y')):
                        with open(filename,'a+') as ap:
                            #rot13() function is called for encoding
                            enc = rot13(d[account_no][0])
                            current_balance = balance
                            balance = str(float(d[account_no][2]) + float(amount))
                            Message = str("Amount of 'Rs "+str(amount)+"' was received on "+str(time.strftime('%d-%b-%Y at %I:%M %p'))+", through Account Number: "+str(acc_no))
                            re_new = [account_no,enc,d[account_no][1],balance,d[account_no][3],d[account_no][4],Message]
                            w = csv.writer(ap)
                            w.writerow(re_new)
                            ap.close()

                        os.system(clear)
                        MSG_from = "You Have Successfully Transferred An Amount Of Rs "+str(amount)+" To A/C #"+str(account_no)+"\n\nYour Net Account Balance Is Rs "+str(float(current_balance) - float(amount))
                        MSG_to = "You Have Received An Amount Of Rs "+str(amount)+" From A/C #"+str(acc_no)+"\n\nYour Net Account Balance Is Rs "+str(float(balance))
                        sendmail(address, MSG_from)
                        msg2 = sendmail(d[account_no][4], MSG_to)
                        os.system(clear)
                        if not (msg2 == True): print(msg2)
                        print(":: Amount Transferred Successfully! ::")
                        return amount
                else:
                    amount = 0
                    os.system(clear)
                    print(":: Amount Transfer Unsuccessful! ::")
                    return amount

        except ValueError as err:
            os.system(clear)
            print("Error :",err)
            print(":: Please Enter Right Amount! ::\n")
            return amount_transfer(account_no, balance, acc_no, address)
    else:
        os.system(clear)
        print (":: No Match Found! ::")
        return amount
