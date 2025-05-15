# Professor Adams needs to analyze student participation in three recent academic workshops. She has three sets of student IDs: the first set contains students who registered for the workshops, the second set contains students who actually attended, and the third set contains students who dropped out. 


# Professor Adams needs to determine which students who registered also attended, and then identify which of these students did not drop out.


# Help Professor Adams identify the students who registered, attended, and did not drop out of the workshops.
# Input format :

# The first line of input consists of integers, representing the student IDs who registered for the workshops.

# The second line consists of integers, representing the student IDs who attended the workshops.

# The third line consists of integers, representing the student IDs who dropped out of the workshops.
# Output format :

# The first line of output displays the intersection of the first two sets, which shows the IDs of students who registered and attended.

# The second line displays the result after removing student IDs that are in the third set (dropped out), showing the IDs of students who both attended and did not drop out.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# 1 ≤ set_elements ≤ 20
# Sample test cases :
# Input 1 :

# 1 2 3
# 2 3 4
# 3 4 5

# Output 1 :

# {2, 3}
# {2}

# Input 2 :

# 2 4
# 1 4 2
# 2 6

# Output 2 :

# {2, 4}
# {4}

# You are using Python
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=set(map(int,input().split()))

print(a&b)
print((a-c)&b)