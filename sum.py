n = 20
print type(n)
x = 0
sum = 0
j=0
for i in range (0,n):
	
	sum = sum+ i+1 
	print sum
	if 2**j < sum and sum <= 2**(j+1):
		x=j+1
		print x
	else:
		j=j+1
print x
