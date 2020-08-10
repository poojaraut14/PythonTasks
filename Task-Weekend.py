# #'''''''''''''''''''''''''''''''''''''''''''''''''''Question 6'''''''''''''''''''#


# input_list=list(range(1,101))

# print 'Numbers that are divisible by 3 and a multiple of 2 are: '

# for i in input_list:
# 	if(i%3==0) and (i%2==0):
# 		print i



# #'''''''''''''''''''''''''''''''''''''''''''''''''''Question 7'''''''''''''''''''#


# input_string=raw_input('Enter a string: ')
# print '\nThe string entered is:', input_string

# input_list=list(input_string)

# reverse_str=input_list[::-1]

# vowel=['a','e','i','o','u']

# for i in range(len(reverse_str)):
# 	for j in vowel:
# 		if reverse_str[i]==j:
# 			print '\nVowel', reverse_str[i], 'is found in the reverse string at index:', i



# #'''''''''''''''''''''''''''''''''''''''''''''''''''Question 8'''''''''''''''''''#


# value='hello my name is Abcde'

# value_str=value.split(" ")

# for word in value_str:
# 	if len(word)%2 == 0:
# 		print (word)



# #'''''''''''''''''''''''''''''''''''''''''''''''''''Question 9'''''''''''''''''''#


# input_value=[1,2,3,4,5,6,7,8,9,-1]

# print 'The inputed numbers are: ',input_value
# print 'The pair of numbers whose sum is 8 are:'
# for i in range(0,len(input_value)):
# 	for j in range(i+1,len(input_value)):
# 		if input_value[i]+input_value[j]==8:
# 			print input_value[i],input_value[j]



# #'''''''''''''''''''''''''''''''''''''''''''''''''''Question 10'''''''''''''''''''#


# even_list=[]
# odd_list=[]
# while True:
# 	value=input('Enter number between 1-50:')
# 	if len(even_list)<5 or len(odd_list)<5:
# 		if value%2 == 0:
# 			even_list.append(value)
# 		else:
# 			odd_list.append(value)

# 	else:
# 		print '\nCannot enter anymore numbers in list.'
# 		print '\nList of odd numbers is: ',odd_list
# 		print '\nSum of odd numbers is:',sum(odd_list)
# 		print '\nMaximum number from the odd number list is:',max(odd_list)
# 		print '\nList of even numbers is: ',even_list
# 		print '\nSum of even numbers is:',sum(even_list)
# 		print '\nMaximum number from the even number list is:',max(even_list)
# 		break


# #'''''''''''''''''''''''''''''''''''''''''''''''''''Question 11'''''''''''''''''''#


# input_val=raw_input('Enter alphanumeric value: ')
# temp_dict={}

# for i in input_val:
# 	if i.isdigit():
# 		continue
# 	else:
# 		if i in temp_dict:
# 			temp_dict[i]+=1
# 		else:
# 			temp_dict[i]=1
# print 'The occurences of specific letters are: ',temp_dict


# #'''''''''''''''''''''''''''''''''''''''''''''''''''Question 12'''''''''''''''''''#

# input_tuple=(1,2,3,4,5,6,7,8,9,10)
# list1=[]
# for i in input_tuple:
# 	if i%2 == 0:
# 		list1.append(i)
# output_tuple=tuple(list1)
# print 'Even numbers tuple is: ',output_tuple

