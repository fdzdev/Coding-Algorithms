def freq_words_with_set():
    d = {}

    # Use a set to get unique values
    unique_elements = set(arr)
    for i in unique_elements:
        d[i] = arr.count(i)  # Count occurrences of each element in the list

    print(arr)
    print(d)

    # Different approach to filter
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")


user_input = input("type: ")
freq_words_with_set = freq_words_with_set(user_input)
print(freq_words_with_set)
