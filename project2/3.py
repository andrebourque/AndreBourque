import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
	#headers = ['name','Artist']
	required_col = ['year','Artist','Stuff']
	#file_data = pd.read_csv("billboard.csv",names=required_col,usecols=range(3),encoding="ISO-8859-1")  # I got all the data in file_dat
	file_data = pd.read_csv("billboard.csv")
	#print(file_data) #use col uses only two columns
	#merge = pd.merge() use this to add the two files to a single ones
	df = pd.DataFrame(file_data)
	# heavy data analysis .!!
	# lens is a data frame
	#most_rates = file_data.groupby('Stuff').size().order(ascending=False)[:20]  # the group by groups regerding to the specigfic columns
	# most_rates = file_data.groupby('Stuff').size().sort_values(ascending=False)
	# print(most_rates)
	# most_valuecounts = file_data.Artist.value_counts()[:20]  # fieldata.columnname.value_counts() #returns the count of the columns
	# print(most_valuecounts)
	# # for getting the statistics
	#movies_stat = file_data.groupby('Artist').agg({'year':[np.size, np.mean]})  # this returns the aggregate of the numpy size and the numpy mean
	# the year represents the numpy size and the numpy mean!
	#file_data.columnname.typeofgraph(bins=30)
	#filedata.Artists.hist(bins = 30) # this creates  a histogram of 30 width block
	#year = int(file_data['year'])
	#year.hist(bins=30)
	#plt.show()

	#Adding a Pivot table//////
	#pivoted = file_data.pivot_table(index=['name of the column'],columns = ['gender'], values = 'ratings',fill_value = 0)
	# pivot table stuff above now the index name of columns become something.
	# column becomes title
	# values become the values to be inserted in it
	#  pivoted['diff'] = pivoted.M - pivoted.F
	# disargement = pivoted[pivoted.movie_id.init(most_50.index)]['diff'] # we get the differences
	# pivoted.reset_index
	#plotting customized
	# plt.title()
	#plt.xlabel()
	#plt.ylabel()
	#tablename.order().plot(kind='barh',figsize)  # bar chat horizintal is the kind one
	# tablename.


	'''---Statistical Operations!---'''
	print(df.dtypes)