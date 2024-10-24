def freq_words_for_else():
    arr = [48, 7, 8, 8, 88, 8, 8, 9, 999, 67, 2, 2, 2, 2, 2]
    d = {}

    for i in arr:
        # `else` block is used if `i` was not found in `d`
        for key in d:
            if key == i:
                d[key] += 1
                break
        else:
            d[i] = 1

    print(arr)
    print(d)

    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")


freq_words_for_else()
