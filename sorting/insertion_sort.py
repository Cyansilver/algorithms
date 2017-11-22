def insertion_sort(input_data):
    for i in range(1, len(input_data)):
        j = i - 1
        key = input_data[i]

        while j >= 0 and key < input_data[j]:
            input_data[j + 1] = input_data[j]
            j = j - 1
        input_data[j + 1] = key

    return input_data

test = [31, 41, 59, 26, 41, 58]
print(test)
print(insertion_sort(test))
