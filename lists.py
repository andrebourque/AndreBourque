# # # # List comes in data structures !!.
# # # # Declaring a list in two way
# # # anyname = list()  # right one is the header fiel and the left one is the name
# # # anyname = []  # this represent also a list
# # # anyname.append(2)  # append adds the item  .append(value)
# # # # anyname.append('SHAFAY')
# # # # anyname.append(12.3)
# # # vegetable = ['Carrot', 'ONION', 'GINGER','ONION']
# # # # print(vegetable[1])
# # # # print(vegetable[1:])
# # # # print(vegetable[-1])
# # # # print(vegetable[:])
# # # Form = [['Name', 'Muhammad', 'Shafay', 'Amjad'],
# # # 	   ['He likes to work'],
# # # 	   [12, 34, 12, 55],
# # # 	   ['Shafay', 'Andre'],
# # # 	   ['HAshtqag'],
# # # 	   [10.5]]
# # #
# # # Form[2][2] = "Shafay"
# # # print(Form[2][2])  # listname[rownumber][columnnumber]
# # # print(Form)
# # # #vegetable.remove('Grape')
# # # print(vegetable)
# # #
# # # ## ---------- DICTIONARIES--------- ## keyword ----> meaning or the value
# # # # decleration
# # anyname = dict()  # which represents a dictionary
# # anyname = {}  # curely braces represents the dictionaries.
# # anyname = {'Shafay': 20, 'Andre': 41}  # variable = {key:value, ......}
# # print(anyname['Shafay'])
# # print(anyname['Andre'])
# # anyname = {'City': ['NY', 'WASHINTON DC', 'DELHI', 'ISLAMBAD', 'LONDON']}
# # # {Key : list of values } <--- Key--> City and the list of Values --> complete column
# # print(anyname['City'])
# # print(anyname['City'][1])
# # # ##------------------- FOR LOOPS -------------------## last topic currently <---
# # # to understand lambda --> functions !!!! def name() :  lambda(x) : x in range(0,5)
# #
# # number = 0
# number2 = 1
# list_number = [0, 1, 2, 3, 4, 5]
# sum = 0
# for variablename in range(0, 10):   # range (starting value , ending value ,skiping or step value)
# 	sum = sum + variablename
# print(sum)
# sum = 0
# for variablename in [0,1,2,3,4,5,6,7,8,9]:  # range()---> a list
# 	sum = sum + variablename  # body
# print(sum)
#

# for i in range(0, 5):    # range(0,5)--> [0, 1, 2, 3 , 4 ,5]
# 	print("ith value is ", i)
# 	print("Shafay got candy")
# 	print("Andre sold a candy")
# 	name = "RAFAY"
# 	print(name)
#

# even numbers using the for loop
#
# for i in range(0, 1000):  # range(starting, ending)
# 	if i % 2 == 0:  # this calculates the modulus (reminder of the number i with 2) is its 0 its even
# 		print("even", i)
# range(startingvalue, endingvalue, skippingvalue or stepvalue)
for i in range(1, 1000, 2):  # ---> starting = starting + stepvalue   0+2 , 2+2 , 4+2
	print(i)
