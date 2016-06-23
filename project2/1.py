import pandas as pd
import numpy as np
import time
from datetime import date
# import Scipy
import statistics

if __name__ == '__main__':
	file_data = pd.read_csv("billboard.csv")  # I got all the data in file_data
	df = pd.DataFrame(file_data)  # data into dataframes ---> df
	names = df.columns.tolist()  # this is used to get the columns of the data frames and converted those in to the list.
	# print(names)
	names[names.index('artist.inverted')] = 'Artist'  # -->names[1] = 'Artist'
	names[1] = 'Artist'  # easiest way
	df.columns = names
	######################################################________________________#######
	# print()
	# print(names)
	# print(names)
	# print(df)
	# statistics.pstdev() # this is for the calculation of the standard deviation pass a list of the values in it
	# statistics.pvariance --> calculate the variabne in the data
	# np.std() #this also give us the standard deviation of the specific numpy array !

	for i in names:
		y = i
		if str(i).startswith('x'):
			i = i[1:]
			# print(i)
			i = str(i).replace('.', ' ')
			# print(i)
			names[names.index(y)] = i
			df.columns = names
	# print (df)
	# print (pd.melt(df))
	# print(pd.pivot_table(df, index=["Artist","track","year"]))
	'''
	#print(file_data["year"])  # hash table --> dictionaries
	print (file_data["artist.inverted"])
	print (file_data["date.entered"][4])
	file_data["artist.inverted"][2]="WOAH"
	#file_data["artist.inverted"][0] = "Shafay the best"  # tecbbiques is used to replace the values in the object  which holds the file data!
	#print(file_data["artist.inverted"])
	print (file_data["artist.inverted"])
	del file_data["artist.inverted"]
	#print(file_data["artist.inverted"])
		'''
	names[names.index("76th week")] = "Week Ranking"
	df.columns = names
	# print(pd.pivot_table(df, index=["track"],values=["Week Ranking"]))
	ls = list()
	# print int(df["date.peaked"])
	# print int(df["date.entered"])
	'''
	for i in range(0,len(df) - 1):
		#print(df["date.peaked"])
		peak_string = df["date.peaked"][i]
		peak_string = peak_string.replace('-', '')
		peak_int = int(peak_string)
		entered_string = df["date.entered"][i]
		entered_string = entered_string.replace('-', '')
		entered_int = int(entered_string)
		ls.append(int(peak_int - entered_int))
		df["Week Ranking"][i] = int(peak_int - entered_int)
		#df["Week Ranking"] = required_rank
	print(df["Week Ranking"])
	df["Week Ranking"].values = ls
	print(df)
	'''
	# print(df.tail())  #prints the last five elements out of the input csv file.
	# data manipulation using the pandas and the split stuff
	# Boolean INdexing --->
	print(df["track"].head(10))
	# for retrieving multiple columns
	# list_i_want = ["Artist", "year", "track"]
	# print (df[list_i_want])

	# if you want to have multiple condition just like the database it would be
	# df[(df.Artist=="MADOONA") & (users.Age < 40)].head()
	# some indexing funcitons
	print(df.dtypes)  # returns the datatypes of the column
	# print(df.describe) # this describes the values as well as the mean , max count in the data set
	print (
	df.describe())  # this tells the describe function, shortcuts tells the median mean std, 25% ,50% and the max values
	# How to change the index , means in general remove the 0-5 indexes and then set the indexes
	print(
	df.set_index("Artist").head())  # now the Artist comes out to be the index  # this sets the index to be the artist
	# to change the permenet values
	df.set_index("Artist",
			   inplace=True)  # this inplace that change the artist completely as an index , now the Artist comes out to be the index
	# print(df[10:15])
	print(df.ix[[1, 12, 22]])  # if you want to see the specific rows and you want to check the multiple indexes

	# Merging the data frames !!!!! --> how to merge
	frame1 = pd.DataFrame({'key': range(5), })
	frame1 = pd.DataFrame({'key': range(5), 'frame': ['a', 'b', 'c', 'd', 'e']})
	frame2 = pd.DataFrame({'key': range(2, 7), 'frame': ['x', 'y', 'z', 'w', 'u']})
	print(frame1)
	print(frame2)
	print(pd.merge(frame1, frame2, on='key',
				how='left'))  # on represend on the basis of the kep # take frame 2 values and make it superior
	# if the fram has the sma
	print(pd.merge(frame1, frame2, on='key',
				how='right'))  # right merging and the left mergin the prioritiees are mentioned by the how attribute
	print (pd.merge(frame1, frame2, on='key', how='outer'))  # get the unlapping values of the both of the frames
	print(pd.merge(frame1, frame2, on='key', how='inner'))  # intersaction if they had the same keys
	print (pd.concat([frame1, frame2]))  # concatinate the data frames
	print(pd.concat([frame1, frame2], axis=1))

	# -------------------Group by function in the pandas
	# USING A GROU PBY FUNCTION IN THE PADAS
	# group_artist = pd.groupby(['Artist'])
	#var = pd.groupby('Artist')
	#print(var)
	#print(df.dtypes)
	# All the other statistical methods are provided in the dataset http://pandas.pydata.org/pandas-docs/stable/computation.html
	print(df["1st week"].pct_change(periods =3))  # percentage is determined regerding to the statistic approach
	print("The mean of the data set :", df["1st week"].mean())  # this calculates the mean of the data set
	print("The median is : ", df["1st week"].median())  # to get the medium of the respective data set
	#print("The mode of the dataset is :"+df["1st week"].mode())  # to get the mode of the 1st week.
	# to print the covariance of the data set
	#The below function prints the covariance of the first column with the first column
	print (df["1st week"].cov(df["1st week"]))  # computes the pairwise covariance in the dataset
	#print(df.cov())  # covariance relation in the data frame
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#############!!!!!!!!!!!!!!!!!")
	print(df.cov(min_periods=12))  # the min_periods specifies the minimum number of the observations
	print("##############################################3")
	#print(df.corr())  # this calculates the correlation of the dataframe
	# if you want to have a relational coorellatin of the two data framces
	anotherdataframe = pd.DataFrame(file_data,index = ['year'])
	# dataframe coorellation with another dataframe
	print(df.corr(anotherdataframe)) #dataframe coorelation between the two data frames
