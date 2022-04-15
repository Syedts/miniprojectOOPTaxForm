# Author : Syed Thahirr Shahid 400421993
#imports

from MyClasses import *

import os
import sys
import time
# the title of the program 

print("----------------------------------------------------------------------------------------")
print("-------------- Welcome to the Tax Filling Software by Syed Thahirr Shahid --------------")
print("----------------------------------------------------------------------------------------")


def getInfo_from_getmoreinfo_file(info):
    execcommand= "python getmoreinfo.py "+info
    os.system(execcommand)
    
#This function makes the T4 Object
def makeT4obj():
    name = input("Enter Employeer Name: ")
    sinno = input("Sin Number: ")
    year = input("Year: ")
    box14 = input("Box 14- Employment Income: $")
    box18 = input("Box 18- Employee's EI premiums: $")
    box20 = input("Box 20- RPP Contributions: $")
    box44 = input("Box 44- Union Dues: $")
    box46 = input("Box 46-Charitable Donations: $")
    print(" \n \n")
    p1 = T4(name,sinno,year,box14,box18,box20,box44,box46)
    p1.addtoform()
    return p1

#This Function makes the RRSP Object 

def makeRRSPobj():
    name = input("Enter Name: ")
    taxyear = input("Tax Year: ")
    sinno = TaxForm.sin_number
    first_period_amount = input("[RRSP1] First Period Amount: $")
    second_period_amount = input("[RRSP2] Second Period Amount: $")
    CS_indicator = input("[RRSP3] Indicate whether or not your spouse or common-law partner has ever contributed to your retirement income plan (yes/no): ")
    p2 = RRSP(name,sinno,taxyear,first_period_amount,second_period_amount,CS_indicator)
    p2.addtoform()
    return p2


# This makes the T4A Object 
def makeT4Aobj():
    #Get information from the user and use previous info.
    payeename = input("Enter Payer's Name: ")
    year = input("Enter Year of payment made: ")
    sinno = TaxForm.sin_number
    b13 = input("Recipient's program account number: ")
    b16 = input("Pension or superannuation: $")
    b18 = input("Lump-sum Payments: $")
    b22 = input("Income Tax Deducted: $")
    b48 = input("Fees for services: $")
    print(" \n \n")
    p3 = T4A(payeename,sinno,year,b13,b16,b18,b22,b48)
    p3.addtoform()

    return p3

def main ():
    # Creating the menu
    # I have multiple print line for readability
    while True:
        userinput = 0
        prompt = ""
        print("Welcome to the main menu, Please have all your tax papers ready.")
        print("3) To print out the Tax Form Summary")
        print("2) For Information ")
        print("1) To Start Filing your Taxes , Type 1 ")
        print("0) To Exit, Type exit")
        userinput = input("Option:")
        match userinput.lower():
            case "1":
                while prompt != "back":
                    print("Enter 1 for T4 \nEnter 2 for RRSP \nEnter 3 for T4A \nEnter back to go back to the main menu \n")
                    prompt = input("Enter:")
                    if prompt == "1":
                        print('''
=============================================================================================   
                    |    T4 form       |
=============================================================================================
                        ''')
                        p1 = makeT4obj()
                        print(p1)
                    if prompt == "back":
                        break    
                    if prompt == "2":
                        print('''
=============================================================================================  
                    |    RRSP form       |
============================================================================================= 
                        ''')
                        p2 = makeRRSPobj()
                        print(p2)
                    if prompt == "3":
                        print('''
=============================================================================================  
                    |    T4A form       |
============================================================================================= 
                        ''')
                        p3 = makeT4Aobj()
                        print(p3)
                
            case "exit":
                print("See you again!")
                sys.exit(0)
            case "2":
                print("Type in the form name then the box number. Syntax is as follows: T414 \n")  
                info = input("What do you need more information on? ")
                print(getInfo_from_getmoreinfo_file(info))
            case "3":
                print("Printing Summary to screen and making a pdf file !!!")
                p1.showform()
                p1.printtofile()
                p1.printtopdf()
                p2.showform()
                p2.printtofile()
                p2.printtopdf()
                p3.showform()
                p3.printtofile()
                p3.printtopdf()
            case _:
                print("Invalid Input , Try Again")
                time.sleep(1)



main()

