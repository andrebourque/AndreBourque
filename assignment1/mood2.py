mood = input('Enter the mood of yours (angry,sad,happy,excited)')  # we are taking an input in the form of a string
"""
if mood == "angry":  # check the value of the variable mood if the value is angry compares that with angry
	print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
	print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)
if mood == "happy":  # ANGRY
	print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
	print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)
if mood == "sad":
	print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
	print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)
if mood == "excited":
	print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
	print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)
"""
# if else statment used for multiple checking ---> (nested if-else condition)
if mood == "angry":  # check the value of the variable mood if the value is angry compares that with angry
	print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
	print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)
else:  # if the mood is not angry
	if mood == "sad":  # check the value of the variable mood if the value is angry compares that with angry
		print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
		print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)
	else:  # if the mood is not angry and the mood is not sad
		if mood == "happy":  # check the value of the variable mood if the value is angry compares that with angry
			print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
			print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)
		else:  # if the mood is not angry nor the mood is sad nor the mood is happy -->
			if mood == "excited":  # check the value of the variable mood if the value is angry compares that with angry
				print("Your %s" % mood)  # the variable mood value is then replaced in the place of %s
				print("Your mood is %s" % mood)  # using the replacement operator (string %s <-- mood(angry)