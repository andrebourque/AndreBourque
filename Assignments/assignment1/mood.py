mood = input("Enter the mood here: ")
if mood == 'Happy':  # if the mood is happy then
	print("Your mood is %s" % mood) # this block will run
else: # if the mood was not happy
	if mood == 'Sad':  # this block will run, check the mood if the mood is sad
		print("Your mood is %s" %mood)  # this block runs if the mood is sad and the condition was true :)
	else:  # if the mood was not sad then
		if mood == 'Excited':  # this block runs if the mood is excited
			print("Your mood is %s " % mood) # if the mood is excited then this mood runs
		else:  # here Write the code for the angry
		     # add the if condition here
			print()
			# here write the code of the mood angry <---- Here Addd the Code--->


'''  Alternative Easy code (An Easy code, but it checks and goes through all the loops )
mood = input("Enter the mood here:")
if mood == 'Happy':  # if the mood is happy then
	print("Your mood is %s" % mood) # this block will run
if mood == 'Sad':  # this block will run, check the mood if the mood is sad
	print("Your mood is %s" %mood)  # this block runs if the mood is sad and the condition was true :)
if mood == 'Excited': # this block runs if the mood is excited
	print("Your mood is %s " % mood) # if the mood is excited then this mood runs
if mood =='Angry':
	print("Your mood is %s " % mood)
'''