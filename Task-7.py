##''''''''''''''''''''''''''''''Question 1''''''''''''''''''''''''''''''

import math 
C = 50
H = 30
Q = []

D=raw_input('Enter values:').split(',')

for i in D:
	Q.append(math.sqrt((2*C*int(i)/H)))
print 'The Result is: ',Q



##'''''''''''''''''''''''''Question 2''''''''''''''''''''''''''''''''''

class shape():
	def area(self, area_shape=0):
		self.area_shape = area_shape
		print 'The area of shape is: ',self.area_shape


class square(shape):
	def __init__(self, len):
		self.len=len
	def area(self, area_square=0):
		self.area_square=area_square
		self.area_square=self.len**2
		print 'The area of square is: ',self.area_square

val1=shape()
val1.area()
val2=square(4)
val2.area()

##''''''''''''''''''''''''''''''Question 3'''''''''''''''''''''''''''

class solution:
 def three_sum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(solution().three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))


##''''''''''''''''''''''''''''Question 5'''''''''''''''''''''''''''''''''''


class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
def add_time(t1, t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes

    if sum.minutes >= 60:
        sum.minutes = sum.minutes - 60
        sum.hours = sum.hours + 1

    return sum

def display_time(self):
        print self.hours,'hr' ,self.minutes, 'min'

def display_minute(self):
   print (self.hours*60)+self.minutes,'minutes'

current_time = Time(2, 50)
bread_time = Time(1, 20)
done_time = add_time(current_time, bread_time)
display_time(done_time)
display_minute(done_time)

###''''''''''''''''''''''''''''Question 6'''''''''''''''''''''''''''''''''''

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = age
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age <= 0:
            age is 0
            print "Age is not valid, setting age to 0"

        elif age < 13:
            print "You are young."

        elif 13 <= age < 18:
            print "You are teenager."

        else:
            print "You are old."
    def yearPasses(self):    
        return age+1

ob1 = int(input())
for i in range(0, ob1):
    age = int(input())         
    person_ob = Person(age)  
    person_ob.amIOld()
    for j in range(0, 3):
        person_ob.yearPasses()       
    person_ob.amIOld()
    print ""
