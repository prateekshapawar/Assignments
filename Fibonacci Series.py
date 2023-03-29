p=int(input("Enter number of terms u want in Fibonacci Series:"))
a=0
b=1
f=0
count=1
while count<=p:
    f=a+b
    print(a)
    a=b
    b=f
    count+=1