def find_longest_chain(pairs):
    pairs.sort(key=lambda pair: pair[1])
    count = 0
    current_end = float("-inf")
    for start, end in pairs:
        if start > current_end:
            count += 1
            current_end = end
    return count
n = int(input("Enter number of pairs: "))
pairs = []
for i in range(n):
    a, b = map(int, input(f"Enter pair {i + 1}: ").split())
    pairs.append([a, b])
print("Maximum Length of Chain:", find_longest_chain(pairs))