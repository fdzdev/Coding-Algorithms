# goal: Exercise 3: Reverse a String Recursively
# Input: "world"
# Output: "dlrow"


def reverse_string_recursive(s):
    # Define a function named reverse_string_recursive that takes a single parameter 's', which is expected to be a string.

    if len(s) == 0:
        # Check if the length of the string 's' is 0 (i.e., if the string is empty).
        return s
        # If the string is empty, return it as is. This is the base case for the recursion.

    else:
        # If the string is not empty, execute the following:
        return s[-1] + reverse_string_recursive(s[:-1])
        # Get the last character of the string 's' using s[-1] and concatenate it with the result of calling
        # reverse_string_recursive(s[:-1]), which is the string 's' without its last character.
        # This effectively builds the reversed string one character at a time through recursive calls.


# Example usage
print(reverse_string_recursive("world"))  # Output: "dlrow"
# Call the function with the string "world" and print the result.
# The output will be "dlrow", which is the reverse of the input string.
