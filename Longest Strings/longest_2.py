# Method 2: Using the max() Function with key
# max() function is used to find the maximum value in an iterable.
# min() is the opposite of max(). The parameter key=len means that the function will determine the "maximum" based on the length (len) of each string


def longest_string_max(strings):
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    return longest, shortest


strings = ["apple", "banana", "cherry", "date", "elderberry"]
print(longest_string_max(strings))  # Output: elderberry
