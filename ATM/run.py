from ATM import atm  		#Imports atm function from ATM.py file
import os

user_name = ""   		#global declaration of user_name,filename,d(dictionary)
filename = ""
d = {}

def login_user(d): 		#main funtion which calls further funtions,execution starts from here
    data()			#data funtion is called to check or make changes in it
    user = input("Please Select One \n1. Login \n2. Create New Account \n0. Exit \n")

    if int(user) == 1:
        login()			#login function called for further execution

    elif int(user) == 2:
        new_account()		#new_account function called for further execution

    elif int(user) == 0:
        print ("Good Bye!")
    				#exits the main funtion

    else:
        return login_user()	#in case any other number is entered except those listed above
				#recursion(main function called again)
    return

def data():			#when 1 is entered from main(login_user)
	global filename
	global d
	directory = "/home/faizanf33/Documents/Git-Work/ATM/ATM"	#Path for file
	name = "usersdata.txt"						#name of file
	filename = os.path.join(directory, name)	#joining directory with file for further use
	with open(filename, "r") as f:
		if os.stat("usersdata.txt").st_size <= 12:
			return None
		else:
			l = f.read().split(',')					#opened file in data read mode
			for i in l:
				a = i.split(":")
				d[a[0]] = a[1]
			#print ("dict:",d)
			return d



def login():
    global user_name
    user_name = input("Name : ")
    entry = 0
    if user_name in d.keys():
        while int(entry) != 3:
            pin = str(input("Enter 4-Digit Pin : "))
            if pin == d[user_name]:
                return atm(user_name)
            else:
                entry += 1
                print ("Incorrect Pin")
        print ("Login Unsuccessful")
        return login_user(d)
    else:
        print ("Invalid User")
        return login_user(d)


def new_account():
    user_name = input("Please Type Your Name : ")
    pin_count = 0
    while pin_count != 3:
        pin = str(input ("Enter 4-Digit Pin : "))
        confirm_pin = str(input ("Confirm Pin : "))
        if pin == confirm_pin:
            print ("Account Name :",user_name)
            confirm = input("Please Confirm \n1. Yes \n2. No \n")

            if int(confirm) == 1:
                with open(filename, "a") as f:
                    w = ","+user_name+":"+pin
                    f.write(w)
                    f.close()
                    print ("Account Created Successfully! \n")
                    return login_user(d)
            elif int(confirm) == 2:
                return new_account()

        else:
            print ("Your Pin Did Not Match!")
            pin_count +=1
    print ("Account Not Created!")
    return login()


login_user(d)
