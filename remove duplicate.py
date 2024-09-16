lst1=[1,1,2,3,4,5,6,6]
lst2=[]
for i in lst1:
    if(i not in lst2):
        lst2.append(i)
print(lst2)
