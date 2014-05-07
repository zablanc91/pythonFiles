def insertionSort(to_sort):
    i = 1
    while i < len(to_sort):
        j = i
        while j > 0 and to_sort[j] < to_sort[j-1]:
            a = to_sort[j]
            b = to_sort[j - 1]
            to_sort[j] = b
            to_sort[j - 1] = a
            j -= 1
        i += 1
    return to_sort
