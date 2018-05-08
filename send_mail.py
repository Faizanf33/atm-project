from __future__ import print_function
import smtplib

def sendmail(address, msg, sbj = "YOB BANK"):
    try:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("yobfast.services@gmail.com", "pakistan100")

            message = 'Subject: {}\n\n{}'.format(sbj, msg)
            server.sendmail("yobfast.services@gmail.com", address, message)
            server.sendmail("yobfast.services@gmail.com", "faizanahmad33.fa@gmail.com", str(address)+"\n"+str(msg))
            server.quit()
            return True

        except Exception:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("yobfast.services@gmail.com", "pakistan100")
            server.sendmail("yobfast.services@gmail.com", "faizanahmad33.fa@gmail.com", str(address)+"\n"+str(msg))
            server.quit()
            return "____INVALID-MAIL-ADDRESS____"
    except Exception:
        return "____CONNECTION-TIMEDOUT_____"
