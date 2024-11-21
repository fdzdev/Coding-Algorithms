# goal: Exercise 1: Reverse a Simple String. Ask user for input!
# Input: "hello"
# Output: "olleh"


def reverse_string(s):
    return s[::-1]


# Example usage
user_input = input("type: ")  # grab input and name the variable user_input
reverse_string = reverse_string(user_input)
print(reverse_string)  # Output: "olleh"
