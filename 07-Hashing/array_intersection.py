def intersection(arr1, arr2):

    set1 = set(arr1)
    result = set()

    for num in arr2:

        if num in set1:
            result.add(num)

    return result


# Example arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]


result = intersection(arr1, arr2)

print("Intersection:", result)
