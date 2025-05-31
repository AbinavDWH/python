    # You are using Python
import pandas as p
    
n=int(input())
    
l=[]
for i in range(n):
    l.append(list(map(str,input().split())))
    
data=p.DataFrame(l,columns=['Name','Years at Company'])

data['Years at Company']=p.to_numeric(data['Years at Company']).astype(float).round(1)
    
exp=[]
for i in range(n):
    if float(l[i][1])<3:
        exp.append("Junior")
    elif float(l[i][1])>=3 and float(l[i][1])<6:
        exp.append("Mid")
    elif float(l[i][1])>5:
        exp.append("Senior")
    
data['Experience Level']=exp
    
print("Employee Data with Experience Level:")
print(data.to_string(index=False))
    
    