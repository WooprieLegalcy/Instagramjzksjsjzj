import os
import requests
import random
import webbrowser
import requests
import os
import sys
import time
import random
import time, os,sys
from time import sleep
import requests
import uuid
import sys
import os
from random import *
import colorama 
from colorama import *
import time 
import string 
from user_agent import generate_user_agent
import random
import pyfiglet
import webbrowser
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
ani = sys.platform
os.system('clear')
os.system('rm -rf email.txt')
E = '\033[1;97m'
A = '\033[1;91m'
Q = '\033[1;93m'
G = '\033[1;32m'
W = '\033[1;95m'
def mouad(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(5. / 700)
def error():
	while True:
		print('')		
		print('خطا في لمعلومات')
		print('error !! ')
		

	webbrowser.open('https://t.me/rolexstore01')
	# = = = = = = = = = = = =
IQ = pyfiglet.figlet_format("İRON")
print(B+IQ+'\n'+C+"━"*35)


id = input(' [+] ID GİR : ')
bot = input(' [+] BOT TOKEN : ')
while True:
	usr = '1234567890'
	hrf = '201234567'
	us =  str(''.join((random.choice(usr) for i in range(16)))) 
	uf = str(''.join((random.choice(usr) for i in range(2))))
	uk = str(''.join((random.choice(hrf) for i in range(1))))
	uki = str("/")
	uk1 = '202' + uk
	wi = str(''.join((random.choice(hrf) for i in range(3))))
	print(us+ '|' +uf+ '|' + wi+ '|' + uk1)
	
	with open('MOUAD visa.txt', 'a') as x:
                	x.write(us+uki+uf+uki+uk1+uki+wi+uki+ '\n')
                	
	t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=● YENİ Visa Card ✅ . \n-----------------------------------------------•\n{us} | {uf} | {uk1} | {wi}\n-----------------------------------------------• \n𝗕𝗲 : @exsvip")
