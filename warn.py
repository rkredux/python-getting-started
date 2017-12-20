
#Understanding the logging in Python
#Various levels of logging in Python
#critical
#error
#warning
#info
#debug 


#warning is an inbuilt logging module
import logging

#We added time logging in our log messages. 
logging.basicConfig(filename ='./warn.py', level = logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s")


#There are different levels of logging that are 
#really possible with this and going forward it will 
#be important to keep them in mind


for i in range(0, 100): 

	if i % 5 == 0:
		logging.debug("Found a number divisible by 5: {0}".format(i))
	elif i % 4 == 0: 
		logging.warning("Found a number divisible by 4: {0}".format(i))
	else: 
		logging.info("At number {0}".format(i))

logging.warning("Finished Sequence")

