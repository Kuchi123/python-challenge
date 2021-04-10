# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
df = pd.read_csv("C:\\Users\\Sam Kumar\\python-challenge\\PyBank\\Resources\\HW3Budget.csv")
Months = len(df.index)
totalprofit = df["Profit/Losses"].sum()
Monthsstr = str(Months)
totalprofitstr = str(df["Profit/Losses"].sum())
averageprofit = totalprofit/Months
averageprofit2 = str(averageprofit)
Greatestincrease = str(df["Profit/Losses"].max())
Greatestdecrease = str(df["Profit/Losses"].min())
print("There are "+ Monthsstr + " months")
print("The total profit is: " +totalprofitstr)
print("The average profit is: " + averageprofit2)
print("The greatest increase in profit was: " + Greatestincrease)
print("The greatest decrease in profit was: " + Greatestdecrease)
f= open("C:\\Users\\Sam Kumar\\python-challenge\\PyBank\\analysis\\financialanalysis.txt","w+")
L = ["Total Months: " + Monthsstr + " \n","Total Profit: " + totalprofitstr +" \n","Average profit: "+ averageprofit2 +" \n", "The Greatest Profit increase is: " + Greatestincrease +"\n", "The Greatest Profit Decrease is: " + Greatestdecrease + "\n"]
f.writelines(L)
f.close()



