#!/usr/bin/python

import os
import sys, traceback


def main():
	try:
		print('''
                        A          PPPPPP      SSSSS
                       A A         P     P    S     S
                      A   A        PPPPPP     S
                     AAAAAAA       P           SSSSS
                    A       A      P                S  
                   A         A     P           SSSSS      v.0.004
		''')
		def inicio1():
			while True:
				print('''
1) APS Members
2) Install Koreans for linux
3) get help

			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
				if opcion0 == "1":
					f = open('APSPe.txt','r')
					s = f.read()
					print(s)
				elif opcion0 == "2":
					print('''
1) First start
2) second start
''')					
					install0 = raw_input("\033[1;32mChoose one > \033[1;m")
					if install0 == "1":	 
 						cmd1 = os.system("apt-get install fonts-nanum*")
						print("install for reboot")
						cmd2 = os.system("sudo reboot")
					elif install0 == "2":
						cmd2 = os.system("apt-get install im-config")
						cmd3 = os.system("im-config")
				if opcion0 == "3":
					f = open('help.txt','r')
					s = f.read()
					print(s)




			inicio1()
		inicio1()
	except KeyboardInterrupt:
		print ("Bye Bye..")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)



if __name__== "__main__":
	main()
