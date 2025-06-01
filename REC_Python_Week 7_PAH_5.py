# A company conducted a customer satisfaction survey where each respondent provides their RespondentID and an optional textual Feedback. Sometimes, respondents submit their ID without any feedback or with empty feedback.



# Your task is to process the survey responses using pandas to replace any missing or empty feedback with the phrase "No Response". Finally, print the cleaned survey responses exactly as shown in the sample output.

# Input format :
# The first line contains an integer n, the number of survey responses.

# Each of the next n lines contains:

# A RespondentID (a single alphanumeric string without spaces),

# Followed optionally by a Feedback string, which may be empty or missing.

# If no feedback is provided after the RespondentID, treat it as missing.

# Output format :
# Print the line:

# Survey Responses with Missing Feedback Filled:

# Then print the cleaned survey data as a table with two columns: RespondentID and Feedback.



# The table should have the headers exactly as:

# RespondentID Feedback

# Print each respondent's data on a new line, aligned to match the output produced by pandas.DataFrame.to_string(index=False).



# For any missing or empty feedback, print "No Response" in the Feedback column.

# Maintain the spacing and alignment exactly as shown in the sample outputs.



# Refer to the sample output for the formatting specifications.

# Code constraints :
# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 1000

# RespondentID consists of alphanumeric characters without spaces.

# Feedback may be any string, possibly containing spaces, or may be missing entirely.

# Sample test cases :
# Input 1 :
# 4
# 101 Great service
# 102 
# 103 Loved it
# 104
# Output 1 :
# Survey Responses with Missing Feedback Filled:
# RespondentID      Feedback
#          101 Great service
#          102   No Response
#          103      Loved it
#          104   No Response
# Input 2 :
# 3
# 201 
# 202 Okay experience
# 203 
# Output 2 :
# Survey Responses with Missing Feedback Filled:
# RespondentID        Feedback
#          201     No Response
#          202 Okay experience
#          203     No Response

# You are using Python
import pandas as pd

# Read number of responses
n = int(input())

# Read each response line
data = []
for _ in range(n):
    line = input().strip()
    if ' ' in line:
        respondent_id, feedback = line.split(' ', 1)
        feedback = feedback.strip()
    else:
        respondent_id = line
        feedback = ''
    data.append([respondent_id, feedback])

# Create DataFrame
df = pd.DataFrame(data, columns=["RespondentID", "Feedback"])

# Replace missing or empty feedback with "No Response"
df["Feedback"] = df["Feedback"].replace('', pd.NA)
df["Feedback"] = df["Feedback"].fillna("No Response")

# Print output
print("Survey Responses with Missing Feedback Filled:")
print(df.to_string(index=False))
