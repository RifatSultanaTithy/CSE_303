import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%%
#1
df=pd.read_csv( 'dataset_lab04.csv' )
print(df.shape)
print ('Total rows: ',df.shape[0])
print ('Total columns: ',df.shape[1])

#%%
#2
print("Numerical Summary of Time column -\n")
time = df['Time']
print(time.describe())

print("Numerical Summary of Amount column -\n")
amount = df['Amount']
print(amount.describe())

#%%
#3
print("Lets take V10 and V15 column for Statistical measurements")

print("\nStatistical measurement of V10 column - ")
v10 = df['V10']   
print("Mean: ",v10.mean())
print("Median: ",v10.median())
print("Standard Deviation: ",v10.std())
print("Variance: ",v10.var())

print("\nStatistical measurement of V15 column - ")
v15 = df['V15']   
print("Mean: ",v15.mean())
print("Median: ",v15.median())
print("Standard Deviation: ",v15.std())
print("Variance: ",v15.var())


#%%
#4
b=df['Time']
print("\nTime informations\n")

print( "variety mean: ",b.mean() )
print("variety median: ",b.median())
print("1st quartile: ",b.quantile(0.25) )
print("2nd quartile: ",b.quantile(0.50) )
print("3rd quartile: ",b.quantile(0.75))
print("variety standard daviance: ",b.std() )
print("variety daviance: ",b.var() )
print("variety max: ",b.max() )
print("variety min: ",b.min())
print("variety skew: ",b.skew() )
print("variety curtosis: ",b.kurt())

#%%
df.boxplot( column=[ 'Time' ] )
#%%
b=df['Amount']
print("\nAmount informations\n")

print( "variety mean: ",b.mean() )
print("variety median: ",b.median())
print("1st quartile: ",b.quantile(0.25) )
print("2nd quartile: ",b.quantile(0.50) )
print("3rd quartile: ",b.quantile(0.75))
print("variety standard daviance: ",b.std() )
print("variety daviance: ",b.var() )
print("variety max: ",b.max() )
print("variety min: ",b.min())
print("variety skew: ",b.skew() )
print("variety curtosis: ",b.kurt())

#%%
df.boxplot( column=['Amount'] )

#%%
#5

time=df[['Time']]
time.hist( column = ['Time'] , bins=5 )
print("time: \n\n",time)
#%%
amount=df[ ['Amount'] ]
amount.hist( column=['Amount'],bins=5 )

print("amount: \n\n",amount)

#%%
#6
class0 = len(df[df['Time']==0])*100
class1 = len(df[df['Amount']==1])*100

print("Percentage of 0 :",class0/len(df['Time']))
print("Percentage of 1 :",class1/len(df['Amount']))

#%%
#7
a=class0/len(df['Time'])
b=class1/len(df['Amount'])

plt.bar(a, df['Time'],  color ='maroon', width = 0.4)
plt.bar(b, df['Amount'], color ='maroon', width = 0.4)
plt.show()

#%%
# Task 8
values = df['Class'].value_counts()
percentage_non_fr = (values[0] / len(df["Time"])) * 100
percentage_fr = (values[1] / len(df["Amount"])) * 100
plotdata = pd.DataFrame({"Percentage": [percentage_non_fr, percentage_fr]})
plotdata.plot(kind="bar", color=["Green"])

#%%
# Task 9
    # neg. skew = V1
    # pos. skew = V4
    # platykurtic = V27
    # leptokurtic = V26
df.hist(column=["V1", "V4", "V27", "V26"], bins=5, color=["purple"])


#%%
# Task 10
max_corr= 0
for i in df.columns:
        for j in df.columns:
            if i != j:
                corr = df[i].corr(df[j])
                if max_corr < corr:
                    max_corr = corr
                    max_i = i
                    max_j = j
print(
      "\nHighest Positive Correlation is: ", max_corr, "between", max_i, "and", max_j
    )
print()
print()

#%%
# Task 11
df.plot.scatter(x="V7", y="Amount", color=["green"])


#%%
# Task 12

min_corr = 0
for i in df.columns:
        for j in df.columns:
            if i != j:
                corr = df[i].corr(df[j])
                if min_corr > corr:
                    min_corr = corr
                    min_i = i
                    min_j = j
print(
        "\nHighest negative Correlation is: ", min_corr, "between", min_i, "and", min_j
    )
print()
print()

#%%
# Task 13

df.plot.scatter(x="V2", y="Amount", color=["green"])

#%%
# Task 14

df.boxplot(column=["Amount"])

#%%
# Task 15

class_zero_amount = df[["Amount", "Class"]].query("Class == 0")
class_one_amount = df[["Amount", "Class"]].query("Class == 1")
class_zero_amount_without_class = class_zero_amount["Amount"]
class_one_amount_without_class = class_one_amount["Amount"]
columns = [class_zero_amount_without_class, class_one_amount_without_class]
fig, ax = plt.subplots()
ax.boxplot(columns)
plt.show()
print("\nComment:\nThere might be a Negative Correlation.")
    
    

#%%
