import random
from os import sys
def osama():

	x = random.randint(0, 10)
	y = random.randint(0, 10)
	while (y == x) :
		y = random.randint(0,10)
		pass
	z = random.randint(0,10)
	while (z == x) or (z == y) :
		z = random.randint(0,10)
		pass
	mylist = [x,y,z]
	print("this list is just shown to check the game <3")
	print( mylist)
	print ("enter a no. from 1 to 10 : ")
	k = int(input())	
	print ("enter another no. from 1 to 10 : ")
	l = int(input())
	while (k==l):
		print ("different no. please XD : ")
		l = int(input())
		pass
	print ("enter another no. from 1 to 10 : ")	
	m = int(input())
	while (m==k) or (m==l):
		print("are u kiddin' me ? !! different no. plz XD : ")
		m = int(input())
		pass
	hislist = [k,l,m]

	if mylist == hislist :
		print ("CONGRATULATIONS, YOU WON !! ")
		sys.exit(0)
		pass

	if (x==k) or (y==l) or (z==m):
		print("MATCH !")
		sys.exit(0)
		pass	

	if (k in set(mylist)) or (l in set(mylist)) or (m in set(mylist)):
		print("CLOSE ! ")
		sys.exit(0)
		pass

	if (k not in set(mylist)) or (l not in set(mylist)) or (m not in set(mylist)) :
		print("Opps, u lost :(")
		pass		
	print("Do you want to complete? 'type yes or no'")
	a = "yes"
	b = "no"
	c = input()
	if c == a :
		print ("okaay")
		osama()

		pass
	if c == b :
		sys.exit(0)

		pass	
	
osama()
