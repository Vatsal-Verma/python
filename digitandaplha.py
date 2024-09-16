a=input("\nenter the string")
count1=0
count2=0
for i in a:
    if(i.isalpha()):
        count1=count1+1
    if(i.isdigit()):
        count2=count2+1
print("\n number of alphabets :",count1,"\nnumber of digits:",count2)
