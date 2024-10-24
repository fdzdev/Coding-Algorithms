from collections import defaultdict


def freq_words_defaultdict():
    arr = [48, 7, 8, 8, 88, 8, 8, 9, 999, 67, 2, 2, 2, 2, 2]
    d = defaultdict(int)

    # Loop through the array
    for i in arr:
        d[i] += 1

    print(arr)
    print(dict(d))

    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")


freq_words_defaultdict()
