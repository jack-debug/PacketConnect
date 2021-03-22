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

k = random.randint(1,2000)
cipher_suite = Fernet(k)
clearConsole()
print('Welcome to PacketConnect')
contact_code = input('Please enter a unique identifying code. You use this code to chat with others via PacketConnect: ')
print('Your contact code is ' + contact_code)
com = input('If you want to send a packet, type "send", if you want to wait to recieve a pack type "listen"\n')
if com == 'send':
	dest_code = input('Enter the contact code of the person you wish to talk to: ')
	dest_ip = input('Enter the IP address of the person that you are contacting via PacketConnect (if you are both on the same network enter the number 1): ')
	my_ip = urlopen('http://ip.42.pl/raw').read()
	my__ip = my_ip.replace("'","")
	my__ip = my__ip.replace("b","")
	if dest_ip == '1':
		print('Connecting to ' + dest_code + ' at ' + my__ip + '...')
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
		s.connect(my__ip, 80)
		print('Established socket to ' + my__ip + 'at port 80.')
		msg = input('Please type a message to send.\n')
		msg = cipher_suite.encrypt(msg) + '|' + dest_code + '|' + contact_code + '|' + k
		print('Sending packet')
		s.send(msg.encode('utf-8'))
		print('Packet sent, listening for reply...')
	else:
		print('Connecting to ' + dest_code + ' at ' + dest_ip + '...')
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
		print('Established socket to ' + dest_ip + 'at port 80.')
		msg = input('Please type a message to send.\n')
		msg = msg + ' ' + dest_code + ' ' + contact_code
		print('Sending packet')
		i = 1
		while i != 10:
			s.sendto(msg.encode('utf-8'), (dest_ip, 80))
			i = i + 1
		print('Packet sent, listening for reply...')
		replied = bool(0)
		while replied = bool(0):
			pacRec = s.recvfrom(65536)
			if contact_code in pacRec:
				print('Recieved packet!')
				replied = bool(1)
				packetData = pacRec.split('|',4)
				decryptedMsg = cipher_suite.decrypt(packetData[0])
				print(packetData[2] + ': ' + decryptedMsg)
				

elif com == 'listen':
	print('### LISTENING FOR PACKETS ###')
	
# sep = '.'
# key2 = dest_ip.split(sep, 1)[0]
# encrypKey = Encryption(str(k),key2)
