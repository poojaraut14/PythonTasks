import math
C = 10
H = 20
Q = []

D = raw_input('Enter Values: ').split(',')

for i in D:
	Q.append(math.sqrt((2*C*int(i)/H)))
# end for
print Q