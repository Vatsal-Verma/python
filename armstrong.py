n=int(input("\nenter the number"))
s=0
c=n
while(n>0):
    a=n%10;
    s=s+a**3
    n=n//10
if(s==c):
    print("yes")

