def collatz(number):
	#Check even vs odd
	if number % 2 == 0:
		return number//2
	return number*3+1
#get that number	
print ("Gimme that number so's I can make it 1")

#Make sure the input is actually a number
while True:
	try:
		number = int(input())
		break
	except ValueError:
		print ("Do better")

#Run it till it's 1
while number !=1:
	number=collatz(number)
	print (number)
print ("Told ya I'd make it 1")