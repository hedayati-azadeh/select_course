import registery
import sign_in

class Menue:
    dict_menue = {"1": "registery" , "2" : "sign_in" , "3" : "exit"}
    print ("-----------------------------")
    print(" 1 - register" )
    print(" 2 - sign in ")
    print (" 3 - exit ")
    print ("-----------------------------")

    def chosse():
        select_menue = input(" choose your number : ")
        if select_menue == "1":
            registery.Register()
        elif select_menue == "2":
            sign_in.Sign()
        elif select_menue == "3":
            print(" exit ")