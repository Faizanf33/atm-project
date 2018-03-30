from __future__ import print_function
from ATM import atm
from encrypt import rot13  							#Imports atm function from ATM.py file
from Data import data,join
import os
import sys
import re


# Using input() in python 2 or 3
try:
    # set raw_input as input in python2
    input = raw_input
except:
    pass

#main funtion which calls further funtions,execution starts from here
def login_user():
    #data funtion is called to check or make changes in it
    d = data()

    user = input("Select One : \n1. Login \n2. Create New Account \n3. Delete Existing Account \n0. Exit \n")
    os.system('cls' if os.name == 'nt' else 'clear')

    if not str(user).isdigit():
        print ("Invalid Selection!")
        return login_user()

    #login function called for further execution
    if int(user) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        login(d)

    #new_account function called for further execution
    elif int(user) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        new_account()

    elif int(user) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        del_account()

    elif int(user) == 0:                        #exits the main funtion
        print ("Good Bye!")

    else:
        print ("Invalid Selection!")
        return login_user()						#in case any other number is entered except those listed above
												#recursion(main function called again)
    return


def login(d):
    import time,datetime
    os.system('cls' if os.name == 'nt' else 'clear')
    user_name = input("Login\nEnter Full Name : ")
    entry = 0
    if (d == None):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Please create an account first!")
        return login_user()

    #admin block
    elif (user_name in d.keys()) and (user_name.lower() == 'admin access'):
        pin = str(input("Enter 4-Digit Pin : "))

        if pin == d[user_name][0]:
            del d[user_name],d['abc xyz']
            os.system('cls' if os.name == 'nt' else 'clear')
            print (time.strftime('Date:%d-%b-%Y \nTime:%I:%M %p  Today:%A\n'))
            print ("Welcome to YOB Admin Block!\n\nSelect Option Provided Below")
            ad = input("1.Active Users \n2.Active User Names\n3.Users Info.\n4.Remove User\n0.Exit\n")
            while ad != '0':

                if ad == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    c_user = 0
                    for users in d:
                        c_user += 1
                    print ("Active:")
                    print ("Active Users :",c_user)

                elif ad == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    c_user = 0
                    print ("Active User Names:")
                    for users in d:
                        c_user += 1
                        print ("Active User",c_user,':',users)

                elif ad == '3':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ("Users Info:")
                    for info in d.keys():
                        print ("Name =",info,", Pin :",d[info][0],", Amount :",d[info][1])

                elif ad == '4':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return del_account()
                ad = input("1.Active Users \n2.Active User Names\n3.Users Info.\n4.Remove User\n0.Exit\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            return login_user()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return login_user()
    #users block
    elif user_name in d.keys():
        while int(entry) != 3:
            print("Entries left :",(3-entry))
            pin = str(input("Enter 4-Digit Pin : "))

            if pin == d[user_name][0]:
                Net_balance = d[user_name][1]
                Pin = d[user_name][0]
                os.system('cls' if os.name == 'nt' else 'clear')
                return atm(user_name,Net_balance,Pin)

            else:
                entry += 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("Incorrect Pin!")
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Login Unsuccessful\n")
        return login_user()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Invalid User!")
        return login_user()


def new_account():
    filename = join()
    user_name1 = input("New Account\nEnter First Name : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    user_name2 = input("Enter Last Name : ")

    if (user_name1.isalpha() == False) or (user_name2.isalpha() == False) or (user_name1 == user_name2):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Invalid Name")
        return new_account()


    os.system('cls' if os.name == 'nt' else 'clear')
    pin_count = 0
    while pin_count != 3:
        print("Entries left :",(3-pin_count))
        pin = str(input ("Enter 4-Digit Pin : "))
        os.system('cls' if os.name == 'nt' else 'clear')

        if (len(pin) == 4) and (pin.isdigit() == True):
            os.system('cls' if os.name == 'nt' else 'clear')
            confirm_pin = str(input ("Confirm Pin : "))

            if pin == confirm_pin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("Account Name :",user_name1+' '+user_name2,"\nPin :",pin)
                confirm = input("Please Confirm \n1. Yes \n2. No \n")

                if (confirm == '1') or (confirm.lower().startswith('y')):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    with open(filename, "a") as wr:
                        enc_name = user_name1+' '+user_name2
                        #rot13() function is called for encoding
                        enc = rot13(enc_name)
                        new = "\n"+enc+":"+pin+",0.0"
                        wr.write(new)
                        wr.close()
                        print ("Account Created Successfully! \n")
                        return login_user()

                elif (confirm == '2') or (confirm.lower().startswith('n')):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ("Account Not Created!")
                    return login_user()

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ("Account Not Created!")
                    return new_account()

            else:
                print ("Your Pin Did Not Match!")
                pin_count +=1

        else:
            pin_count = pin_count
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Invalid Pin")

    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Account Not Created!")
    return login_user()

def del_account():
    d = data()
    filename = join()

    os.system('cls' if os.name == 'nt' else 'clear')
    acc_name = input("Delete Account\nEnter Full Name : ")

    if acc_name in d.keys():
        acc_pin = str(input("Enter 4-Digit Pin : "))

        if acc_pin == d[acc_name][0]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Delete Account :",acc_name)
            confirm = input("Please Confirm \n1. Yes \n2. No \n")

            if (confirm == '1') or (confirm.lower().startswith('y')):
                os.system('cls' if os.name == 'nt' else 'clear')
                if d[acc_name] == d['abc xyz']:
                    del d[acc_name]
                else:
                    del d[acc_name],d['abc xyz']
                #over_writing of existing file
                with open(filename,"w") as rd:
                    rd.write('nop klm:1234,0.0')
                    rd.close()
                with open(filename,"a") as ow:
                    for item in d.keys():
                        items = rot13(item)
                        over_write = '\n'+items+':'+d[item][0]+','+str(d[item][1])
                        ow.write(over_write)
                    ow.close()
                    print ("Account Deleted Successfully! \n")
                    return login_user()

            elif (confirm == '2') or (confirm.lower().startswith('n')):
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("Account Not Deleted!")
                return login_user()

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("Account Not Deleted!")
                return login_user()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Incorrect Pin!")
            return login_user()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Account Does Not Exist!")
        return login_user()


try:
    os.system('cls' if os.name == 'nt' else 'clear')
    login_user()
except:
    Exception
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Sorry for inconvenience.")
    print ("Some errors were encountered,\nPlease be careful next time.\nGood bye!")
