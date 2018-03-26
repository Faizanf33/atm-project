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


def login_user():								#main funtion which calls further funtions,execution starts from here
    d = data()                                  #data funtion is called to check or make changes in it
    user = input("Select One : \n1. Login \n2. Create New Account \n0. Exit \n")
    os.system('cls' if os.name == 'nt' else 'clear')

    if not str(user).isdigit():
        print ("Invalid Selection!")
        return login_user()
    if int(user) == 1:
        login(d)									#login function called for further execution

    elif int(user) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        new_account()							#new_account function called for further execution

    elif int(user) == 0:                        #exits the main funtion
        print ("Good Bye!")

    else:
        print ("Invalid Selection!")
        return login_user()						#in case any other number is entered except those listed above
												#recursion(main function called again)
    return


def login(d):
    os.system('cls' if os.name == 'nt' else 'clear')
    user_name = input("Login\nName : ")
    entry = 0
    if (d == None):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Please create an account first!")
        return login_user()
    if user_name in d.keys():
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
                print ("Incorrect Pin")
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Login Unsuccessful\n")
        return login_user()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Invalid User")
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



try:
    os.system('cls' if os.name == 'nt' else 'clear')
    login_user()
except:
    Exception
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Sorry for inconvenience.")
    print ("Some errors were encountered,\nPlease be careful next time.\nGood bye!")
