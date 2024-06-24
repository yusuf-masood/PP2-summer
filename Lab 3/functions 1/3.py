def solve(numheads, numlegs):
    # Calculate number of rabbits (r) and chickens (c)
    r = (numlegs - 2 * numheads) / 2
    c = numheads - r

    # Check if r and c are non-negative integers
    if r >= 0 and c >= 0 and r.is_integer() and c.is_integer():
        print(f"Number of chickens: {int(c)}")
        print(f"Number of rabbits: {int(r)}")
    else:
        print("No valid solution found.")

def solve(numheads, numlegs):
    # Calculate number of rabbits (r) and chickens (c)
    r = (numlegs - 2 * numheads) / 2
    c = numheads - r

    # Check if r and c are non-negative integers
    if r >= 0 and c >= 0 and r.is_integer() and c.is_integer():
        print(f"Number of chickens: {int(c)}")
        print(f"Number of rabbits: {int(r)}")
    else:
        print("No valid solution found.")

# Example usage with provided numbers of heads and legs
solve(35, 94)

