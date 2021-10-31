import pandas as pd

#set the filepath or folder location 
filepath = "C:\Documents\test.csv"
df = read_csv(filepath,dtype=str)
print(df)
#display header
print(list(df))
