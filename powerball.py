from collections import Counter
import random


def data_update(fname_list,lname_list,favorite_number,freq) :
	""" 
	This function updates the names of the employees,their
	favorite numbers and also a list for frequency counting

	"""
	temp = []
	num = 0
	counter = 1

	#Taking the employee name and checking if it is not blank.
	while 1 :

		fname = raw_input("Enter your first name:")
		lname = raw_input("Enter your last name:")
		
		if fname == "" or lname == "" : 
			print "Enter a valid Name"
			continue

		else :	
			fname_list.append(fname)
			lname_list.append(lname)
			break	

	#Taking in the input for the favorite numbers.
	while counter < 7 :
		try :

			#Slot #1
			if counter==1 :
			
				num = int(raw_input("select 1st # (1 thru 69):"))

			#Slot #2
			elif counter==2 : 
				
				num = int(raw_input("select 2nd # (1 thru 69 excluding "+ str(temp[0]) + "):"))

			#Slot #3
			elif counter==3 : 
							
				num = int(raw_input("select 3rd # (1 thru 69 excluding " + str(temp[0]) + " and "+ str(temp[1]) + "):"))

			#Slot #4
			elif counter==4 : 
							
				num = int(raw_input("select 4th # (1 thru 69 excluding " + str(temp[0]) + ", " + str(temp[1]) + " and " + str(temp[2]) + "):"))

			#Slot #5
			elif counter==5 : 
							
				num = int(raw_input("select 5th # (1 thru 69 excluding " + str(temp[0]) + ", " + str(temp[1]) + ", " + str(temp[2]) + " and " + str(temp[3]) + "):"))

			#Powerball slot
			elif counter==6 :
			
				num = int(raw_input("select Power Ball # (1 thru 26):"))

		#Non integer input
		except ValueError :	
				
				print "Enter Valid Input"
				continue	

		#Powerball number is out of the specified range.
		if (counter==6) and (num < 1 or num > 26) :
				
				print "Enter Powerball No. in range"
				continue	

		#One of the first five numbers is either repeated or out of the specified range.
		if (counter != 6) and ((num < 1 or num > 69) or (num in temp)) :
			
			print "Enter Valid Input, Number out of range or duplicate"
			continue

		freq[counter - 1].append(num)
		counter += 1
		temp.append(num)
		
	#Adding the current employee's favorite number list to the list for all employees.
	favorite_number.append(temp)
	return


def driver() :
	""" 
	This is the driver function that calls the function to update 
	the user data and calculates the Powerball winning number    
	
	"""
	
	#The lists  for the first name, last name and the favorite number for all employees.
	fname_list = [] 
	lname_list = []
	favorite_number = []

	#The list used in calculating the frequency of the numbers at a specific slot. 
	freq = [[] for _ in xrange(6)]

	#The result list containing the Powerball winning number.
	res=[]
	input_choice=""

	# Taking the user inputs until N or n is entered as input.
	while 1 :  
		input_choice = raw_input("Enter employee info? [Y/N] ") 

		# if the user inputs lowercase y or n it would still work.
		if input_choice in ['y','Y']:

			data_update(fname_list,lname_list,favorite_number,freq)

		elif input_choice in ['n','N'] :
			
			break

		else :
			print "Invalid Choice"
			continue		

	n_employees = len(fname_list)
	counter = 0
	print "\n\n"

	#Printing the user names and their favorite numbers to stdout.
	while counter < n_employees :
		print fname_list[counter] + " " + lname_list[counter] + " " + " ".join(map(str,favorite_number[counter][:-1])) + " Powerball: " +  str(favorite_number[counter][5])
		counter += 1

	print " \n\n "

	#If No employee info was entered.
	if n_employees==0:
		print "No Employee Found"

	#Calculating the numbers with max frequency in each slot. If not unique, a random number would be used.
	else : 
		itr = 0
		while itr < 6 :
			count=Counter(freq[itr])

			#There is just one number to choose from in this slot.  
			if len(count)==1 :
				res.append(count.most_common()[0][0])

			#There is no unique number with max frequency.	
			elif count.most_common()[0][1] == count.most_common()[1][1] :
				if itr < 5 :
					res.append(random.randint(1,69))
				else :
					res.append(random.randint(1,26))

			#The number with max frequency is unique. 	
			else :
				res.append(count.most_common()[0][0])

			itr += 1

		#Printing out the winning Powerball number.
		print "Powerball winning number:\n"
		print " ".join(map(str,res[:-1])) + " Powerball: " +  str(res[5])
	
	return		

if __name__ == "__main__":
	"""
	The main function.

	"""
	driver()		
		