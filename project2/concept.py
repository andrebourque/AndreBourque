'''
Vegetable = ["Carrot", "Potato","Tomato","Onions","BLAHAAKD","Potato"]  # Carrot <--- 0th index , Potato <-- 1st
print (type(Vegetable))
print (Vegetable[0])
print(Vegetable[2])
# negative indexing
print (Vegetable[-1])  # negative indexing to access the last elements <--
Vegetable.append("ANOTHER VEGETABLE")  # appends function --> add a value to the list.!!!
print(Vegetable)
print (Vegetable.count("Potato"))  # count anything in the list
print (Vegetable.index("Potato")) # its shows the index value
Vegetable.remove("Potato")  # Removes a specific value from the list
# it can have numbers integet with stirng value
Vegetable.append(10)
print(Vegetable)
'''
# Numpy arrays <--- The arrays are of single data types !!.
# list of lists----->
# Customer = [ list1 , list2 , list3]  # list1<--- 0th index
Customer = [["Muhammad","Shafay","Amjad"],
		  ["20", "Red", "EMINEM FAN!"],
		  ["RED SHIRT","PYTHON SHIRT","BLUE BERRY SHIRTS"]]
print(Customer[0][0])  # 2d list ---> [row][columnvalue]
print(Customer[1][2])
print(Customer[2][1]) # <----------
Customer[2][1]="DATASCIENTIS SHIRTS"
print (Customer)
