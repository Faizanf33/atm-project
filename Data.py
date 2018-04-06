from encrypt import rot13
import os
import csv

#relative path for file
def join():
    directory = "Data"
    name = "usersdata.csv"
    filename = os.path.join(directory, name)
    return filename

#when 1 is entered from main(login_user)
def data():
    filename = join()
    d = {}
    new = ['Name','PIN','Amount','History']

    try:
        #file size shorter than 13 bit
        with open(filename, "a") as ap:
            if (os.path.getsize(filename)) <= 0:
                wr = csv.writer(ap)
                wr.writerow(new)
                ap.close()
                print ("Please create an account first!")
                return

            else:
                with open(filename, "r") as rd:
                        r = csv.reader(rd)
                        for indiv_user_info in r:
                            if indiv_user_info == ['Name','PIN','Amount','History']:
                                continue
                            else:
                                #rot13() function is called for decoding
                                indiv_user_info[0] = rot13(indiv_user_info[0])
                                indiv_user_info[2] = float(indiv_user_info[2])
                                d[indiv_user_info[0]] = indiv_user_info[1],indiv_user_info[2],indiv_user_info[3]
                        return d

    except:
        IOError or FileNotFoundError
        os.mkdir("Data")
        data()
