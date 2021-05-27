'''
Name: Metta Tan
Admin Number: 1904275
Class: 1B/02
'''

import socket                   # Import socket module
def getnewsocket():
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket = getnewsocket()
host = "localhost"
serversocket.bind((host, 8089))
serversocket.listen(5) # become a server socket, maximum 5 pending connections

print('Server is online.')

conn, addr = serversocket.accept()     # Establish connection with client.
print('Got connection from', addr)

import csv
reader = csv.reader(open('acc.csv'))   # Open accounts file
accounts = {} #dictionary for storing user accounts

for col in reader:
   key = col[0] #set key as username
   accounts[key] = col[1] 

choice = conn.recv(4096) # indicates whether the main client or menu editor is sending
choice2 = choice.decode()

if choice2 == "acc": # if trying to login or create account
   data2 = ""

   if data2 != "n":
      while True:
         data = conn.recv(4096)
         data2 = data.decode()
         if data2 != "n":
            if "," not in data2: # if not trying to create acc
               username,password = data2.split(' ')
               if username in accounts: #checks if username is in .txt file
                  if accounts[username] == password: #checks if the password matches 
                     conn.sendall(("Login success!").encode()) 
                     break
                  else:
                     conn.sendall(("Wrong password.").encode()) #if password doesn't match the username
               else:
                  conn.sendall(("You don't have an account.").encode()) #if account doesn't exist
            else:
               newuser,newpass = data2.split(",") # if trying to create account
               if newuser in accounts:
                  conn.sendall(("Username unavailable.").encode()) #if username already exists
               else:
                  with open('acc.csv', 'a') as f: #open account file
                     f.write(data2) # add new account to file
                     conn.sendall(("Account successfully created.").encode())
                     break
         else:
            break

   filename='menu.txt' #menu file
   f = open(filename,'rb')
   l = f.read(4096)
   while (l):
      conn.sendall(l) #send menu file to client
      print('Sent ',repr(l))
      l = f.read(4096)
   f.close()

elif choice2 == "no": #if not logging in or creating account
   filename='menu.txt'
   f = open(filename,'rb')
   l = f.read(4096)
   while (l):
      conn.sendall(l)
      print('Sent ',repr(l))
      l = f.read(4096)
   f.close()

elif choice2 == "menu": # if menu editor client sends
   filename='menu.txt'
   f = open(filename,'rb')
   l = f.read(4096)
   while (l):
      conn.sendall(l)
      print('Sent ',repr(l))
      l = f.read(4096)
   f.close()

   menudata = conn.recv(4096) # receive updated menu data
   newmenu = menudata.decode()

   f = open("menu.txt","w+")
   f.write(newmenu) # replace old menu with new menu
   f.close()

end = conn.recv(4096)
end2 = end.decode()
if end == "end":
   conn.close()
   serversocket.close()
print("Connection closed.\nShutting down.")