convert_to_ounces = lambda grams: 28.3495231 * grams

# Example usage
grams1, grams2 = 1000, 123454
ounces1, ounces2 = convert_to_ounces(grams1), convert_to_ounces(grams2)

print(f"{grams1} grams is equal to {ounces1} ounces")
print(f"{grams2} grams is equal to {ounces2} ounces")
