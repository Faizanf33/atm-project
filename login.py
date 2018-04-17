from __future__ import print_function
from ATM import atm
from encrypt import rot13
from Data import data,join
import os
import sys
import csv
import random as rd


# Using input() in python 2 or 3
try:
    # set raw_input as input in python2
    input = raw_input
except:
    pass

#main funtion which calls further funtions,execution starts from here
def login_user():
    clear = ('cls' if os.name == 'nt' else 'clear')
    #data funtion is called to check or make changes in it
    d = data()

    user = input("Select One : \n1. Login \n2. Create New Account \n3. Delete Existing Account \n0. Exit \n")
    os.system(clear)

    if not str(user).isdigit():
        print ("Invalid Selection!")
        return login_user()

    #login function called for further execution
    if int(user) == 1:
        os.system(clear)
        login(d)

    #new_account function called for further execution
    elif int(user) == 2:
        os.system(clear)
        new_account()

    elif int(user) == 3:
        os.system(clear)
        del_account()

    #exit the main funtion
    elif int(user) == 0:
        print ("Good Bye!")

    #in case any other number is entered except those listed above
    #recursion(main function called again)
    else:
        print ("Invalid Selection!")
        return login_user()

    return


def login(d):
    clear = ('cls' if os.name == 'nt' else 'clear')
    import time,datetime
    os.system(clear)
    user_name = input("Login\nEnter Full Name : ")
    entry = 0
    if (d == None):
        os.system(clear)
        print ("Please create an account first!")
        return login_user()

    for a in user_name:
        if ((ord(a) >= 65) and (ord(a) <= 90)) or ((ord(a) >= 97) and (ord(a) <= 122)) or (ord(a) == 32):
            continue
        else:
            os.system(clear)
            print ("Invalid User!")
            return login_user()

    #--Admin Block--
    if (user_name.lower() in d.keys()) and (user_name.lower() == 'admin access'):
        user_name = user_name.lower()
        pin = str(input("Enter 4-Digit Pin : "))

        if pin == d[user_name][0]:
            del d[user_name]
            os.system(clear)
            print (time.strftime('Date:%d-%b-%Y \nTime:%I:%M %p  Today:%A\n'))
            print ("Welcome to YOB Admin Block!\n\nSelect Option Provided Below")
            ad = input("1.Active Users \n2.Active User Names\n3.Users Info.\n4.Remove User\n0.Exit\n")
            while ad != '0':

                if ad == '1':
                    os.system(clear)
                    c_user = 0
                    for users in d:
                        c_user += 1
                    print ("Active:")
                    print ("Active Users :",c_user)

                elif ad == '2':
                    os.system(clear)
                    c_user = 0
                    print ("Active User Names:")
                    for users in d:
                        c_user += 1
                        print ("Active User",c_user,':',users)

                elif ad == '3':
                    os.system(clear)
                    print ("Users Info:")
                    for info in d.keys():
                        print ("Name =",info,", Pin :",d[info][0],", Amount :","{:,}".format(d[info][1]))

                elif ad == '4':
                    os.system(clear)
                    return del_account()
                ad = input("1.Active Users \n2.Active User Names\n3.Users Info.\n4.Remove User\n0.Exit\n")
            os.system(clear)
            return login_user()

        else:
            os.system(clear)
            return login_user()

    #users block
    elif user_name.lower() in d.keys():
        user_name_l = user_name.lower()
        while int(entry) != 3:
            print("Entries left :",(3-entry))
            pin = str(input("Enter 4-Digit Pin : "))

            if pin == d[user_name_l][0]:
                Pin = d[user_name_l][0]
                Net_balance = d[user_name_l][1]
                History = d[user_name_l][2]
                os.system(clear)
                return atm(user_name,Net_balance,Pin,History)

            else:
                entry += 1
                os.system(clear)
                print ("Incorrect Pin!")
        os.system(clear)
        print ("Login Unsuccessful\n")
        return login_user()

    else:
        os.system(clear)
        print ("Invalid User!")
        return login_user()


def new_account():
    clear = ('cls' if os.name == 'nt' else 'clear')
    import time,datetime

    filename = join()
    user_name1 = input("New Account\nEnter First Name : ")
    os.system(clear)
    user_name2 = input("Enter Last Name : ")

    if (user_name1.isalpha() == False) or (user_name2.isalpha() == False) or (user_name1 == user_name2):
        os.system(clear)
        print ("Invalid Name!")
        return new_account()

    #auto-generated pin
    auto_gen_pin = rd.randint(1000,9999)
    os.system(clear)

    print("Your Auto-Generated Pin : ",auto_gen_pin)
    confirm = input("Want To Use This Pin ? \n1. Yes \n2. No \n")

    if (confirm == '1') or (confirm.lower().startswith('y')):
        os.system(clear)

        print ("Account Name :",user_name1+' '+user_name2,"\nPin :",auto_gen_pin)
        confirm = input("Please Confirm \n1. Yes \n2. No \n")

        if (confirm == '1') or (confirm.lower().startswith('y')):
            os.system(clear)
            with open(filename, "a+") as wr:
                enc_name = (user_name1.lower())+' '+(user_name2.lower())
                #rot13() function is called for encoding
                enc = rot13(enc_name)
                new = [enc,auto_gen_pin,'0.0',time.strftime('%d-%b-%Y at %I:%M %p')]

                w = csv.writer(wr)
                w.writerow(new)
                wr.close()
                print ("Account Created Successfully! \n")
                return login_user()

        elif (confirm == '2') or (confirm.lower().startswith('n')):
            os.system(clear)
            print ("Account Not Created!")
            return login_user()

        else:
            os.system(clear)
            print ("Account Not Created!")
            return new_account()



    else:
        os.system(clear)
        pin_count = 0
        print("Create Your Own Pin....")
        while pin_count != 3:
            print("Entries left :",(3-pin_count))
            pin = str(input ("Enter 4-Digit Pin : "))
            os.system(clear)

            if (len(pin) == 4) and (pin.isdigit() == True):
                os.system(clear)
                confirm_pin = str(input ("Confirm Pin : "))

                if pin == confirm_pin:
                    os.system(clear)
                    print ("Account Name :",user_name1+' '+user_name2,"\nPin :",pin)
                    confirm = input("Please Confirm \n1. Yes \n2. No \n")

                    if (confirm == '1') or (confirm.lower().startswith('y')):
                        os.system(clear)
                        with open(filename, "a+") as wr:
                            enc_name = (user_name1.lower())+' '+(user_name2.lower())
                            #rot13() function is called for encoding
                            enc = rot13(enc_name)
                            new = [enc,pin,'0.0',time.strftime('%d-%b-%Y at %I:%M %p')]

                            w = csv.writer(wr)
                            w.writerow(new)
                            wr.close()
                            print ("Account Created Successfully! \n")
                            return login_user()

                    elif (confirm == '2') or (confirm.lower().startswith('n')):
                        os.system(clear)
                        print ("Account Not Created!")
                        return login_user()

                    else:
                        os.system(clear)
                        print ("Account Not Created!")
                        return new_account()

                else:
                    print ("Your Pin Did Not Match!")
                    pin_count +=1

            else:
                pin_count = pin_count
                os.system(clear)
                print ("Invalid Pin!")

        os.system(clear)
        print ("Account Not Created!")
        return login_user()

def del_account():
    clear = ('cls' if os.name == 'nt' else 'clear')
    d = data()
    filename = join()

    os.system(clear)
    acc_name = input("Delete Account\nEnter Full Name : ")

    if acc_name.lower() in d.keys():
        acc_name = acc_name.lower()
        acc_pin = str(input("Enter 4-Digit Pin : "))

        if acc_pin == d[acc_name][0]:
            os.system(clear)
            print ("Delete Account :",acc_name)
            confirm = input("Please Confirm \n1. Yes \n2. No \n")

            if (confirm == '1') or (confirm.lower().startswith('y')):
                os.system(clear)
                del d[acc_name]

                #over_writing of existing file
                with open(filename,"w") as rd:
                    r = csv.writer(rd)
                    r.writerow(['Name','PIN','Amount','History'])
                    rd.close()

                with open(filename,"a") as ow:
                    for item in d.keys():
                        items = rot13(item)
                        over_write = [items,d[item][0],str(d[item][1]),str(d[item][2])]
                        o = csv.writer(ow)
                        o.writerow(over_write)
                    ow.close()
                    print ("Account Deleted Successfully! \n")
                    return login_user()

            elif (confirm == '2') or (confirm.lower().startswith('n')):
                os.system(clear)
                print ("Account Not Deleted!")
                return login_user()

            else:
                os.system(clear)
                print ("Account Not Deleted!")
                return login_user()

        else:
            os.system(clear)
            print ("Pin Did Not Match!")
            return login_user()

    else:
        os.system(clear)
        print ("Account Does Not Exist!")
        return login_user()

clear = ('cls' if os.name == 'nt' else 'clear')
try:
    os.system(clear)
    login_user()

except Exception as exc:
    os.system(clear)
    print ("Some errors were encountered: %s" %exc)
    print ("Sorry for inconvenience.\nGood bye!")
