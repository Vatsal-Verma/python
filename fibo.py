def fibo(n):
    if(n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("\nenter the limit:"))
for i in range(0,n,1):
    k=fibo(n)
    print(k)
