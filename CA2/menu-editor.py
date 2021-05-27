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

var = "menu"
sendMessage(var) # tells server that menu editor is sending

data = clientsocket.recv(4096)
data2 = data.decode()
menufile = data2.split(',')

prices = []
foods = []

for i in range(len(menufile)):
    if menufile[i] != '':
        if isFloat(menufile[i]):
            prices.append(menufile[i]) #puts prices in prices list
        else:
            foods.append(menufile[i]) #puts food items into foods list

for i in range(len(prices)):
    prices[i] = float(prices[i]) #converts prices list items to float type

print("Current menu: ")
print("\n")
for i in range(len(foods)):
    if (i + 1) <= 9:
        print(str((i + 1)) + ')', '{:<30}'.format(foods[i]), '$' + '{:.2f}'.format(prices[i]) + '\n') # prints the current menu 
    else:
        print(str((i + 1)) + ')', '{:<29}'.format(foods[i]), '$' + '{:.2f}'.format(prices[i]) + '\n') 
newmenu = input("Please enter your restaurant dishes followed by their prices, seperated by a comma ','\n") # allows admin to update items in the menu
sendMessage(newmenu) # sends updated menu back to server 
end = "end"
sendMessage(end) # closes server
clientsocket.close()