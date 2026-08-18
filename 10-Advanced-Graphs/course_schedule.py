from collections import deque


def can_finish(num_courses, prerequisites):

    # Create graph
    graph = [
        []
        for _ in range(num_courses)
    ]

    # Calculate indegree
    indegree = [0] * num_courses

    # Build graph
    for course, prerequisite in prerequisites:

        graph[prerequisite].append(course)

        indegree[course] += 1

    # Courses with no prerequisites
    queue = deque()

    for course in range(num_courses):

        if indegree[course] == 0:

            queue.append(course)

    completed_courses = 0

    # BFS / Kahn's Algorithm
    while queue:

        course = queue.popleft()

        completed_courses += 1

        for next_course in graph[course]:

            indegree[next_course] -= 1

            if indegree[next_course] == 0:

                queue.append(next_course)

    # If all courses were completed
    return completed_courses == num_courses


# Example 1

num_courses = 4

prerequisites = [
    [1, 0],
    [2, 1],
    [3, 2]
]


if can_finish(num_courses, prerequisites):

    print("Can finish all courses: True")

else:

    print("Can finish all courses: False")