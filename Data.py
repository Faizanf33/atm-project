from encrypt import rot13
import os
import re

#relative path for file
def join():
    directory = "Data"
    name = "usersdata.txt"
    filename = os.path.join(directory, name)
    return filename

#when 1 is entered from main(login_user)
def data():
    filename = join()
    d = {}

    try:
        with open(filename, "a") as ap:
            #file size shorter than 13 bit
            if os.stat(filename).st_size <= 0:
                ap.write('nop klm:1234,0.0')
                ap.close()
                print ("Please create an account first!")
                return

            else:
                with open(filename, "r") as rd:
                    id_user = rd.read().split("\n")				#opened file in data read mode
                    for items in id_user:
                        indiv_user_info = re.split("[:,]",items)
                        #rot13() function is called for decoding
                        indiv_user_info[0] = rot13(indiv_user_info[0])
                        indiv_user_info[1],indiv_user_info[2] = str(indiv_user_info[1]),float(indiv_user_info[2])
                        d[indiv_user_info[0]] = indiv_user_info[1],indiv_user_info[2]
                    return d

    except:
        IOError or FileNotFoundError
        os.mkdir("Data")
        data()
