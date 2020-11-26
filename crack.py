#!/usr/bin/python3
import hashlib
import time
from hashlib import md5
import sys
import os
from termcolor import colored


try:

	def banner():
		print(""" 


		 _______  _______  _______  _______  _           _______          
		(  ____ \(  ____ )(  ___  )(  ____ \| \    /\   (  ____ )|\     /|
		| (    \/| (    )|| (   ) || (    \/|  \  / /   | (    )|( \   / )
		| |      | (____)|| (___) || |      |  (_/ /    | (____)| \ (_) / 
		| |      |     __)|  ___  || |      |   _ (     |  _____)  \   /  
		| |      | (\ (   | (   ) || |      |  ( \ \    | (         ) (   
		| (____/\| ) \ \__| )   ( || (____/\|  /  \ \ _ | )         | |   
		(_______/|/   \__/|/     \|(_______/|_/    \/(_)|/          \_/   
                                                                  """)
		print(colored("									By Anant\n","red",attrs=['bold','reverse']))

	def for_md5():
		print("\n")
		
		wordlis=input("Enter path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter your hash: ")
			print('\n')
		
			for password in wordlist:
				if hassh == hashlib.md5(str(password).encode('utf-8')).hexdigest():

					print('\n')
					print(colored("			[*] Cracked: " + password,"yellow",attrs=['bold','reverse']))
					sys.exit(1)



	def for_SHA1():
		wordlis=input("Enter path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter your hash: ")
			print('\n')
		
			for password in wordlist:
				if hassh == hashlib.sha1(str(password).encode('utf-8')).hexdigest():

					print('\n')
					print(colored("			[*] Cracked: " + password,"yellow",attrs=['bold','reverse']))
					sys.exit(1)



	def for_SHA256():
		wordlis=input("Enter path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter your hash: ")
			print('\n')
		
			for password in wordlist:
				if hassh == hashlib.sha256(str(password).encode('utf-8')).hexdigest():

					print('\n')
					print(colored("			[*] Cracked: " + password,"yellow",attrs=['bold','reverse']))
					sys.exit(1)

	def for_SHA512():
		wordlis=input("Enter path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter your hash: ")
			print('\n')
		
			for password in wordlist:
				if hassh == hashlib.sha512(str(password).encode('utf-8')).hexdigest():

					print('\n')
					print(colored("			[*] Cracked: " + password,"yellow",attrs=['bold','reverse']))
					sys.exit(1)
		

	def for_SHA224():
		wordlis=input("Enter path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter your hash: ")
			print('\n')
		
			for password in wordlist:
				if hassh == hashlib.sha224(str(password).encode('utf-8')).hexdigest():

					print('\n')
					print(colored("			[*] Cracked: " + password,"yellow",attrs=['bold','reverse']))
					sys.exit(1)
		



	if __name__ == "__main__":
		os.system('clear')
		#os.system('cls') 	 # for windows
		
		banner()

		print(colored("[1] For md5","yellow",attrs=['bold']))
		print(colored("[2] For SHA1","yellow",attrs=['bold']))
		print(colored("[3] For SHA256","yellow",attrs=['bold']))
		print(colored("[4] For SHA512","yellow",attrs=['bold']))
		print(colored("[5] For SHA224","yellow",attrs=['bold']))
		#print(colored("[6] For Identify Type of Hash","yellow",attrs=['bold']))
		print('\n')

		select = int(input("Enter your choice: "))

		if select == 1:
			for_md5()
		if select == 2:
			for_SHA1()
		if select == 3:
			for_SHA256()
		if select == 4:
			for_SHA512()
		if select == 5:
			for_SHA224()

except KeyboardInterrupt:
	print(colored("\n\n Stop By User!\n","red",attrs=['blink','bold','reverse']))
