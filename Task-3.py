# #'''''''''''''''''''''''''''''''''''''Question 4'''''''''''''''''#


# list4=[2,5,10,12,1,45,89,100,3,66,19,300,34,23]
# large=list4[0]
# small=list4[0]
# for i in range(len(list4)):
# 	if(list4[i]>large):
# 		large=list4[i]
# 	elif (list4[i]<small):
# 		small=list4[i]
# 	else:
# 		continue
# print list4
# print large
# print small


# #Using in-built functions

# list4=[2,5,10,12,1,45,89,100,3,66,19,300,34,23]
# small = min(list4)
# large =  max(list4)
# print list4
# print small
# print large


# #'''''''''''''''''''''''''''''''''''''Question 5'''''''''''''''''#


old=[1,2,3,5,7,8,10,12,13]
print 'List is: ', old
for i in old:
	print i
	if(i%2 == 0):
		print i
		old.remove(i)

print 'List after removing even numbers is: ', old



# #'''''''''''''''''''''''''''''''''''''Question 6'''''''''''''''''#


# list1=[]
# for i in range(1,31):
# 	if(i<6 or i>25):
# 		list1.append(i*i)
# 	else:
# 		list1.append(i)

# print 'Square of first five elements of list are: ',list1[:5]
# print 'Square of last five elemeents of list are: ',list1[-5:]



# #From internet (little different algo)
# # l = list()
# # for i in range(1,21):
# # 	l.append(i**2)
# # print l[:5]
# # print l[-5:]
# # print l



# #'''''''''''''''''''''''''''''''''''''Question 7'''''''''''''''''#



# list1 = [10,20,30,40,50]
# list2 = [60,70,80,90]
# print 'List 1 is: ', list1
# print 'List 2 is: ', list2
# list1.pop()
# for i in list2:
# 	list1.append(i)
# print 'Result list is: ',list1



# #Another method: using slicing

# list1 = [10,20,30,40,50]
# list2 = [60,70,80,90]
# print 'List 1 is: ', list1
# print 'List 2 is: ', list2
# list1 = list1[:-1] + list2
# print 'Result list is: ',list1



# #'''''''''''''''''''''''''''''''''''''Question 9'''''''''''''''''#


# num=input('Enter value of n: ')
# res={}
# for i in range(1,num+1):
# 	res[i]=i*i
# print res



# #'''''''''''''''''''''''''''''''''''''Question 10'''''''''''''''''#

# value=raw_input('Enter sequence of comma sepearated numbers: ')

# list1=value.split(",")
# tuple1=tuple(list1)

# print 'List is: ', list1
# print 'Tuple is: ', tuple1


