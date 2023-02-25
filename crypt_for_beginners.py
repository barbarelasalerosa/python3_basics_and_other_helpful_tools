#! /usr/bin/python3
# crypt_for_beginners.py Author: barbarelasalerosa 
# contact: jerusalemabandida@proton.me

import pyperclip
import time


info = "Hi, this is 1st Chapter of Basic Cryptography or Cryptography For Beginners in Python Programming Language."
print(info)
print()
time.sleep(3)
info = "This program will reverse Your Message which may not contain less than 20 characters. Also, You will have to choose some number randomly (e.g. month of Your birth), so that this number do not exceed 12.\nTry with number 2, so you will see what happens!\nEnjoy!" 
print(info)
print()
time.sleep(12)
message = input("Enter Your Message: ")
funnynumber = input("Enter Your Number: ")
translated = ""

i = len(message) - int(funnynumber)
while i >= 0:
    translated = translated + message[i]
    i = i - int(funnynumber)
print(translated)

info = "Good. Now, let's get started with 1.1 Chapter!"
print(info)
time.sleep(2)
message = input("Enter Your Message: ")
key = int(input("Enter Yor Key: "))
mode = input("Enter the mode: ")
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@=#$-%^&*)(/+"
translated = ''
message = message.upper()
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print(translated)
pyperclip.copy(translated)  

info = "THIS PROGRAM WILL ENCRYPT OR DECRYPT YOUR 'SECRET MESSAGE'. IN CASE IT IS ALREADY ENCRYPTED, YOU WILL CHOOSE MODE 'DECRYPT'. IN OTHER CASE, YOUR CHOICE WILL BE 'ENCRYPT'. CHOOSE YOUR SECRET KEY (WHICH MUST BE SOME NUMBER/INTEGER) AND (UN)LOCK THE MESSAGE OF YOURS.\nIN THE NEXT FEW SECONDS YOU WILL BE ASKED TO ENTER CERTAIN INFORMATION. ENJOY OUR PROGRAM!"
print(info)
print()
time.sleep(25)
message = input("Enter Your Secret Message: ")
key = int(input("Enter Your Key: "))
mode = input("Enter the Mode: ")
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*)(/*-+,.;"
translated = ""
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + int(key)
        elif mode == 'decrypt':
            num = num - int(key)
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print(translated)
pyperclip.copy(translated)

info2 = "IN THIS CHAPTER, YOU ARE ABOUT TO ENTER YOUR ENCRYPTED MESSAGE (IN CASE IT HAD ALREADY BEEN ENCRYPTED, PLEASE COPY IT AGAIN AND FOLLOW SAME INSTRUCTIONS). AFTER TYPING IT, MESSAGE WILL BE DECRYPTED AS MANY TIMES AS IT IS POSSIBLE.\nENJOY OUR PROGRAM 'NOCH EINMAL'!"
print(info2)
print()
time.sleep(20)
message2 = input("Enter Your Encrypted Message: ")
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*)(/*-+,.;"
for key in range(len(LETTERS)):
    translated = ""
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
            
    print("Key #%s: %s" % (key,translated))


