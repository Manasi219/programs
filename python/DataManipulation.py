import pandas as pd

df1 = {‘Id’: [11, 22, 33, 44,55],
       ‘Name’:[‘Vivek’, ‘Geetha’, ‘Ajay’, ‘Poorva’,’Dipak’], 
       ‘Age’:[27, 24, 22, 32, 28],}

df2 = {‘Id’: [11, 22, 33, 44],
       ‘City’:[‘Pune’, ‘Mumbai’, ‘Noida’, ‘Chennai’], 
       ‘Subject’:[‘Maths’, ‘English’, ‘Science’, ‘History’],}

df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)

# Merge Data
df3 = pd.merge(df1,df2,left_on=’Id’,right_on=’Id’,how=’left’)
print(df3)

pd.concat([df1,df2])
