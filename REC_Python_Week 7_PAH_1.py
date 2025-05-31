# You are using Python
import numpy as np
import math

n=int(input())


l=list(map(float,input().split()))

max_time=math.ceil(max(l))
# print(max_time)
w_l=[s for s in range(0,max_time+5,5)]
# print(w_l)
arr=np.array(l)
print("Wait Time buckets and Counts:")
n_l=[]
for i in range(1,len(w_l)):
    n_l.append(np.sum((arr<w_l[i]) & (arr>=w_l[i-1])))

for i in range(1,len(w_l)):
    # if(n_l[i-1]!=0):
    print(f"{w_l[i]-5}-{w_l[i]}:{n_l[i-1]}")
    # else:
        # break