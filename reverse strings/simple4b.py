# goal: Exercise 4: Reverse Words in a Sentence
# Input: "Hello World"
# Output: "World Hello"


def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


# Example usage
user_input = input("Type your sentence: ")
reverse_words = reverse_words(user_input)

print(f"This is the reverse sentence: {reverse_words}")  # Output: "World Hello"
print(f"This is the user input: {user_input}")  # Output: "World Hello"
