# Yes or No --> and , or , not --> Boolean Expressions !!
name = "Shafay"
mood = "happy"
age = 19
# Boolean --> True or False,
#  True ---> not True ---> False---> not False--> True
if name == "Shafay" or mood == "happy" or age == 20: # or --> any condition True --> Runs its Body
	# name == Shafay--> True
	# mood == Happy --> True
	# age == 20 --> True
	# if True and True and True
	# if True
	print("Shafay is happy and 20 years of age !") # and--> All of them Must be True
if name == "Shafay" and mood == "happy" and age == 20:
	# name == Shafay--> True
	# mood == Happy --> True
	# age == 20 --> True
	# if True and True and True
	# if True
	print("Shafay is happy and 20 years of age !")

if not True:  # the True --> is not False cause of the not statment
	print("This was True")
if not name == "Shafay":  # this is again converted into False
	print("You are  Shafay")