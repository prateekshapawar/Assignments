p=int(input("Enter Number:"))

i=1
c=0
while i<=p:
    if (p%i)==0:
        c+=1
    i+=1

if c==2:
    print(p,"is a prime number")
else:
    print(p,"is not a prime number")