# Method 2: Using the max() Function with key
def longest_string_max(strings):
    longest = max(
        strings, key=len
    )  # max() function is used to find the maximum value in an iterable.
    shortest = min(
        strings, key=len
    )  # min() is the opposite of max(). The parameter key=len means that the function will determine the "maximum" based on the length (len) of each string
    return longest, shortest


strings = ["apple", "banana", "cherry", "date", "elderberry"]
print(longest_string_max(strings))  # Output: elderberry
