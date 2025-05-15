# James is an engineer working on designing a new rocket propulsion system. He needs to solve a quadratic equation to determine the optimal launch trajectory. The equation is of the form ax2 +bx+c=0. 


# Your task is to help James find the roots of this quadratic equation. Depending on the discriminant, the roots might be real and distinct, real and equal, or complex. Implement a program to determine and display the roots of the equation based on the given coefficients.
# Input format :

# The first line of input consists of an integer N, representing the number of coefficients.

# The second line contains three space-separated integers a,b, and c representing the coefficients of the quadratic equation.
# Output format :

# The output displays:

#     If the discriminant is positive, display the two real roots.
#     If the discriminant is zero, display the repeated real root.
#     If the discriminant is negative, display the complex roots as a tuple with real and imaginary parts.


# Refer to the sample output for formatting specifications.
# Code constraints :

# N = 3

# −10 ≤ a,b,c ≤ 10
# Sample test cases :
# Input 1 :

# 3
# 1 5 6

# Output 1 :

# (-2.0, -3.0)

# Input 2 :

# 3
# 2 9 0

# Output 2 :

# (0.0, -4.5)

# Input 3 :

# 3
# 1 2 5

# Output 3 :

# ((-1.0, 2.0), (-1.0, -2.0))

# You are using Python
import math

n=int(input())
l=list(map(int,input().split()))

a,b,c=l[0],l[1],l[2]

m=b*b-(4*a*c)

f=[]
if m<0:
    
    t=[]
    t1=-b/2
    t2=math.sqrt(-m)/2
    t.append(round(t1,2))
    t.append(round(t2,2))
    f.append(tuple(t))
    t.clear()
    t.append(round(t1,2))
    t.append(round(-t2,2))
    f.append(tuple(t))
else:
    
    t1=(-b+math.sqrt(m))/(2*a)
    t2=(-b-math.sqrt(m))/(2*a)
    f.append(round(t1,2))
    f.append(round(t2,2))

    
print(tuple(f))