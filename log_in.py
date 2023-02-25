#! /usr/bin/python3
# log_in.py Author: barbarelasalerosa 
# contact: jerusalemabandida@proton.me

import sys
import time
import re
import phonenumbers
import ftplib
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from email_validator import validate_email, EmailNotValidError
from ndicts.ndicts import NestedDict

registeredUsers = {

    "user1":{
        "Name":"Rebacca",
        "Surname":"Buck",
        "Phone Number or email address":"tank_girl69@gmail.com",
        "Password":"M!keTyS0n2002",
        "Birthday":"02.02.1999."   
            },
    "user2":{
        "Name":"Kevin",
        "Surname":"Tnimick",
        "Phone Number or email address":"kevin_elcondorpasa@hotmail.com",
        "Password":"R!Ba69IgR1Ze>>",
        "Birthday":"11.09.1978."    
            },
    "user3":{
        "Name":"Paul",
        "Surname":"Hawkins",
        "Phone Number or email address":"verax1971@proton.com",
        "Password":"lacasadepapel2027",
        "Birthday":"12.12.2007."
            },
    "user4":{
        "Name":"John",
        "Surname":"Wayne",
        "Phone Number or email address":"wildwildwest909@yahoo.com",
        "Password":"moutinyonthebountyisnotmymovie",
        "Birthday":"12.05.1999."
        }
    }     

print("This is Registration Time!\n\nPlease follow instructions.")
print()
name = input("Please enter Your Name: ")
surname = input("Please enter Your Surname: ")
phonenumber = str(input("Please enter Your mobile number: "))
car = carrier._is_mobile(number_type(phonenumbers.parse(phonenumber)))
print(car)
if car is True:   # We could have typed here 'if car == 1:', where '1' is equivalent for 'True'.
    print("Phone Number is valid.")
else:
    print("Phone Number is invalid!")
    sys.exit(0)
emailaddress = str(input("Please enter valid email address: "))   # We can use both 're library' and 'email_validator library' for this part of task. 
regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"       
if(re.fullmatch(regex,emailaddress)):
    print("Your email address is valid!")
else:
    print("Sorry, but You entered an invalid email address.")
try:
    validation = validate_email(emailaddress)
    emailaddress = validation["email"]
    print()
except EmailNotValidError as e:
    print(str(e))
    sys.exit(0)    
password = input("Please, create the strong(est) password which must contain 12 or more characters that must include capital letters, small letters, numbers, and other characters: " )            
if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{12,}', password) or len(password) > 12:
    print("Rule is satisfied!")
else:
    print("Strong password, damit!")
    print("Fine, it's Your funeral!!!")
print()
birthday = input("Please add your Birthday: ")
print()
addingNewUser = print("New User is Added:\n\n\tName: %s\n\tSurname: %s\n\tPhone Number: %s\n\temail address: %s\n\tPassword: %s\n\tBirthday: %s" % (name,surname,phonenumber,emailaddress,password,birthday))
print()
print("New User is added.")
print() 


