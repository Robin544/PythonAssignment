#                                       PANDAS


# Importing pandas lib.
import pandas as pd


# QUESTION 1:
# Create a data-frame with your name, age, mail-id and phone number and
# add your friends’s information to the same.

print("\n")
data_frame = {'Name': ['Robin Singh'], 'Age': [20], 'mail id': ['robinsinghkamboj@gmail.com'],
              'phone number': ['8081828384']}

df = pd.DataFrame(data_frame)       # Creating a data-frame.

# Adding friend's information.
df.loc[1] = ['Pooja Kamboj', 20, 'poojau0001@gmail.com', '9192939495']
df.loc[2] = ['Mayank Kumar', 17, 'mayanklinghe@gmail.com', '9897969594']
df.loc[3] = ['Prashant Kamboj', 19, 'prashantkamboj418@gmail.com', '9897954321']
df.loc[4] = ['Shalini', 18, 'shalinilinghe@gmail.com', '9835789594']
df.loc[5] = ['Rajesh Kumar', 22, 'rajeshlinghe@gmail.com', '9876543294']
print(df)
print("\n\n")


# QUESTION 2:
# Import the data from "https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv" and
# print the following :
# a.) First 5 rows of Data-frame
# b.) First 10 rows of the Data-frame
# c.) find basic statistics on the particular data-set.
# d.) Find the last 5 rows of the data-frame
# e.) Extract the 2nd column and find basic statistics on it.

df = pd.read_csv('example.csv')

# a.) First 5 rows of Data-frame
print(df.head(5))

# b.) First 10 rows of the Data-frame
print("\n", df.head(10))

# c.) Find basic statistics on the particular data-set.
print("\n", df['Rainfall'].describe())
print("\n", df['WindSpeed3pm'].describe())

# d.) Find the last 5 rows of the data-frame
print("\n", df.tail(5))

# e.) Extract the 2nd column and find basic statistics on it.
basic_statistic = [df.iloc[:, 2].min(),
                   df.iloc[:, 2].max(),
                   df.iloc[:, 2].sum(),
                   df.iloc[:, 2].median(),
                   df.iloc[:, 2].mean(),
                   df.iloc[:, 2].nunique(),]

print("\n", basic_statistic)


# Finally done.

print("\n\nDone")
