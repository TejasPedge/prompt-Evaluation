# a. Write a Python program that takes a string input from the user and prints out the reversed string.  
# For instance, if a user inputs: "Python is fun"

# Expected output:

# nuf si nohtyP


def reverse_str(str) :
    return str[::-1]

user_string = input();

result = reverse_str(user_string.strip());

print(result);

