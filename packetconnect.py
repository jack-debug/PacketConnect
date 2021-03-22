import socket
import pickle, rehash
import sys
from urllib.request import urlopen
import os
from cryptography.fernet import Fernet
import random
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def sendReply(contactCode, destCode, s):
    msgUn = input('Reply: ')
    print ("\033[A                             \033[A")
    encryptionKey = Fernet(Fernet.generate_key())
    msg = encryptionKey.encrypt(msgU) + '|' + destCode + '|' + contactCode + '|' + encryptionKey
    s.send(msg.encode('utf-8'))

k = random.randint(1,2000)
clearConsole()
print('Welcome to PacketConnect')
contact_code = input('Please enter a unique identifying code. You use this code to chat with others via PacketConnect: ')
print('Your contact code is ' + contact_code)
com = input('If you want to send a packet, type "send", if you want to wait to recieve a pack type "listen"\n')
if com == 'send':
	dest_code = input('Enter the contact code of the person you wish to talk to: ')
	dest_ip = input('Enter the IP address of the person that you are contacting via PacketConnect (if you are both on the same network enter the number 1): ')
	my_ip = urlopen('http://ip.42.pl/raw').read() # gets users ip address
	my__ip = my_ip.replace("'","")
	my__ip = my__ip.replace("b","")
	if dest_ip == '1':
		print('Connecting to ' + dest_code + ' at ' + my__ip + '...')
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
		s.connect(my__ip, 80)
		print('Established socket to ' + my__ip + 'at port 80.')
		msgU = input('Please type a message to send.\n')
        print('Sending packet and starting conversation...')
        clearConsole()
        print('Conversation with ' + dest_code + ' started.')
        loopConv= bool(1)
        encryptionKey = Fernet(Fernet.generate_key())
        msg = encryptionKey.encrypt(msgU) + '|' + dest_code + '|' + contact_code + '|' + encryptionKey
        s.send(msg.encode('utf-8'))
        print(contact_code + ': ' + msgU)
		while loopConv = bool(1):
            replied = bool(0)
		    while replied = bool(0):
			    pacRec = s.recvfrom(65536) #receives packet
			    if contact_code in pacRec: # checks if packet has the contact code of the user, if not it listens for another packet
				    replied = bool(1)
				    packetData = pacRec.split('|',4) # splits packet into array
				    decryptionKey = Fernet(packetData[3]) # gets decryption code
				    decryptedMsg = decryptionKey.decrypt(packetData[0]) # decrypts the message
				    print(packetData[2] + ': ' + decryptedMsg)
                    sendReply(contact_code, dest_code, s)
	else:
		print('Connecting to ' + dest_code + ' at ' + dest_ip + '...')
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
		s.connect(dest_ip, 80)
		print('Established socket to ' + my__ip + 'at port 80.')
		msg = input('Please type a message to send.\n')
		encryptionKey = Fernet(Fernet.generate_key())
		msg = encryptionKey.encrypt(msg) + '|' + dest_code + '|' + contact_code + '|' + encryptionKey
		print('Sending packet')
		s.send(msg.encode('utf-8'))
		print('Packet sent, listening for reply...')
		replied = bool(0)
		while replied = bool(0):
			pacRec = s.recvfrom(65536) #receives packet
			if contact_code in pacRec: # checks if packet has the contact code of the user, if not it listens for another packet
				print('Recieved packet!')
				replied = bool(1)
				packetData = pacRec.split('|',4) # splits packet into array
				decryptionKey = Fernet(packetData[3]) # gets decryption code
				decryptedMsg = decryptionKey.decrypt(packetData[0]) # decrypts the message
				print(packetData[2] + ': ' + decryptedMsg)

elif com == 'listen':
	print('### LISTENING FOR PACKETS ###')