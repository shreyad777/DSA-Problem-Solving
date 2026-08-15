def two_sum(arr, target):

    seen = {}

    for i in range(len(arr)):

        current = arr[i]

        needed = target - current

        if needed in seen:
            return [seen[needed], i]

        seen[current] = i

    return []