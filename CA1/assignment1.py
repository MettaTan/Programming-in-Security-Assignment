'''
Name: Metta Tan
Admin Number: 1904275
Class: 1B/02
'''

#function declaration
def login(): #account management
    import csv
    reader = csv.reader(open('acc.csv')) #open account .csv file

    accounts = {} #dictionary for storing user accounts

    for col in reader:
        key = col[0] #set key as username
        accounts[key] = col[1] 

    acc = input("Do you have a SPAM account? Enter 'y' if yes or 'c' if you would like to create an account (ENTER if no): ") 
    print()

    global menu
    global foods
    global prices

    if acc == "y":
        user = input("Please enter your username: ")
        print()

        passwd = input("Please enter your password: ")
        print()

        if user == "admin":
            if passwd == "admin123":
                #   Curry Rice, 3.5, Pork Chop, 6, Prawn Noodles, 3, Salad, 2.8, Burger, 5, Chicken Rice, 2.5, Katsu Curry, 4.5, Bak Chor Mee, 3.5, Laksa, 4.5, Carrot Cake, 3.5, Fried Rice, 2.5, Chilli Crab, 6.5, Chee Chong Fun, 2.5, Mee Rebus, 3.5, Bak Kut Teh, 6.8, Fish & Chips, 4.5, Dim Sum, 5.2, Oyster Omelette, 5.0, Satay, 3.0, Nasi Lemak, 3.3, Mee Siam, 2.5, Roti Prata, 3.5, Rojak, 2.5, Duck Rice, 3, Char Kway Teow, 3.5, Curry Puff, 2, Popiah, 2.5, Wanton Mee, 3.5, Chwee Kueh, 2.5, Ramen, 4
                f = open("menu.txt","w+")
                f.write(input("Please enter your restaurant dishes followed by their prices, seperated by a comma ','\n")) #write menu into .txt file (food, price, food, price)
                f.close()

                f = open("menu.txt", "r")
                menu = f.read() #read from .txt file
                menu = menu.split(sep=", ") #split menu items into list
                print()

                delacc = input("Would you like to delete any accounts? 'y' if yes (ENTER if no) ")
                print()

                if delacc == "y":
                    import csv
                    reader = csv.reader(open('acc.csv')) #open account .csv file

                    users = {} #dictionary for storing user accounts

                    for col in reader:
                        key = col[0] #set key as username
                        users[key] = col[1] 
                    
                    for i in users:
                        print(i, users[i])
                    print()
                    
                    delacc1 = "h"
                    import csv

                    while delacc1 != "s":
                        delacc1 = input("Enter the username of the account you would like to delete or 's' to stop: ")

                        if delacc1 != 's':
                            if delacc1 == "admin": #if you try to delete the admin account
                                print("You cannot delete the admin account.")
                            else:
                                key = delacc1
                                users.pop(key)
                                print(delacc1, "deleted.")
                            
                        w = csv.writer(open("acc.csv", "w", newline=''))
                        for key, val in users.items():
                            w.writerow([key, val]) #writes account info to .csv file
            else:    
                print("Wrong password entered. You will now proceed as a regular user.\n") 
                menu = ['Curry Rice', '3.5', 'Pork Chop', '6', 'Prawn Noodles', '3', 'Salad', '2.8', 'Burger', '5', 'Chicken Rice', '2.5', 'Katsu Curry', '4.5', 'Bak Chor Mee', '3.5', 'Laksa', '4.5', 'Carrot Cake', '3.5', 'Fried Rice', '2.5', 'Chilli Crab', '6.5', 'Chee Chong Fun', '2.5', 'Mee Rebus', '3.5', 'Bak Kut Teh', '6.8', 'Fish & Chips', '4.5', 'Dim Sum', '5.2', 'Oyster Omelette', '5.0', 'Satay', '3.0', 'Nasi Lemak', '3.3', 'Mee Siam', '2.5', 'Roti Prata', '3.5', 'Rojak', '2.5', 'Duck Rice', '3', 'Char Kway Teow', '3.5', 'Curry Puff', '2', 'Popiah', '2.5', 'Wanton Mee', '3.5', 'Chwee Kueh', '2.5', 'Ramen', '4'] #default menu if wrong password
        else:
            menu = ['Curry Rice', '3.5', 'Pork Chop', '6', 'Prawn Noodles', '3', 'Salad', '2.8', 'Burger', '5', 'Chicken Rice', '2.5', 'Katsu Curry', '4.5', 'Bak Chor Mee', '3.5', 'Laksa', '4.5', 'Carrot Cake', '3.5', 'Fried Rice', '2.5', 'Chilli Crab', '6.5', 'Chee Chong Fun', '2.5', 'Mee Rebus', '3.5', 'Bak Kut Teh', '6.8', 'Fish & Chips', '4.5', 'Dim Sum', '5.2', 'Oyster Omelette', '5.0', 'Satay', '3.0', 'Nasi Lemak', '3.3', 'Mee Siam', '2.5', 'Roti Prata', '3.5', 'Rojak', '2.5', 'Duck Rice', '3', 'Char Kway Teow', '3.5', 'Curry Puff', '2', 'Popiah', '2.5', 'Wanton Mee', '3.5', 'Chwee Kueh', '2.5', 'Ramen', '4'] #default menu if regular user
            if user in accounts: #checks if username is in .txt file
                if accounts[user] == passwd: #checks if the password matches 
                    print("Login success!\n")
                    global name 
                    name = user #assign username to variable for user tracking
                else:
                    print("Wrong password.\n") #if password doesn't match the username
            else:
                print("You don't have an account.\n") 
    elif acc == "c": #create new account
        newuser = input("Enter a username: ") #enter new username
        print()
        if newuser == "admin": #if user tries to create a new admin account
            print("You cannot create another admin account.\n")
            menu = ['Curry Rice', '3.5', 'Pork Chop', '6', 'Prawn Noodles', '3', 'Salad', '2.8', 'Burger', '5', 'Chicken Rice', '2.5', 'Katsu Curry', '4.5', 'Bak Chor Mee', '3.5', 'Laksa', '4.5', 'Carrot Cake', '3.5', 'Fried Rice', '2.5', 'Chilli Crab', '6.5', 'Chee Chong Fun', '2.5', 'Mee Rebus', '3.5', 'Bak Kut Teh', '6.8', 'Fish & Chips', '4.5', 'Dim Sum', '5.2', 'Oyster Omelette', '5.0', 'Satay', '3.0', 'Nasi Lemak', '3.3', 'Mee Siam', '2.5', 'Roti Prata', '3.5', 'Rojak', '2.5', 'Duck Rice', '3', 'Char Kway Teow', '3.5', 'Curry Puff', '2', 'Popiah', '2.5', 'Wanton Mee', '3.5', 'Chwee Kueh', '2.5', 'Ramen', '4']
        else:
            newpass = input("Enter a password: ") #enter new password
            print()
            account = newuser + ',' + newpass + '\n' 

            with open('acc.csv', 'a') as f:
                f.write(account) #writes account info to .csv file
            f.close()
            print("Account created successfully!\n")

            name = newuser
            menu = ['Curry Rice', '3.5', 'Pork Chop', '6', 'Prawn Noodles', '3', 'Salad', '2.8', 'Burger', '5', 'Chicken Rice', '2.5', 'Katsu Curry', '4.5', 'Bak Chor Mee', '3.5', 'Laksa', '4.5', 'Carrot Cake', '3.5', 'Fried Rice', '2.5', 'Chilli Crab', '6.5', 'Chee Chong Fun', '2.5', 'Mee Rebus', '3.5', 'Bak Kut Teh', '6.8', 'Fish & Chips', '4.5', 'Dim Sum', '5.2', 'Oyster Omelette', '5.0', 'Satay', '3.0', 'Nasi Lemak', '3.3', 'Mee Siam', '2.5', 'Roti Prata', '3.5', 'Rojak', '2.5', 'Duck Rice', '3', 'Char Kway Teow', '3.5', 'Curry Puff', '2', 'Popiah', '2.5', 'Wanton Mee', '3.5', 'Chwee Kueh', '2.5', 'Ramen', '4']
    else:
        menu = ['Curry Rice', '3.5', 'Pork Chop', '6', 'Prawn Noodles', '3', 'Salad', '2.8', 'Burger', '5', 'Chicken Rice', '2.5', 'Katsu Curry', '4.5', 'Bak Chor Mee', '3.5', 'Laksa', '4.5', 'Carrot Cake', '3.5', 'Fried Rice', '2.5', 'Chilli Crab', '6.5', 'Chee Chong Fun', '2.5', 'Mee Rebus', '3.5', 'Bak Kut Teh', '6.8', 'Fish & Chips', '4.5', 'Dim Sum', '5.2', 'Oyster Omelette', '5.0', 'Satay', '3.0', 'Nasi Lemak', '3.3', 'Mee Siam', '2.5', 'Roti Prata', '3.5', 'Rojak', '2.5', 'Duck Rice', '3', 'Char Kway Teow', '3.5', 'Curry Puff', '2', 'Popiah', '2.5', 'Wanton Mee', '3.5', 'Chwee Kueh', '2.5', 'Ramen', '4'] 
    
    for i in range(len(menu)):
        menu[i] = menu[i].strip() #remove spaces

    foods = [] #food list
    prices = [] #price list

def isFloat(string): #checks if string is a float
    try:
        float(string)
        return True
    except ValueError:
        return False

def sepLists(menu):
    for i in range(len(menu)):
        if isFloat(menu[i]):
            prices.append(menu[i]) #puts prices in prices list
        else:
            foods.append(menu[i]) #puts food items into foods list

    for i in range(len(prices)):
        prices[i] = float(prices[i]) #converts prices list items to float type

def choose():
    global choice
    try:
        choice = int(input("What would you like to do?\n\n1) Display Today's Menu\n\n2) Search Menu\n\n3) Display Cart\n\n4) Check Out\n\nPlease input your choice of action (5 to exit): "))
        print()
    except ValueError:  
        print("Invalid input. Exiting program.")
        choice = 5

orders = [] #order list
total = 0

def orderfood():
    global order
    order = "h"

    while order != 0:
        try:
            order = int(input("Enter the number of the dish you would like to order or 0 to stop: ")) #to order food
            print()
            if order in range(len(foods) + 1):
                if order != 0:
                    orders.append(order)
            else:
                print("Number out of range.")
        except ValueError:
            print("Invalid input. Please enter the number of the dish you would like to order.\n")
        
login()
sepLists(menu)

if 'name' in globals(): #if the user has logged in
    print("Welcome to SPAM,", name)
    print()
else:
    print("Welcome to SPAM!\n")

choose()
while choice != 5: #5 will exit the program
    if choice == 1: #display menu
        print("Menu for today:\n")
        for i in range(len(foods)):
            if (i + 1) <= 9:
                print(str((i + 1)) + ")", "{:<30}".format(foods[i]), "$" + "{:.2f}".format(prices[i]) + "\n") #print the food items and prices
            else:
                print(str((i + 1)) + ")", "{:<29}".format(foods[i]), "$" + "{:.2f}".format(prices[i]) + "\n") 

        orderfood()
        choose()
    elif choice == 2: #search menu
        order = "h"
        count = 0
        search = input("Please enter food to search (case-sensitive): ")
        print()
        searchlist = [] #store index of search results

        while order != 0:
            try:
                for i in range(len(foods)):
                    if search in foods[i]: #checks if the input is in the food list
                        if (i + 1) <= 9:
                            print(str((i + 1)) + ")", "{:<30}".format(foods[i]), "$" + "{:.2f}".format(prices[i]) + "\n") #print the food items and prices that matches teh search
                        else:
                            print(str((i + 1)) + ")", "{:<29}".format(foods[i]), "$" + "{:.2f}".format(prices[i]) + "\n") 
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
                    print(str(i + 1) + ")", "{:<30}".format(foods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") #prints out users orders
                else:
                    print(str(i + 1) + ")", "{:<29}".format(foods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") 

            rmv = input("Would you like to remove any items from your cart? Enter 'y' if yes (ENTER if no): ") #ability to remove items
            print()

            rmv1 = "h"

            if rmv == "y":
                while rmv1 != 0:
                    for i in range(len(orders)):
                        if (i + 1) <= 9:
                            print(str(i + 1) + ")", "{:<30}".format(foods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") #prints out users orders
                        else:
                            print(str(i + 1) + ")", "{:<29}".format(foods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n")

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
                    print(str(i + 1) + ")", "{:<30}".format(foods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") #prints out users orders
                else:
                    print(str(i + 1) + ")", "{:<29}".format(foods[int(orders[i]) - 1]), "$" + "{:.2f}".format(prices[int(orders[i]) - 1]) + "\n") 

            for i in range(len(orders)):
                total += prices[int(orders[i] - 1)] #calculates total 

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

            if 'name' in globals(): #if user is logged in
                print("SPAM members get an additional 10% discount!\n")
                total = 0.9 * total #additional discount if user is a SPAM member.

                print("Thank you for using SPAM,", name)
                print()
            else:
                print("Thank you for using SPAM.\n")
                
            print("Please pay a total of", "$" + str("{:.2f}".format(total) + ".\n")) #prints out total that user has to pay
            break #end of program