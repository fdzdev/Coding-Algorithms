#  Using a Simple Loop
def longest_string_loop(strings):
    longest = ""  # empty string

    for string in strings:  # iterates through all strings
        if len(string) > len(longest):
            longest = string
    return longest


strings = ["apple", "banana", "cherry", "date", "elderberry", "elderberryelderberry"]
print(longest_string_loop(strings))
