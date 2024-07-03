# 1 =>:
import re

def hasAFollowedbyB(theString):
# The regex pattern    
    pattern= r"a(b*)"
# Searching the pattern
    match= re.match(pattern, theString)

    return match

theString= str(input("enter the string   "))
matched = hasAFollowedbyB(theString)
if matched:
    print(matched.group())
else:
    print("no matched ")

# 2 =>
import re

my_string = input("Enter a string: ")
pattern = re.compile(r'^ab{2,3}$')
match = pattern.match(my_string)

if match:
    print("The string matches the pattern.")
else:
    print("No match.")


# 3 =>
import re

def find_sequences(text):
    pattern = re.compile(r'\b[a-z]+_[a-z]+\b')
    matches = pattern.findall(text)
    return matches

# Get input from the user
user_input = input("Enter a string: ")

# Find and print sequences
sequences = find_sequences(user_input)
if sequences:
    print("Found sequences:", sequences)
else:
    print("No sequences found.")

# 4 =>
import re

def find_sequences(text):
    pattern = re.compile(r'\b[A-Z][a-z]+\b')
    matches = pattern.findall(text)
    return matches

# Get input from the user
user_input = input("Enter a string: ")

# Find and print sequences
sequences = find_sequences(user_input)
if sequences:
    print("Found sequences:", sequences)
else:
    print("No sequences found.")