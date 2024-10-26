# least efficient algorithm


def freq_words_nested():
    arr = [48, 7, 8, 8, 88, 8, 8, 9, 999, 67, 2, 2, 2, 2, 2]
    counted = []  # Track which elements have been counted
    frequencies = []

    # Loop through each element to count frequency
    for i in arr:
        if i not in counted:
            count = 0
            for j in arr:
                if i == j:
                    count += 1
            frequencies.append((i, count))
            counted.append(i)

    # Sort by frequency in descending order
    sorted_items = sorted(frequencies, key=lambda x: x[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")


freq_words_nested()
