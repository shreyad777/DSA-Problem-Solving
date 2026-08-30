def combination_sum(candidates, target):
    result = []
    def backtrack(
        start,
        remaining,
        current
    ):
        if remaining == 0:
            result.append(current.copy())
            return
        if remaining < 0:
            return

        for i in range(
            start,
            len(candidates)
        ):

            num = candidates[i]
            current.append(num)
            backtrack(
                i,
                remaining - num,
                current
            )
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