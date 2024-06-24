def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        # To keep track of characters already used in this position
        used = set()
        for i in range(l, r + 1):
            if a[i] not in used:
                # Swap characters
                a[l], a[i] = a[i], a[l]
                # Recursively permute the remaining characters
                permute(a, l + 1, r)
                # Backtrack
                a[l], a[i] = a[i], a[l]
                used.add(a[i])

string = "ABA"
n = len(string)
a = list(string)
permute(a, 0, n-1)

