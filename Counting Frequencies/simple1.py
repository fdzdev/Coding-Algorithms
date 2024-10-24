def freq_words():
    arr = [
        2,
        3,
        4,
        1,
        1,
        2,
        3,
        4,
        5,
        4,
        5,
        5,
        5,
        6,
        456,
        48,
        7,
        8,
        8,
        88,
        8,
        8,
        9,
        999,
        67,
        2,
        2,
        2,
        2,
        2,
    ]
    d = {}

    for i in arr:
        if i not in d:
            d[i] = 0
        d[i] += 1
    print(arr)
    print(d)

    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")


freq_words()
