# Program to solve the circuit give

# Initialize variables with default values
a=1
b=0
c=0

# Computing all bitwise operations
aANDb = a & b
bXORc = b ^ c
bORc = b | c
g = bXORc & bORc

# Calculationg final result
final = aANDb ^ g

# Printing final result
print("q = ",final)