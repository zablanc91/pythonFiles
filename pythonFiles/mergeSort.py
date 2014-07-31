def mergeSort(x):
    if len(x) < 2:
        return x
    result = []
    
    mid = int(len(x)/2)
    y = mergeSort(x[:mid])
    z= mergeSort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)

    result += y
    result += z
    return result
