# Arjun is developing a system to monitor environmental sensors installed in different rooms of a smart building. Each sensor records multiple temperature readings throughout the day. To compare sensor data fairly despite differing scales, Arjun needs to normalize each sensor’s readings so that they have a mean of zero and standard deviation of one. 


# Help him implement this normalization using numpy.


# Normalization Formula:

# Input format :

# The first line of input consists of two integers: sensors (number of sensors) and samples (number of readings per sensor).

# The next sensors lines each contain samples space-separated floats representing the sensor readings.
# Output format :

# The first line of output prints: "Normalized Sensor Data:"

# The next lines print the normalized readings as a numpy array, where each row corresponds to a sensor’s normalized values.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ sensors, samples ≤ 1000

# Sensor readings are real numbers.
# Sample test cases :
# Input 1 :

# 3 3
# 1.0 2.0 3.0
# 4.0 5.0 6.0
# 7.0 8.0 9.0

# Output 1 :

# Normalized Sensor Data:
# [[-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]]

# Input 2 :

# 2 4
# 1.0 2.0 3.0 4.0
# 4.0 3.0 2.0 1.0

# Output 2 :

# Normalized Sensor Data:
# [[-1.34164079 -0.4472136   0.4472136   1.34164079]
#  [ 1.34164079  0.4472136  -0.4472136  -1.34164079]]

# You are using Python
import numpy as np

# Read inputs
sensors, samples = map(int, input().split())
data = [list(map(float, input().split())) for _ in range(sensors)]


arr = np.array(data)

# Calculate mean and std deviation along each sensor's readings (rows)
mean = arr.mean(axis=1, keepdims=True)
std = arr.std(axis=1, keepdims=True)

# Normalize
normalized = (arr - mean) / std

# Output
print("Normalized Sensor Data:")
print(normalized)
