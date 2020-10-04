#it's my first long project
#please tell my if you like it
#made by osx447 with python
#------------------------------

import time

name = input("What's your name : ")
while True:
	try:
		age = int(input("whats your age " + name + " : "))
		break
	except:
		print("enter your age in numbers")

#now i got your name and age lets use them

print("try again later")
time.sleep(2)
print("just kidding")

#just a joke :) 

while True:
	if age < 16:
		print(name + " you dont have a passport or id")
		dad_fake_id = input("give me your dad id number " + name + " : ")
		confirm_id = input("your dad's id " + dad_fake_id + " are you sure? (y-n) ")
		
# now you must confirm the id (i know it is fake :-)

		if confirm_id == "y":
			print("confirmed")
			print("just joking")
			print("bye " + name + ", it was nice to meet you")
			break
		else:
			print("please confirm")
	else:
		fake_id = input("please, give me your id " + name + " : ")
		confirm_your_id = input("your id is" + fake_id + " are you sure (y-n) :")
		if confirm_your_id == "y":
			print("you are being hacked..")
			time.sleep(4)
			print("just joking")
			print("bye " + name + ", is was nice to meet you")
			break
		else:
			print("please confirm")

#you must confirm to break the loop
#and that is it
#i know that *karim* will read the code #then please tell me your opinion
#thanks for reading the code 
#coding it took an hour
#bye
#:-):-):-):-):-):-):-):-):-):-):-):-)


