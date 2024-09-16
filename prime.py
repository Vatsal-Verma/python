f=0
n=int(input("\nenter the number:"))
for i in range(2,n,1):
    if(n%i==0):
        f=1
        break
if(f==0):
    print("\nentered number is prime")
else:
    print("\nentered number is not prime")
