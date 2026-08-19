def climb_stairs(n):

    if n <= 2:
        return n

    previous_two = 1
    previous_one = 2

    for i in range(3, n + 1):

        current = previous_one + previous_two

        previous_two = previous_one
        previous_one = current

    return previous_one


n = 5

print("Number of ways:", climb_stairs(n))