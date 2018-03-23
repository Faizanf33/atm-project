from ATM import atm  							#Imports atm function from ATM.py file
import os
import sys
import re

user_name = ""   								#global declaration of user_name,filename,d(dictionary)
filename = ""
d = {}
directory = "Data"	#Path for file
name = "usersdata.txt"						#name of file
filename = os.path.join(directory, name)	#joining directory with file for further use


def login_user():
    global d 								#main funtion which calls further funtions,execution starts from here
    data()										#data funtion is called to check or make changes in it
    user = input("Please Select One \n1. Login \n2. Create New Account \n0. Exit \n")
    if not str(user).isdigit():
        print ("Invalid Selection!")
        return login_user()
    if int(user) == 1:
        login()									#login function called for further execution

    elif int(user) == 2:
        new_account()							#new_account function called for further execution

    elif int(user) == 0:
        print ("Good Bye!")
    											#exits the main funtion

    else:
        print ("Invalid Selection!")
        return login_user()						#in case any other number is entered except those listed above
												#recursion(main function called again)
    return

def data():										#when 1 is entered from main(login_user)
    global filename,name
    global d
    try:
        with open(filename, "a+") as ap:
            #file size shorter than 13 bit
            if os.stat(filename).st_size <= 0:
                ap.write('abc xyz:1234,0.0')
                ap.close()
                print ("Please create an account first!")
                return
            else:
                with open(filename, "r+") as rd:
                    id_user = rd.read().split("\n")				#opened file in data read mode
                    for i in id_user:
                        a = re.split("[:,]",i)
                        a[1],a[2] = int(a[1]),float(a[2])
                        d[a[0]] = a[1],a[2]
                    return d
    except:
        FileNotFoundError
        os.mkdir("Data")
        data()


def login():
    global user_name
    user_name = input("Name : ")
    entry = 0
    if user_name in d.keys():
        while int(entry) != 3:
            pin = int(input("Enter 4-Digit Pin : "))
            if pin == d[user_name][0]:
                Net_balance = d[user_name][1]
                Pin = d[user_name][0]
                return atm(user_name,Net_balance,Pin)
            else:
                entry += 1
                print ("Incorrect Pin")
        print ("Login Unsuccessful")
        return login_user()
    else:
        print ("Invalid User")
        return login_user()


def new_account():
    user_name1 = input("Enter First Name : ")
    user_name2 = input("Enter Last Name : ")

    if (user_name1.isalpha() == False) or (user_name2.isalpha() == False):
        print ("Invalid Name")
        return new_account()
    pin_count = 0
    while pin_count != 3:
        pin = str(input ("Enter 4-Digit Pin : "))
        if (len(pin) == 4) and (pin.isdigit() == True):
            confirm_pin = str(input ("Confirm Pin : "))
            if pin == confirm_pin:
                print ("Account Name :",user_name1+' '+user_name2,"\nPin :",pin)
                confirm = input("Please Confirm \n1. Yes \n2. No \n")

                if (confirm == '1') or (confirm.lower().startswith('y')):
                    with open(filename, "a") as wr:
                        new = "\n"+user_name1+' '+user_name2+":"+pin+",0.0"
                        wr.write(new)
                        wr.close()
                        print ("Account Created Successfully! \n")
                        return login_user()
                elif (confirm == '2') or (confirm.lower().startswith('n')):
                    return new_account()
                else:
                    return new_account()

            else:
                print ("Your Pin Did Not Match!")
                pin_count +=1
        else:
            pin_count = 0
    print ("Account Not Created!")
    return login()

try:
    login_user()
except:
    Exception
    print ("Some errors came encountered,\nPlease be careful next time.\nGood bye!")
