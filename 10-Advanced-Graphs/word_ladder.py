from collections import deque


def word_ladder(begin_word, end_word, word_list):

    word_set = set(word_list)

    # If end word is not available
    if end_word not in word_set:
        return 0

    queue = deque()

    # Store word and number of steps
    queue.append((begin_word, 1))

    # Avoid visiting the same word again
    visited = set()
    visited.add(begin_word)

    while queue:

        current_word, steps = queue.popleft()

        # Target reached
        if current_word == end_word:
            return steps

        # Change every character
        for i in range(len(current_word)):

            for char in "abcdefghijklmnopqrstuvwxyz":

                new_word = (
                    current_word[:i]
                    + char
                    + current_word[i + 1:]
                )

                # Valid unvisited word
                if (
                    new_word in word_set
                    and new_word not in visited
                ):

                    visited.add(new_word)

                    queue.append(
                        (new_word, steps + 1)
                    )

    # Transformation impossible
    return 0


# Example

begin_word = "hit"

end_word = "cog"

word_list = [
    "hot",
    "dot",
    "dog",
    "lot",
    "log",
    "cog"
]


result = word_ladder(
    begin_word,
    end_word,
    word_list
)

print("Shortest Transformation Length:", result)