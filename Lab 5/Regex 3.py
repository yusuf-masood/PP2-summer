import re

def insert_spaces(s):
    # Use regular expression to insert spaces before words starting with capital letters
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    # Add a space before any sequence of uppercase letters that are not at the beginning of the string
    s = re.sub(r'(?<!^)([A-Z][a-z])', r' \1', s)
    return s

theString = input('Enter your string: ')
matched = insert_spaces(theString)
print(matched)

# 10 =>
def camel_to_snake(s):
  
    import re
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


    return s



theString = input('Enter The string again ')
theString = camel_to_snake(theString)
print(theString) 