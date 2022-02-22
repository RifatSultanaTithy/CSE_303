##1
x= int(input("Enter x :"))
y= int(input("Enter y :"))
product = x*y
if(product > 1000):
    print(x+y)
else:
    print(product)

#%%
##2
r = int(input("Enter radius :"))
pi = 3.1416
perimeter = 2*pi*r
area = pi*r*r
print("Area of a circle :",area)
print("Perimeter of circle:",perimeter)

#%%
##3
def compound_interest_2019_1_60_179(P,R,T):
    A = P * (pow((1+R/100),T))
    compound_interest = A-P
    return compound_interest
P=float(input("Enter the principle amount:"))
R=float(input("Enter interest rate:"))
T=float(input("Enter time:"))
c= compound_interest_2019_1_60_179(P, R, T)
print("Compound interest :{:.2f}".format(c))

#%%
##4
N = int(input("Enter the Value Of N :"))
s=0
for i in range(1, N + 1, 1):
    s = s+(i*i)
print("The value of the series:",s)

#%%
##5
def prime_find_2019_1_60_179(N):
    for i in range(2, N + 1, 1):
        if(N%i)==0:
            return False
            break  
        else:
          return True
N = int (input("Enter number:"))
if(prime_find_2019_1_60_179(N)==False):
    print(N," is not a prime number")
else:
    print(N," is a prime number.")

#%%
##6
N = int(input("Enter Number:"))
f1=0
f2=1
for i in range(2,N):
    f = f1+f2
    f1 = f2
    f2 = f
print("The Fibonacci number is:",f2)

#%%
##7
list = [0,1,2,3,4,5,6,7,8,9,10,50,100]
s = 0
for i in range (0, len(list)):
    s = s + list[i]
print("Sum of the list is:",s)

#%%
##8
list=[1,2,3,4,5,6,7,8,9,10,50]
s = 0
for i in range(0, len(list)):
    if (i%2)==0:
      s=s+list[i]
print("Sum of the Even index is:",s)

#%%
##9
def largest_number_2019_1_60_179(list):
    max=-9999999
    for i in range(0, len(list)):
        if(list[i]>max):
            max = list[i]
    return max
def smallest_number_2019_1_60_179(list):
    min=9999999
    for i in range(0, len(list)):
        if(list[i]<min):
            min = list[i]
    return min
list=[1,2,3,4,5,6,7,8,9,50]
print("Largest_number is :",largest_number_2019_1_60_179(list))
print("Smallest_number is :",smallest_number_2019_1_60_179(list))


#%%
##!0
list=[1,2,3,4,5,6,7,8,9,10,50]
sorted(list)
N=len(list)
print("Second largest Number is:",list[N-2])


#%%
##11
str = (input("Enter String: "))
for i in range(0,len(str)):
    if(i%2==0):
      print(str[i])


#%%
##!2
a = input("Enter a String: ")
n = int(input("Enter the Integer: "))
print(a[n+1:])


#%%
##13
count = 0
for i in "CSE303":
    count = count+1
print(count)

#%%
##14
def palindrome_checker_2019_1_60_179(A):
       if A == A[::-1]:
         return True
A = input("Enter word: ")
if palindrome_checker_2019_1_60_179(A)==True:
          print(A,"is a palindrome")
else:
    print(A,"is not a palindrome")


#%%
##15
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,2,3,4,5,6,7,8,9,10]
newlist=[]
for i in range(0,len(list1)):
    x=list1[i]
    if(x%2!=0):
        newlist.append(x)
for i in range(0,len(list2)):
    y=list2[i]
    if(y%2==0):
        newlist.append(y)
print(newlist)




