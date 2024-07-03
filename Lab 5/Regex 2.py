# 5 =>
import re

def match_pattern(text):
    pattern = re.compile(r'a.*b$')
    match = pattern.match(text)
    return match

# Get input from the user
user_input = input("Enter a string: ")

# Check if the input matches the pattern
if match_pattern(user_input):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")


# 6 =>
def replace_chars_with_colon(text):
    # Replace space, comma, and dot with colon
    modified_text = text.replace(' ', ':').replace(',', ':').replace('.', ':')
    return modified_text

# Example usage:
input_text = input("Enter a string: ")
modified_text = replace_chars_with_colon(input_text)
print("Modified text:", modified_text)

# 7 =>
def snake_to_camel(snake_case_str):
    # Split the string by underscores
    words = snake_case_str.split('_')
    
    # Capitalize the first letter of each word except the first one
    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camel_case_str

# Example usage:
snake_case_input = input("Enter a snake_case string: ")
camel_case_output = snake_to_camel(snake_case_input)
print("CamelCase output:", camel_case_output)

# 9 =>
import re

def split_at_uppercase(input_str):
    # Split the string at uppercase letters using regular expression
    split_list = re.findall(r'[A-Z][^A-Z]*', input_str)
    return split_list

# Example usage:
input_string = input("Enter a string: ")
split_strings = split_at_uppercase(input_string)
print("Split strings:", split_strings)
