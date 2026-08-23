# Question 129: Combination Sum


def combination_sum(candidates, target):

    result = []

    def backtrack(
        start,
        remaining,
        current
    ):

        # Target reached
        if remaining == 0:

            result.append(current.copy())

            return

        # Target exceeded
        if remaining < 0:
            return

        for i in range(
            start,
            len(candidates)
        ):

            num = candidates[i]

            # Choose
            current.append(num)

            # Explore
            backtrack(
                i,
                remaining - num,
                current
            )

            # Undo
            current.pop()

    backtrack(
        0,
        target,
        []
    )

    return result


candidates = [2, 3, 6, 7]
target = 7

print(
    "Combinations:",
    combination_sum(
        candidates,
        target
    )
)