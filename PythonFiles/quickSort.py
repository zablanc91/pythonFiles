#let the first element in arr serve as the pivot
#sorts a set with unique elements

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + [x for x in arr[0:] if x == arr[0]] + qsort([x for x in arr[1:] if x > arr[0]])
