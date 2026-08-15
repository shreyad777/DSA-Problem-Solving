def find_union(arr1, arr2):

    union = set()

    for num in arr1:
        union.add(num)

    for num in arr2:
        union.add(num)

    return union

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

result = find_union(arr1, arr2)

print("Union:", result)