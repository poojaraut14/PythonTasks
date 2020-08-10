# #'''''''''''''''''''''''''''''Question 1''''''#

# #Code for Q1

# num = input('Enter a number: ')
# if(num != 0):    
#     if ((num % 3 == 0) and (num % 5 == 0)): 
#         print 'Consultadd Python Training'
#     elif num % 5 == 0:
#         print 'c'
#     elif num % 3 == 0:
#         print 'Consultadd'
#     else: 
#         print 'Number is not divisible by 3 or 5'
# else: 
#     print ' Enter value greater than zero. '


# #'''''''''''''''''''''''''''''''Question 2''''''#

# print 'Please select option: \n 1. Addition \n 2. Subtraction \n 3. Division \n 4. Multiplication \n 5. Average'
# choice = input('Enter your choice number: ')

# if (choice == 1):
# 	num1 = input('Enter 1st number: ')
# 	num2 = input('Enter 2nd number: ')
# 	result = num1 + num2
# 	if (result>0):
# 		print 'The addition is: ', result
# 	else: 
# 		print 'Zsa'
# elif (choice == 2):
# 	num1 = input('Enter 1st number: ')
# 	num2 = input('Enter 2nd number: ')
# 	result = num1 - num2
# 	if (result>0):
# 		print 'The difference is: ', result
# 	else: 
# 		print 'Zsa'
# elif (choice == 3):
# 	num1 = input('Enter 1st number: ')
# 	num2 = input('Enter 2nd number: ')
# 	result = num1 / num2
# 	if (result>0):
# 		print 'The result is: ', result
# 	else: 
# 		print 'Zsa'
# elif (choice == 4):
# 	num1 = input('Enter 1st number: ')
# 	num2 = input('Enter 2nd number: ')
# 	result = num1 * num2
# 	if (result>0):
# 		print 'The product is: ', result
# 	else: 
# 		print 'Zsa'
# elif (choice == 5):
# 	num1 = input('Enter 1st number: ')
# 	num2 = input('Enter 2nd number: ')
# 	num3 = input('Enter 3rd number: ')
# 	num4 = input('Enter 4th number: ')
# 	result = (num1 + num2 + num3 + num4)/4
# 	if (result>0):
# 		print 'The average is: ', result
# 	else: 
# 		print 'Zsa'



# #''''''''''''''''''''''''''''''''''Question 3''''''#


# age = input('Enter age: ')
# if(age >= 11):
# 	print 'You are eligible to see the Football match.'
# 	if (age <= 20) or (age >= 60):
# 		print ' Ticket price is $12.'
# 	else:
# 		print 'Ticket price is $20.'
# else:
# 	print " You're not eligible to buy a ticket."



# #'''''''''''''''''''''''''''''''''''Question 4''''''#


# while 1:
# 	num = input('Enter a number: ')
# 	if (num < 0 ):
# 		break	
# 	else:
# 		print "Good going"
# 		continue
# print "It's over"



# #'''''''''''''''''''''''''''''''''''Question 5''''''#


# for i in range(2000, 3201):
# 	if (i%7 == 0) and (i%5 != 0):
# 		print i



# #'''''''''''''''''''''''''''''''''''Question 6''''''#

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
# 	print 'error'



# #'''''''''''''''''''''''''''''''''''Question 7''''''#

# for i in range(0,7):
# 	if(i==3) or (i==6):
# 		continue
# 	print i
# 	i+=1


# #'''''''''''''''''''''''''''''''''''Question 8''''''#

# string1=raw_input('Enter a string: ')
# count_letter = 0
# count_digit = 0
# for i in string1:
# 	if(i.isdigit()):
# 		count_digit = count_digit+1
# 	else:
# 		count_letter = count_letter+1
# print 'Letters: ',count_letter
# print 'Digits: ',count_digit



# #'''''''''''''''''''''''''''''''''''Question 9''''''#

# lucky_number = 14
# while True:
# 	number=input('Guess the lucky number: ')
# 	if(number == lucky_number):
# 		break
# 	else:
# 		answer = raw_input('Do you want to guess again (yes/no)? ')
# 		if answer=='no':
# 			break



# #'''''''''''''''''''''''''''''''''''Question 10''''''#

# lucky_number = 14
# counter=1
# while counter<=5:
# 	print 'Type in the ', counter, 'number'
# 	number=input()
# 	if(number == lucky_number):
# 		print 'Good guess!'
# 	else:
# 		print 'Try again!'
# 	counter+=1
# print 'Game over!'
	


#'''''''''''''''''''''''''''''''''''Question 11''''''#

lucky_number = 14
counter=1
while counter<=5:
	print 'Type in the ', counter, 'number'
	number=input()
	if(number == lucky_number):
		print 'Good guess!'
		break
	else:
		print 'Try again!'
	counter+=1
if(counter==6):
	print 'Sorry but that was not very successful!'
	

