from __future__ import print_function
from ATM import atm
from encrypt import rot13
from Data import data,join
from acc_no_gen import account_no_gen
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

    user = input("Select One : \n1. Login \n2. Create New Account \n3. Activate Account \n4. De-Activate Account \n0. Exit \n")
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
        activate_account()

    elif int(user) == 4:
        os.system(clear)
        de_active_account()

    #exit the main funtion
    elif int(user) == 0:
        print ("Good Bye!")

    #in case any other number is entered except those listed above
    #recursion(main function called again)
    else:
        print ("Invalid Selection! '",user,"'")
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

    for item in d.keys():
        if user_name.lower() in d[item]:
            acc_no = item

    if acc_no.startswith('#'):
        os.system(clear)
        print("Account Is De-Activated")
        return login_user()

    #--Admin Block--
    elif (user_name.lower() == 'admin access'):
        pin = str(input("Enter 4-Digit Pin : "))
        if pin == d[acc_no][1]:
            del d[acc_no]
            os.system(clear)
            print (time.strftime('Date:%d-%b-%Y \nTime:%I:%M %p  Today:%A\n'))
            print ("::: Welcome to YOB Admin Block! :::\n\n:: Select Option Provided Below ::")
            ad = input("1. Number Of Users \n2. Active User Names \n3. Active Users Info. \n4. Users Acivity \n5. De-Activate Account\n0. Exit\n")
            while ad != '0':

                if ad == '1':
                    os.system(clear)
                    c_user, i_user = 0, 0
                    for users in d.keys():
                        if not users.startswith('#'):
                            c_user += 1
                        else:
                            i_user += 1

                    print(":: Users ::")
                    print("Active Users :",c_user)
                    print("Inactive Users :",i_user,'\n')

                elif ad == '2':
                    os.system(clear)
                    c_user = 0
                    print (":: Active User Names ::")
                    for users in d.keys():
                        if not users.startswith('#'):
                            c_user += 1
                            print ("Active User",c_user,':',d[users][0])
                    print('\n')

                elif ad == '3':
                    os.system(clear)
                    print (":: Users Info ::")
                    for user_info in d.keys():
                        if not user_info.startswith('#'):
                            print ("Name =",d[user_info][0],", Pin :",d[user_info][1],", Amount :","{:,}".format(d[user_info][2]))
                    print('\n')

                elif ad == '4':
                    os.system(clear)
                    print (":: Users Acivity ::")
                    for user_info in d.keys():
                        if not user_info.startswith('#'):
                            print ("Account Number :",user_info,"of Name :",d[user_info][0],"was previously logged in on",d[user_info][3])
                    print('\n')

                elif ad == '5':
                    os.system(clear)
                    return de_active_account()

                ad = input("1. Active Users \n2. Active User Names\n3. Users Info.\n4. Users Acivity \n5. De-Activate Account\n0. Exit\n")
            os.system(clear)
            return login_user()

        else:
            os.system(clear)
            return login_user()

    #users block
    elif not (user_name.lower() == 'admin access'):
        user_name_l = user_name.lower()
        while int(entry) != 3:
            print("Entries left :",(3-entry))
            pin = str(input("Enter 4-Digit Pin : "))

            if pin == d[acc_no][1]:
                Pin = pin
                Net_balance = d[acc_no][2]
                History = d[acc_no][3]
                os.system(clear)
                return atm(user_name,Net_balance,Pin,History,acc_no)

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

    full_name = (user_name1.lower())+' '+(user_name2.lower())
    acc_no = account_no_gen(full_name)

    print("Your Auto-Generated Pin : ",auto_gen_pin)
    confirm = input("Want To Use This Pin ? \n1. Yes \n2. No \n")

    if (confirm == '1') or (confirm.lower().startswith('y')):
        os.system(clear)

        print ("Account Name :",user_name1+' '+user_name2,"\nAccount Number :",acc_no,"\nPin :",auto_gen_pin)
        confirm = input("Please Confirm \n1. Yes \n2. No \n")

        if (confirm == '1') or (confirm.lower().startswith('y')):
            os.system(clear)
            with open(filename, "a+") as wr:
                #rot13() function is called for encoding
                enc = rot13(full_name)
                new = [acc_no,enc,auto_gen_pin,'0.0',time.strftime('%d-%b-%Y at %I:%M %p')]

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
                            #rot13() function is called for encoding
                            enc = rot13(full_name)
                            new = [acc_no,enc,pin,'0.0',time.strftime('%d-%b-%Y at %I:%M %p')]

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

def activate_account():
    clear = ('cls' if os.name == 'nt' else 'clear')
    d = data()
    filename = join()

    user_acc_no = str(input('Enter 12-Digit Account Number : '))
    os.system(clear)

    if not user_acc_no.isdigit():
        print('Invalid Account!')
        return login_user()

    elif user_acc_no in d.keys():
        print('Account Is Already Active!')
        return login_user()

    elif user_acc_no.isdigit():
        ch_acc_no = str('#'+user_acc_no)

        if ch_acc_no in d.keys():
            d[user_acc_no] = d.pop(ch_acc_no)
            print ("Activate Account Neme :",d[user_acc_no][0])
            confirm = input("Please Confirm \n1. Yes \n2. No \n")

            if (confirm == '1') or (confirm.lower().startswith('y')):
                os.system(clear)
                #over_writing of existing file
                with open(filename,"w") as rd:
                    r = csv.writer(rd)
                    r.writerow(['Account Number','Name','PIN','Amount','Time'])
                    rd.close()

                with open(filename,"a") as ow:
                    for item in d.keys():
                        items = rot13(d[item][0])
                        over_write = [item,items,str(d[item][1]),str(d[item][2]),str(d[item][3])]
                        o = csv.writer(ow)
                        o.writerow(over_write)
                    ow.close()
                    print ("Account Activated Successfully! \n")
                    return login_user()

            elif (confirm == '2') or (confirm.lower().startswith('n')):
                os.system(clear)
                print ("Account Not Activated!")
                return login_user()

            else:
                os.system(clear)
                print ("Account Not Activated!")
                return login_user()

        else:
            os.system(clear)
            print('Account Does Not Exist')
            return login_user()

def de_active_account():
    clear = ('cls' if os.name == 'nt' else 'clear')
    d = data()
    filename = join()

    os.system(clear)
    acc_no = input("Account De-activate\nEnter Account Number : ")

    if acc_no in d.keys():
        acc_pin = str(input("Enter 4-Digit Pin : "))

        if acc_pin == d[acc_no][1]:
            os.system(clear)
            print ("De-activate Account :",d[acc_no][0])
            confirm = input("Please Confirm \n1. Yes \n2. No \n")

            if (confirm == '1') or (confirm.lower().startswith('y')):
                os.system(clear)
                d[('#'+acc_no)] = d.pop(acc_no)
                #over_writing of existing file
                with open(filename,"w") as rd:
                    r = csv.writer(rd)
                    r.writerow(['Account Number','Name','PIN','Amount','Time'])
                    rd.close()

                with open(filename,"a") as ow:
                    for item in d.keys():
                        items = rot13(d[item][0])
                        over_write = [item,items,str(d[item][1]),str(d[item][2]),str(d[item][3])]
                        o = csv.writer(ow)
                        o.writerow(over_write)
                    ow.close()
                    print ("Account De-Activated Successfully! \n")
                    return login_user()

            elif (confirm == '2') or (confirm.lower().startswith('n')):
                os.system(clear)
                print ("Account Not De-Activated!")
                return login_user()

            else:
                os.system(clear)
                print ("Account Not De-Activated!")
                return login_user()

        else:
            os.system(clear)
            print ("Pin Did Not Match!")
            return login_user()

    else:
        os.system(clear)
        print ("No match found!")
        return login_user()

clear = ('cls' if os.name == 'nt' else 'clear')
try:
    os.system(clear)
    login_user()

except Exception as exc:
    os.system(clear)
    print ("Some errors were encountered: %s" %exc)
    print ("Sorry for inconvenience.\nGood bye!")
