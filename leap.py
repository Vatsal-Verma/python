year=int(input("\nEnter the year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("\nleap year")
else:
    print("\nnot leap year");
