import heapq

def merge_k_sorted(arrays):

    min_heap = []
    result = []

    # Put the first element of every array
    # into the heap
    for i in range(len(arrays)):

        if arrays[i]:

            heapq.heappush(
                min_heap,
                (arrays[i][0], i, 0)
            )

    # Process the heap
    while min_heap:

        value, array_index, element_index = \
            heapq.heappop(min_heap)

        result.append(value)

        # Move to the next element
        next_index = element_index + 1

        if next_index < len(arrays[array_index]):

            next_value = arrays[array_index][next_index]

            heapq.heappush(
                min_heap,
                (next_value, array_index, next_index)
            )

    return result


# Example
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

result = merge_k_sorted(arrays)

print("Merged array:", result)