def reverse_string_ii(s, k):
    # Initialize an empty list to store the parts of the result
    result = []
    # Loop through the string in steps of 2k
    for i in range(0, len(s), 2 * k):
        # Get the current segment of the string
        segment = s[i : i + 2 * k]

        # Reverse the first k characters of the segment
        # If there are fewer than k characters left, reverse all of them
        to_reverse = segment[:k][::-1]

        # Append the reversed part to the result
        result.append(to_reverse)

        # Append the remaining characters from the segment as they are
        # If there are fewer than k characters left, this will still work correctly
        result.append(segment[k:])

    # Join the result list into a single string and return it
    return "".join(result)


# Example usage
print(reverse_string_ii("abcdefg", 2))  # Output: "bacdfeg"
print(reverse_string_ii("abcd", 2))  # Output: "bacd"
