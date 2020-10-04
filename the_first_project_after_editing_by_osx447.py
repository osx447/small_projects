#it is my last project put after editing
#and adding factions and making it more simple
#---------------------------------------------

import time

name = input("what's your name : ")
while True:
	try:
		age = int(input(f"please, enter your age {name} : "))
		break
	except:
		print("enter your age in numbers please")

def joke():
	print("try again later")
	time.sleep(2)
	print("why are you waiting? ")
	print("yeah, for the rest of the program")

joke()


while True:
	if age < 16:
		print(name + " you dont have a passport or id")
		
		dad_fake_id = input("give me your dad id number " + name + " : ")
		
		confirm_id = input("your dad's id " + dad_fake_id + " are you sure? (y-n) ")
		
# now you must confirm the id (i know that the id you will enter is fake :-)

		if confirm_id == "y":
			print("confirmed")
			print("just joking")
			print("bye " + name + ", it was nice to meet you")
			break
		else:
			print("please confirm")
	else:
		fake_id = input("please, give me your id " + name + " : ")
		confirm_your_id = input("your id is " + fake_id + " are you sure (y-n) :")
		if confirm_your_id == "y":
			print("you are being hacked..")
			time.sleep(4)
			print("just joking")
			print("bye " + name + ", is was nice to meet you")
			break
		else:
			print("please confirm")
#---------------------------------
#thats it i hope that is better
#print("bye " + name)
#---------------------------------