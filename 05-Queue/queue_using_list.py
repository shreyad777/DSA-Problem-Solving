queue = []


queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

removed = queue.pop(0)

print("Removed:", removed)


print("Queue after dequeue:", queue)

if queue:
    print("Front:", queue[0])
else:
    print("Queue is empty")

if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")