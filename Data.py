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
    new = ['Account Number','Name','PIN','Amount','Time']

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
                            if indiv_user_info == ['Account Number','Name','PIN','Amount','Time']:
                                continue
                            else:
                                try:
                                    #rot13() function is called for decoding
                                    indiv_user_info[1] = rot13(indiv_user_info[1])
                                    indiv_user_info[3] = float(indiv_user_info[3])
                                    d[indiv_user_info[0]] = indiv_user_info[1],indiv_user_info[2],indiv_user_info[3],indiv_user_info[4],indiv_user_info[5]

                                except IndexError:
                                    d[indiv_user_info[0]] = indiv_user_info[1],indiv_user_info[2],indiv_user_info[3],indiv_user_info[4],"None"
                        return d

    except:
        IOError or FileNotFoundError
        os.mkdir("Data")
        data()
