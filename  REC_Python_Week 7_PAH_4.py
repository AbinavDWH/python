
# // Arjun is a data scientist working on an image processing task. He needs to normalize the pixel values of a grayscale image matrix to scale between 0 and 1. The input image data is provided as a matrix of integers. 


# // Help him to implement the task using the numpy package.


# // Formula:

# // To normalize each pixel value in the image matrix:

# // normalized_pixel = (pixel - min_pixel) / (max_pixel - min_pixel)

# // where min_pixel and max_pixel are the minimum and maximum pixel values in the image matrix, respectively. If all pixel values are the same, the normalized image matrix should be filled with zeros.
# // Input format :

# // The first line of input consists of an integer value, rows, representing the number of rows in the image matrix.

# // The second line of input consists of an integer value, cols, representing the number of columns in the image matrix.

# // The next rows lines each consist of cols integer values separated by a space, representing the pixel values of the image matrix.
# // Output format :

# // The output prints: normalized_image


# // Refer to the sample output for the formatting specifications.
# // Code constraints :

# // The given test cases fall under the following constraints:

# // 1 ≤ rows ≤ 100

# // 1 ≤ cols ≤ 100

# // 0 ≤ pixel ≤ 255
# // Sample test cases :
# // Input 1 :

# // 2
# // 3
# // 1 2 3
# // 4 5 6

# // Output 1 :

# // [[0.  0.2 0.4]
# //  [0.6 0.8 1. ]]

# // Input 2 :

# // 2
# // 2
# // 0 0
# // 0 0

# // Output 2 :

# // [[0. 0.]
# //  [0. 0.]]

# You are using Python
import numpy as np

# Read dimensions
rows = int(input())
cols = int(input())

# Read matrix
data = [list(map(int, input().split())) for _ in range(rows)]
image = np.array(data, dtype=float)

# Calculate min and max
min_pixel = image.min()
max_pixel = image.max()

# Normalize
if max_pixel == min_pixel:
    normalized_image = np.zeros((rows, cols))
else:
    normalized_image = (image - min_pixel) / (max_pixel - min_pixel)

# Print output
print(normalized_image)
