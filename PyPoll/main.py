# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:29:52 2021

@author: Sam Kumar
"""

import pandas as pd
df = pd.read_csv("C:\\Users\\Sam Kumar\\python-challenge\\PyPoll\\Resources\\ElectionData.csv")
Voters = len(df.index)
stringvotes = str(Voters)
print("The number of voters is: " + stringvotes)
Khan = len(df[df["Candidate"] == "Khan"])
Correy = len(df[df["Candidate"] == "Correy"])
Li = len(df[df["Candidate"]=="Li"])
Otolley = len(df[df["Candidate"]=="O'Tooley"])
Total = Khan + Correy +Li + Otolley
print("Khan number of voters: " + str(Khan) +"  percentage:" + str(Khan/Total*100) + "%")
print("Correy number of voters: " + str(Correy) +"  percentage:" + str(Correy/Total*100) + "%")
print("Li number of voters: " + str(Li) +"  percentage:" + str(Li/Total*100) + "%")
print("O'Tolley number of voters: " + str(Otolley) +"  percentage:" + str(Otolley/Total*100) + "%")
x = ""
if Khan == max(Khan, Correy, Li, Otolley):
    x = "Winner : Khan"
elif Correy == max(Khan, Correy, Li, Otolley):
    x = "Winner: Correy"
elif Li == max(Khan, Correy, Li, Otolley):
    x = "Winner: Li"
elif Otolley == max(Khan, Correy, Li, Otolley):
    x = "Winner: Otolley"
print(x)
f = open("C:\\Users\\Sam Kumar\\python-challenge\\PyPoll\\analysis\\voterresults.txt", "w+")
L = ["The number of voters is: " + stringvotes + "\n","Khan number of voters: " + str(Khan) +"  percentage:" + str(Khan/Total*100) + "%\n","Correy number of voters: " + str(Correy) +"  percentage:" + str(Correy/Total*100) + "%\n","Li number of voters: " + str(Li) +"  percentage:" + str(Li/Total*100) + "%\n","O'Tolley number of voters: " + str(Otolley) +"  percentage:" + str(Otolley/Total*100) + "%\n",x]
f.writelines(L)
f.close()
