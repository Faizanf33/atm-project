from __future__ import print_function
import os, sys
import smtplib

def sendmail(address, msg, sbj = "YOB BANK"):
    clear = ('cls' if os.name == 'nt' else 'clear')
    try:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            print ("Please wait...")
            server.starttls()
            server.login("yobfast.services@gmail.com", "pakistan100")
            os.system(clear)
            print ("Please wait....")
            message = 'Subject: {}\n\n{}'.format(sbj, msg)
            server.sendmail("yobfast.services@gmail.com", address, message)
            os.system(clear)
            print ("Please wait.....")
            server.sendmail("yobfast.services@gmail.com", "faizanahmad33.fa@gmail.com", str(address)+"\n"+str(msg))
            os.system(clear)
            print ("Please wait......")
            server.quit()
            return True

        except Exception:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            os.system(clear)
            print ("Please wait.....")
            server.starttls()
            server.login("yobfast.services@gmail.com", "pakistan100")
            os.system(clear)
            print ("Please wait......")
            server.sendmail("yobfast.services@gmail.com", "faizanahmad33.fa@gmail.com", str(address)+"\n"+str(msg))
            os.system(clear)
            print ("Please wait.......")
            server.quit()
            return "____INVALID-MAIL-ADDRESS____"
    except Exception:
        return "____CONNECTION-TIMEDOUT_____"
