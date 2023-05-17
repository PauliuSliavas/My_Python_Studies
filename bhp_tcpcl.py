##############################################################
############################################################## 
###      ____  _                                           ###
##      / ___|| |_   ___   _____  _ __   ___ __ _ ___       ##
##      \___ \| | | | \ \ / / _ \| '_ \ / __/ _` / __|      ##
##       ___) | | |_| |\ V / (_) | | | | (_| (_| \__ \      ##
##      |____/|_|\__, | \_/ \___/|_| |_|\___\__,_|___/      ##
##               |___/                                      ##
###                                                        ###
##############################################################
##############################################################

# This TCP CLIENT is based on Justin Seitz and Tim Arnold book Black Hat Python 2nd edition for Pyhon3.
# As I go along the book, I will try to share the code thats in the book, will try to add explanation. 

import socket 

target_host = "www.google.com"
target_port = 443

#Create a socket object [tiesiog sukuriamas socket objektas]
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the client
client.connect((target_host,target_port))

#Send some data
client.send(b'GET / HTTP/1.1\r\n\Host: google.com\r\n\r\n')

#Receyve some data
response = client.recv(4096)

print(response.decode())
client.close()