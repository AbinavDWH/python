# Write a program to obtain the start time and end time for the stage event show. If the user enters a different format other than specified, an exception occurs and the program is interrupted. To avoid that, handle the exception and prompt the user to enter the right format as specified.


#     Start time and end time should be in the format 'YYYY-MM-DD HH:MM:SS'
#     If the input is in the above format, print the start time and end time.
#     If the input does not follow the above format, print "Event time is not in the format "

# Input format :

# The first line of input consists of the start time of the event.

# The second line of the input consists of the end time of the event.
# Output format :

# If the input is in the given format, print the start time and end time.

# If the input does not follow the given format, print "Event time is not in the format".


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# The input format: YYYY-MM-DD HH:MM:SS
# Sample test cases :
# Input 1 :

# 2022-01-12 06:10:00
# 2022-02-12 10:10:12

# Output 1 :

# 2022-01-12 06:10:00
# 2022-02-12 10:10:12

# Input 2 :

# 2022-01-12 06:10:00
# 2022-02-12 10:00:

# Output 2 :

# Event time is not in the format

# Input 3 :

# 2022-01-12 06:10:00
# 2022-02-31 10:10:12

# Output 3 :

# Event time is not in the format

# Input 4 :

# 2022-01-12 10:75:00
# 2022-02-12 10:10:80

# Output 4 :

# Event time is not in the format

# You are using Python
from datetime import datetime
import re
import calendar

def va(d_s1,d_s2):
    try:
        dt=datetime.strptime(d_s1,"%Y-%m-%d %H:%M:%S")
        end=datetime.strptime(d_s2,"%Y-%m-%d %H:%M:%S")
        print(d_s1)
        print(d_s2)
    except Exception:
        print("Event time is not in the format")
s1=input()
s2=input()
va(s1,s2)


# l1=list(re.split(r'[-: ]',s1))
# l2=list(re.split(r'[-: ]',s2))

# try:
#     if (int(l1[1])>12 or int(l1[2])>calendar.monthrange(int(l1[0]),int(l1[1]))[1] or int(l1[3])>12 or int(l1[4])>59 or int(l1[5])>59 or int(l2[1])>12 or int(l2[2])>calendar.monthrange(int(l2[0]),int(l2[1]))[1] or int(l2[3])>12 or int(l2[4])>59 or int(l2[5])>59):
#         print("Event time is not in the format")
#     else:
#         print(s1+"\n"+s2)
# except Exception as e:
#     print("Event time is not in the format")
    