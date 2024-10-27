# goal: Exercise 4: Reverse Words in a Sentence
# Input: "Hello World"
# Output: "World Hello"


def reverse_words(sentence):
    # Define a function named reverse_words that takes a single parameter 'sentence', which is expected to be a string.

    words = sentence.split()
    # Use the split() method to divide the sentence into a list of words based on whitespace.
    # For example, "Hello World" becomes ['Hello', 'World'].

    reversed_words = words[::-1]
    # Use slicing to reverse the list of words.
    # The slice [::-1] creates a new list that starts from the end to the beginning.
    # So, ['Hello', 'World'] becomes ['World', 'Hello'].

    return " ".join(reversed_words)
    # Use the join() method to concatenate the reversed list of words into a single string,
    # separating each word with a space.
    # This converts ['World', 'Hello'] back into "World Hello".


# Example usage
print(reverse_words("Hello World"))  # Output: "World Hello"
# Call the function with the sentence "Hello World" and print the result.
# The output will be "World Hello", which is the original sentence with the words reversed.
