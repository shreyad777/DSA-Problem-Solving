class Solution:
    def carFleet(self, target, position, speed):
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
target = int(input("Enter target: "))
position = list(
    map(int, input("Enter positions: ").split())
)
speed = list(
    map(int, input("Enter speeds: ").split())
)

solution = Solution()

print(
    "Number of Car Fleets:",
    solution.carFleet(target, position, speed)
)