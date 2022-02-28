#Name:Rifat Sultana Tithy
#ID: 2019-1-60-179
##1
n = [i for i in range(1,1001) 
          if i%8==0]

print(n)

#%%
##2

n = [i for i in range(1,1001) if '6' in str(i)]

print(n)

#%%
##3
string = "Practice Problems to Drill List Comprehension in Your Head"
sub = [i for i in string if i== " "]
print(len(sub))


#%%
##4

string = "Practice Problems to Drill List Comprehension in Your Head"
sub = [i for i in string if i!='a' and i!='e' and i!='i' and i!='o' and i!='u' ]
print(''.join(sub))

#%%
##5
string = "Practice Problems to Drill List Comprehension in Your Head"
words = string.split()
sub = [words for words in words if len(words) < 5]

print(sub)

#%%
##6
string = "Practice Problems to Drill List Comprehension in Your Head"
words = string.split()
sub = {word:len(word) for word in words}

print(sub)

#%%
##7

n=[i for i in range (1,1001) ]
result=[n for n in n if [div for div in range(2,10) if n%div == 0]]
print(result)

#%%
##8
n=[i for i in range (1,1001)]
div = {n:max([div for div in range(1,10) if n % div==0]) for n in n}

print(div)
