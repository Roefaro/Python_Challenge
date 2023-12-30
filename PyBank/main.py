import pandas as pd 
df=pd.read_csv('C:/Users/francesca/Desktop/Class Folder/_Week 3/Module 3 Project/Python_Challenge/PyBank/resources/budget_data.csv')
print(df.count())
sum_row=df[["Profit/Losses"]].sum()
print(df.sum())



print(df.sum())


