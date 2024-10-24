from collections import Counter


def freq_words_counter():
    arr = [48, 7, 8, 8, 88, 8, 8, 9, 999, 67, 2, 2, 2, 2, 2]

    d = Counter(arr)
    print(arr)
    print(d)

    sorted_items = d.most_common()
    # Returns elements sorted by frequency in descending order
    for key, value in sorted_items:
        print(f"{key}: {value}")


freq_words_counter()
