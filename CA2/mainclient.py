'''
Name: Metta Tan
Admin Number: 1904275
Class: 1B/02
'''

import socket
def getnewsocket():
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket = getnewsocket()
host = "localhost"
clientsocket.connect((host, 8089))		
def sendMessage(msg):
    clientsocket.sendall(msg.encode())

def isFloat(string): #checks if string is a float
    try:
        float(string)
        return True
    except ValueError:
        return False
 
def choose(): # main SPAM system
    global choice
    try:
        choice = int(input("What would you like to do?\n\n1) Display Today's Menu\n\n2) Search Menu\n\n3) Display Cart\n\n4) Check Out\n\nPlease input your choice of action (5 to exit): "))
        print()
    except ValueError:  
        print("Invalid input. Exiting program.")
        choice = 5

orders = [] #order list
preorders = [] #preorder list
total = 0
preordertotal = 0

prices = []
foods = []

def orderfood():
    global order
    order = "h"

    while order != 0:
        try:
            order = int(input("Enter the number of the dish you would like to order or 0 to stop: ")) #to order food
            print()
            if order in range(len(todayfoods) + 1):
                if order != 0:
                    orders.append(order)
            else:
                print("Number out of range.")
        except ValueError:
            print("Invalid input. Please enter the number of the dish you would like to order.\n")

def preorder():
    global preorder
    preorder = "h"

    while preorder != 0:
        try:
            preorder = int(input("Enter the number of the dish you would like to order or 0 to stop: ")) #to order food
            print()
            if preorder in range(len(tmrfoods) + 1):
                if preorder != 0:
                    preorders.append(preorder)
            else:
                print("Number out of range.")
        except ValueError:
            print("Invalid input. Please enter the number of the dish you would like to order.\n")

acc = input("Do you have a SPAM account? Enter 'y' if yes or 'c' if you would like to create an account (ENTER if no): ") 
print()
if acc == "y" or acc == "c":
    var = "acc"
    sendMessage(var) #if trying to login or create account
    if acc == "y": #login
        while True:
            username = input("Enter your username: ")
            if username == "": #if enter is pressed, exit from login menu
                user = "n"
                sendMessage(user)
                username = "guest"
                break
            elif " " in username:
                print("Spaces are not allowed.")
            else: 
                password = input("Enter your password: ")
                if password == "": #if enter is pressed, exit from login menu
                    user = "n"
                    sendMessage(user)
                    username = "guest"
                    break
                elif " " in password:
                    print("Spaces are not allowed.")
                else:
                    user = username + " " + password
                    sendMessage(user) #sends login info to server
                    login = clientsocket.recv(4096) 
                    print(login.decode())
                    if login.decode() == "Login success!": #if login is successful
                        break  
    elif acc == "c": #create account
        while True:
            newuser = input("Please enter a username: ")
            if newuser == "": #if enter is pressed, exit from login menu
                createuser = "n"
                sendMessage(createuser)
                user = ""
                username = "guest" #will login user as guest
                break
            elif " " in newuser:
                print("Spaces are not allowed.")
            elif "," in newuser:
                print("Commas are not allowed.")
            else:
                newpass = input("Please enter a password: ")
                if newpass == "": #if enter is pressed, exit from login menu
                    createuser = "n"
                    sendMessage(createuser)
                    user = ""
                    username = "guest"
                    break
                elif " " in newpass:
                    print("Spaces are not allowed.")
                elif "," in newpass:
                    print("Commas are not allowed.")
                else:
                    createuser = newuser + "," + newpass
                    sendMessage(createuser)
                    user = ""
                    create = clientsocket.recv(4096)
                    print(create.decode())
                    if create.decode() == "Account successfully created.": # if account is sucessfully created
                        username = newuser # user will be addressed as that username
                        break  
    else: 
        user = "n"
        sendMessage(user)
        username = "guest"
else:
    var = "no"
    sendMessage(var)
    username = "guest"

data = clientsocket.recv(4096) # receive menu data
data2 = data.decode()
menufile = data2.split(',') # put menu into list

for i in range(len(menufile)):
    if menufile[i] != '':
        if isFloat(menufile[i]):
            prices.append(menufile[i]) #puts prices in prices list
        else:
            foods.append(menufile[i]) #puts food items into foods list

for i in range(len(prices)):
    prices[i] = float(prices[i]) #converts prices list items to float type
end = "end"
sendMessage(end) # closes server
clientsocket.close()
print("Connection closed.\nServer shut down.\n")

print("Welcome to SPAM, " + username)

from datetime import date
import calendar
my_date = date.today()
day = calendar.day_name[my_date.weekday()]

if day == 'Monday':
    todayfoods = foods[0:4]
    todayprices = prices[0:4]
    tmrfoods = foods[4:8]
    tmrprices = prices[4:8]
elif day == 'Tuesday':
    todayfoods = foods[4:8]
    todayprices = prices[4:8]
    tmrfoods = foods[8:12]
    tmrprices = prices[8:12]
elif day == 'Wednesday':
    todayfoods = foods[8:12]
    todayprices = prices[8:12]
    tmrfoods = foods[12:16]
    tmrprices = prices[12:16]
elif day == 'Thursday':
    todayfoods = foods[12:16]
    todayprices = prices[12:16]
    tmrfoods = foods[16:20]
    tmrprices = prices[16:20]
elif day == 'Friday':
    todayfoods = foods[16:20]
    todayprices = prices[16:20]
    tmrfoods = foods[20:24]
    tmrprices = prices[20:24]
elif day == 'Saturday':
    todayfoods = foods[20:24]
    todayprices = prices[20:24]
    tmrfoods = foods[24:28]
    tmrprices = prices[24:28]
else:
    todayfoods = foods[24:28]
    todayprices = prices[24:28]
    tmrfoods = foods[0:4]
    tmrprices = prices[0:4]
    
choose()
while choice != 5: #5 will exit the program
    if choice == 1: #display menu
        print('Menu for today:\n')
        for i in range(len(todayfoods)):
            print(str((i + 1)) + ')', '{:<30}'.format(todayfoods[i]), '$' + '{:.2f}'.format(todayprices[i]) + '\n') 

        orderfood()

        showtmr = input("Would you like to view the menu for tomorrow? Enter 'y' if yes (ENTER if no): ") 
        if showtmr == 'y':
            print('Menu for tomorrow:\n')
            for i in range(len(tmrfoods)):
                print(str((i + 1)) + ')', '{:<30}'.format(tmrfoods[i]), '$' + '{:.2f}'.format(tmrprices[i]) + '\n') # displays menu for next day

            preorder()        #allows user to preorder items for next day
            if preorders != []:
                print('You have preordered these items:\n')
                for i in range(len(preorders)):
                    if (i + 1) <= 9:
                        print(str(i + 1) + ")", "{:<30}".format(tmrfoods[int(preorders[i]) - 1]), "$" + "{:.2f}".format(tmrprices[int(preorders[i]) - 1]) + "\n") #prints out users preorders
                    else:
                        print(str(i + 1) + ")", "{:<29}".format(tmrfoods[int(preorders[i]) - 1]), "$" + "{:.2f}".format(tmrprices[int(preorders[i]) - 1]) + "\n")        
                    preordertotal += tmrprices[int(preorders[i] - 1)] #calculates total
                print("Please pay a total of", "$" + str("{:.2f}".format(preordertotal))) #calculates total of preorders
                cfmpay = input("Confirm payment of preordered items? Enter 'y' if yes (ENTER if no): ")
                if cfmpay == 'y':
                    print('Payment confirmed. Thank you.')
                else:
                    print('Payment cancelled.')
        choose()
    elif choice == 2: #search menu
        order = "h"
        count = 0
        search = input("Please enter food to search (case-sensitive): ")
        print()
        searchlist = [] #store index of search results

        while order != 0:
            try:
                for i in range(len(todayfoods)):
                    if search in todayfoods[i]: #checks if the input is in the food list
                        print(str((i + 1)) + ')', '{:<30}'.format(todayfoods[i]), '$' + '{:.2f}'.format(todayprices[i]) + '\n') 
                        count += 1 #if there is a result, increment count
                        searchlist.append(i + 1)
                order = int(input("Enter the number of the dish you would like to order or 0 to stop: ")) #to order food
                print()
                if order in searchlist: #if the number the user entered is in the search results
                    if order != 0:
                        orders.append(order)
                else:
                    if order != 0:
                        print("Number out of range.\n")
            except ValueError:
                print("Invalid input. Please enter the number of the dish you would like to order.\n")
        choose()
    elif choice == 3: #display cart
        if orders == []: #if the order list is empty
            print("Your cart is empty. You can order dishes by entering 1 or 2.\n") #suggest that the user orders food
        elif orders != []:
            print("Please review your order:\n")
            for i in range(len(orders)):
                if (i + 1) <= 9:
                    print(str(i + 1) + ")", "{:<30}".format(todayfoods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") #prints out users orders
                else:
                    print(str(i + 1) + ")", "{:<29}".format(todayfoods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") 

            rmv = input("Would you like to remove any items from your cart? Enter 'y' if yes (ENTER if no): ") #ability to remove items
            print()

            rmv1 = "h"

            if rmv == "y":
                while rmv1 != 0:
                    for i in range(len(orders)):
                        if (i + 1) <= 9:
                            print(str(i + 1) + ")", "{:<30}".format(todayfoods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") #prints out users orders
                        else:
                            print(str(i + 1) + ")", "{:<29}".format(todayfoods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n")

                    rmv1 = int(input("Please enter the number of the item you would like to remove or 0 to stop: ")) 
                    print()

                    if rmv1 != 0:
                        if orders == []:
                            print("Your cart is empty. You can order dishes by entering 1 or 2.\n")
                            break
                        else:
                            del orders[rmv1 - 1] #remove orders based on what the user enters
        choose()
    elif choice == 4: #check out (user cannot go back at this point)
        if orders == []: #if the order list is empty
            print("Your cart is empty. You can order dishes by entering 1 or 2.\n") #suggest that the user orders food
            choose()
        elif orders != []:
            print("Please review your order:\n") 
            for i in range(len(orders)):
                if (i + 1) <= 9:
                    print(str(i + 1) + ")", "{:<30}".format(todayfoods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") #prints out users orders
                else:
                    print(str(i + 1) + ")", "{:<29}".format(todayfoods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") 

            for i in range(len(orders)):
                total += todayprices[int(orders[i] - 1)] #calculates total 

            disc = input("Do you have a discount code? Enter 'y' if yes (ENTER if no): ") #asks if user has a discount code
            print()

            if disc == "y":
                code = input("Enter discount code: ") 
                print()
                if code == "cbt": #if code entered matches the correct code
                    print("Valid code entered! You are eligible for a 10% discount on your bill.\n")
                    total = 0.9 * total #10% discount 
                else:
                    print("Invalid code entered.\n") #if wrong code is entered

            if username != "guest": #if user is logged in
                print("SPAM members get an additional 10% discount!\n")
                total = 0.9 * total #additional discount if user is a SPAM member.
                
            print("Please pay a total of", "$" + str("{:.2f}".format(total) + ".\n")) #prints out total that user has to pay
            break #end of program

print("Thank you for using SPAM, " + username)