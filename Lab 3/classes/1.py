class StringUpper:
    def __init__(self, input_string):
        self.input_string = input_string

    def display_upper_string(self):
        print(self.input_string.upper())

user_input = StringUpper(input())
user_input.display_upper_string()
