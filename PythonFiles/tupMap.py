def tupMap(func, tup):
    newTup = ( )
    for item in tup:
        newTup += (func(item),)
    return newTup
