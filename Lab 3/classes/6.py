numbers = [2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]

# Using filter with a lambda function to filter prime numbers
prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, numbers))

# Print the prime numbers
print("Prime numbers in the list:", prime_numbers)
