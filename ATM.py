#! /usr/bin/python3
# ATM.py Author: barbarelasalerosa 
# contact: jerusalemabandida@proton.me

import time
import sys
import random

class Card:
    naziv  = "Kim Bodnia"
    stanje = 2000
    PIN    = 1111
    klik   = ("R","L")
class Bankomat: 
    card = Card() 
    def set_card(self):
        print("Hello! Please enter Your card.")
        Card.klikunos = random.choice(Card.klik)
        if Card.klikunos == "R":
            pass
        else:
            print("Error.")
            sys.exit(0) 
        Card.PINunos = int(input("Please Mr.%s, enter Your PIN: " % (Card.naziv[3:10])))  
        if Card.PINunos != Card.PIN:
            print("You have entered the wrong PIN.\nGoodbye!")
            sys.exit(0)     
        elif Card.PINunos == Card.PIN:
            print("Success!")
            time.sleep(1)
        Card.unos = int(input("Enter amount of money, Mr.%s, You want to withdraw from Your account:" % (Card.naziv[3:10])))
    def withdraw(self):
        if Card.unos <= Card.stanje:
            novo_stanje = Card.stanje - Card.unos
            print("Success, new balance: %s." % (novo_stanje))
            time.sleep(1) 
        elif Card.unos > Card.stanje:
            print("We are sorry, Mr.%s, but the amount of money You have entered exceeds the amount You already have on Your account." % (Card.naziv[3:10]))
            print()
            print("You will have to enter Your card so as Your PIN one more time.")   
            time.sleep(1)
            print("Goodbye.")
            sys.exit(0)
cards = Bankomat()
cards.set_card()
cards.withdraw()
           
