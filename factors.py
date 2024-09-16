# Function to find factors of a number
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Input number from user
num = int(input("Enter a number to find its factors: "))

# Finding factors using the function
factors = find_factors(num)

# Displaying the factors
print("Factors of", num, "are:", factors)
