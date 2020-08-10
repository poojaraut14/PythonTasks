# #'''''''''''''''''''''''''''''''''''''''''Question 2'''''''''''''''''''''#


# def case_check(str1):
# 	upper_count=0
# 	lower_count=0
# 	for i in str1:
# 		if i.isupper():
# 			upper_count+=1
# 		elif i.islower():
# 			lower_count+=1
# 		else: continue
# 	return upper_count,lower_count	

# str1=raw_input('Enter a string value: ')

# upper_count, lower_count = case_check(str1)
# print 'No.of Upper case characters: ',upper_count
# print 'No.of Lower case characters: ',lower_count


# #'''''''''''''''''''''''''''''''''''''''''Question 3'''''''''''''''''''''#


def get_unique_elements(input_list):
	temp_dict={}
	for i in input_list:
		if i in temp_dict:
			temp_dict[i]+=1
		else:
			temp_dict[i]=1
	for key in temp_dict:
		if temp_dict[key]==1:
			output_list.append(key)
	return output_list


input_list=['a','b','c','a','b','ab','uy','c','uy','z']
output_list=[]
print '\nThe Original list is: ',input_list
output_list=get_unique_elements(input_list)
print '\nThe list with unique elements is: ',output_list


# #'''''''''''''''''''''''''''''''''''''''''Question 4'''''''''''''''''''''#


# input_string=raw_input('Enter hyphen-separated sequence of words: ')

# words=input_string.split('-')

# words.sort()

# output_string=''
# for i in range(len(words)):
# 	if i!=len(words)-1:
# 		output_string=output_string+words[i]+'-'
# 	else:
# 		output_string+=words[i]

# print 'Alphabetically sorted hyphen-separated sequence of words is: ',output_string


# #'''''''''''''''''''''''''''''''''''''''''Question 5'''''''''''''''''''''#


# input_lines=[]
# print 'Enter sequence of lines: '
# while True:
# 	line1=raw_input()
# 	if line1:
# 		input_lines.append(line1)
# 	else: break
# for i in range(len(input_lines)):
# 	input_lines[i]=input_lines[i].upper()
# 	print input_lines[i]


# #'''''''''''''''''''''''''''''''''''''''''Question 6'''''''''''''''''''''#


# def print_sum(str1,str2):

# 	num1=int(str1)
# 	num2=int(str2)

# 	sum_value=num1+num2
# 	print 'The sum is: ',sum_value


# str1=raw_input("Enter 1st number: ")
# str2=raw_input("Enter 2nds number: ")

# print_sum(str1,str2)


# #'''''''''''''''''''''''''''''''''''''''''Question 7'''''''''''''''''''''#


# def print_max_length_string(string1,string2):
# 	if len(string1)==len(string2):
# 		print 'Both strings have equal length'
# 		print string1
# 		print string2
# 	elif len(string1) > len(string2):
# 		print '\nString with maximum length is: ',string1
# 	else:
# 		print '\nString with maximum length is: ',string2


# str1=raw_input("Enter string 1:")
# str2=raw_input("Enter string 2:")
# print_max_length_string(str1,str2)



# #'''''''''''''''''''''''''''''''''''''''''Question 8'''''''''''''''''''''#


# def print_square_value_tuple():
# 	list_square=[]
# 	for i in range(1,21):
# 		list_square.append(i**2)
# 	tuple_square=tuple(list_square)
# 	print tuple_square

# print_square_value_tuple()


# #'''''''''''''''''''''''''''''''''''''''''Question 9'''''''''''''''''''''#


# def showNumbers(limit):
# 	for i in range(limit+1):
# 		if (i%2 == 0):
# 			print i, 'EVEN'
# 		else:
# 			print i, 'ODD'

# limit_input=input('Enter the limit value:')
# showNumbers(limit_input)


# #'''''''''''''''''''''''''''''''''''''''''Question 10'''''''''''''''''''''#


# def even_odd(num):
# 	if num%2 == 0:
# 		return True
# 	else:
# 		return False

# input_list=[]
# for i in range(1,21):
# 	input_list.append(i)

# output_list=filter(even_odd, input_list)

# print 'List with even numbers between 1 and 20 is:', output_list


# #'''''''''''''''''''''''''''''''''''''''''Question 11'''''''''''''''''''''#


# input_list=[1,2,3,4,5,6,7,8,9,10]
# even_numbers=filter(lambda x: x%2 == 0, input_list)

# map_list=map(lambda x: x**2,even_numbers)
# print map_list


# #'''''''''''''''''''''''''''''''''''''''''Question 12'''''''''''''''''''''#


# def divide_func(num,den):

# 	try:
# 		res=num/den
# 		print 'Result is: ',res
# 	except:
# 		print 'Denominator cannot be zero.'

# num1=input('enter numerator:')
# num2=input('enter denominator')
# divide_func(num1,num2)

# #'''''''''''''''''''''''''''''''''''''''''Question 13'''''''''''''''''''''#


# import functools

# input_list=[[1,2,3],[4,5,6],[7,8]]
# print '\nInput list is:',input_list

# result=reduce(lambda x,y: x+y, input_list)
# print '\nFlattened list is: ',result


# #'''''''''''''''''''''''''''''''''''''''''Question 14'''''''''''''''''''''#

# #Question and Answer (avoid)

# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print k



# def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()


