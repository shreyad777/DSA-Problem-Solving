def heapify(arr, n, i):

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If parent is not largest, swap
    if largest != i:

        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):

        heapify(arr, n, i)

    # Step 2: Extract elements
    for i in range(n - 1, 0, -1):

        # Move maximum to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Reduce heap size
        heapify(arr, i, 0)


# Example
arr = [5, 3, 8, 4, 2]

print("Before sorting:", arr)

heap_sort(arr)

print("After sorting:", arr)