'''
number = input("Enter the number here!")  # = input()  # complete this line , take input here by user instead of fixed input
if number % 2 == 0:  # if the number reminder is 0 when divided by 2 then it is even e.g 4%2 comes out to be 0 cause 2*2 = 4 so 4-4 = 0
	print("The number %d is even" % number)  # this is the replacment operators used here
else:
	print("The number %d is odd" % number)  # here write the statement to print out that the number is odd using the replacment operator

'''
# Q1) Does both block executes of if else or the one ? Yes or No and which one ?
number = int(input("Enter the number here : "))  # we are converting string into integer
if number % 2 == 0:  # both will be checked
	print('Its even')
if number % 2 == 1:
	print("this is odd")
