a="strig"
if(len(a)>3):
    if(a.endswith("ing")):
        a+="ly"
    else:
        a=a+"ing"
print(a)