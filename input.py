#This file just sets up a chat from command line. 


name = input("Name: ")
job = input("Occupation: ")
location = input("Location: ")


print("Hi {0}, working as a {1} in {2} must be exciting".format(name, job, location))

res = input("Y for Yes and N or No: ")

if res == "Y": 
	print("Yeah thought so")
elif res == "N": 
	print("Oh I am sorry to hear that you are not having fun")
	followup = input("What else would you be doing: ")
	print("Oh yeah, being a {0} in {1} would be better I guess. Well Good luck!".format(followup, location))




