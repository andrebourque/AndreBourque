import pandas as pd
import matplotlib.pyplot as plt
import
read_data = pd.read_csv('Iowa_Liquor_sales_sample_10pct.csv')
df = pd.DataFrame(read_data)
#df2 = pd.DataFrame(read_data, usecol=3)
anotherlist = df['City'][0]
print(anotherlist)
#print(df['Bottle Volume (ml)'][0:5])
# anotherlist = list()
# anotherlist = df['Bottle Volume (ml)'][0:5]
# anotherlist.append(7500000)
# print(anotherlist)
# df = df.replace({'\$': ''}, regex=True)
# print(df.dtypes)

#print(df[['City', 'Bottles Sold']].groupby('City').size().sort_values(ascending=False))
# print(df[['City', 'Bottles Sold']].groupby('City').size().sort_values(ascending=False).head(30).plot(kind='barh', figsize=[20,15]))
# print(df[['City', 'Bottles Sold']].groupby('City').size().sort_values(ascending=False).head(30))
sum = 0
# plt.scatter(x,y)
# print(df[['City']].groupby('City').size().sort_values(ascending=False))
# print(df[['City', 'Bottles Sold']].groupby('Bottles Sold').size().sort_values(ascending=False).head(30).plot(kind='barh', figsize=[20,15]))
# print(df[['City', 'Bottles Sold']].groupby('City').size().sort_values(ascending=False).plot(kind='hist'))
# plt.xlabel('BOTTLE SOLD')
# plt.ylabel('City')
# plt.title('ANALYSIS OF BOTTLE SOLD IN CITIES')
# plt.tick_params(axis='x',color='white')
# plt.tick_params(axis='y', color='Red')
# plt.xticks()
# plt.show()
# finds sequence of symbols like func
# most_rates = file_data.groupby('Stuff').size().sort_values(ascending=False)

#
# list_xaxis = list()
#
# list_yaxis = list()
#
# li_cities = list()
# print(df["City"][0])
# for i in range(0, len(df["City"])):
# 	if df["City"][i] in li_cities:
# 		continue
# 	else:
# 		li_cities.append(i)
# print(li_cities)
print(df.dtypes) # checking the datatypes of the dataframe

# Below is the Percentage change
print(df["Store Number"].pct_change(periods=3))  # percentage is determined regerding to the statistical approach
# over a given number of the period the percentage is determinded
#print(df.pct_change(periods=3)) # this determines the complete dataset
print("The mean of the data set", df["Store Number"].mean()) # this is the mean calculation
print("This is the median calculation of Bottle sold : ", df["Bottles Sold"])
print("The covariance is : ", df.cov(min_periods=3))
print("The coveriance on another data set is :")
# Covariance is a measure of how changes in one variable are associated with changes in a second variable.
print(df["Store Number"].cov(df["Vendor Number"]))  #the dataframe coveriance
# for the correlation
print("Below is the Correlation")
print(df.corr())  # this defines the coorelation of the data frame
#print(df[df["Total Sales"]==])

# for ranking the data the data rank function is used
