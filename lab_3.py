
import pandas as pd
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(type(obj))

print(obj[obj%2==0])
print(obj+5 )
print(obj*2)


#%%

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 
 'Utah': 5000}

obj3 = pd.Series(sdata)
print(obj3)

#%%

df2=pd.read_csv("sam.csv")
df2.columns=['id','state','population','murder_rate']
print(df2)
print(df2.head() )
print(df2.tail()) 
print(df2.count())

#%%
dict1 = {'id':[1,2,3],'name':['alice','bob','charlie'],
 'age':[20, 25, 32]}
df1 = pd.DataFrame(dict1)
print(df1)

#%%
list1 = [['Alice',23,3.5,10],['Bob',24,3.4,6],['Charlie',22,3.9,8]]
df = pd.DataFrame(list1)
df.columns = ['name','age','cgpa','hoursStudied']
print(df.head())


























