
# You are tasked with designing a shipping cost calculator program that calculates the shipping cost for packages based on their weight and destination. The program utilizes different shipping rates for domestic, international, and remote destinations. The rates for each destination type are provided as global constants.


# Constant Values:


# DOMESTIC_RATE = 5.0

# INTERNATIONAL_RATE = 10.0

# REMOTE_RATE = 15.0


# Function Signature: calculate_shipping(weight, destination)


# Formula: shipping cost = weight * destination rate
# Input format :

# The first line of the input consists of a float representing the weight of the package.

# The second line consists of a string representing the destinations(Domestic or International or Remote).
# Output format :

# The program outputs any one of the following:

#     If the input is valid and the destination is recognized, the output should consist of a single line stating the calculated shipping cost for the given weight and destination in the format: "Shipping cost to [destination] for a [weight] kg package: $[calculated cost]" with two decimal places.
#     If the input weight is not a positive float, print "Invalid weight. Weight must be greater than 0."
#     If the input destination is not one of the valid options, print "Invalid destination."


# Refer to the sample output for the formatting specifications.
# Code constraints :

# 1.0≤weight≤1000.0.

# 1≤len(destination)≤15.

# destination is case sensitive.
# Sample test cases :
# Input 1 :

# 5.5
# Domestic

# Output 1 :

# Shipping cost to Domestic for a 5.5 kg package: $27.50

# Input 2 :

# 2.0
# International

# Output 2 :

# Shipping cost to International for a 2.0 kg package: $20.00

# Input 3 :

# -2.0
# Domestic

# Output 3 :

# Invalid weight. Weight must be greater than 0.


# You are using Python
n=float(input())
s=input()
p=0
destination=""
weight=n
shipping_cost=0.0
if(n<0):
    print("Invalid weight. Weight must be greater than 0.")
    exit()
if s=="Domestic":
    destination=s
    shipping_cost=n*5.0
elif s=="International":
    destination=s
    shipping_cost=n*10.0
elif s=="Remote":
    destination=s
    shipping_cost=n*15.0
else:
    print("Invalid destination.")
    exit()

    
if shipping_cost is not None:
    print(f"Shipping cost to {destination} for a {weight} kg package: ${shipping_cost:.2f}")