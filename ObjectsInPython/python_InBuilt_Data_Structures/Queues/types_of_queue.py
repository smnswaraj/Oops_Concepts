
# Common Types of Queues in Python
# Queue Type	   Description	                                Use Case
# FIFO Queue	   First-In-First-Out	                        Task scheduling, pipelines
# LIFO Queue	   Last-In-First-Out (Stack)	                Undo operations, backtracking
# Priority Queue   Elements served based on priority	        Task scheduling with priorities
# Deque	           Double-ended queue (both ends access)	    Fast insert/remove from both ends

from queue import Queue

q = Queue()
q.put("task1")
q.put("task2")
print(q.get())  # task1
print(q.get())  # task2

from queue import LifoQueue

stack = LifoQueue()
stack.put("undo1")
stack.put("undo2")
print(stack.get())  # undo2
print(stack.get())  # undo1


from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2, "medium"))
pq.put((1, "high"))
pq.put((3, "low"))
print(pq.get())  # (1, 'high')

from collections import deque

dq = deque()
dq.append("left")
dq.append("right")
dq.appendleft("front")
print(dq.pop())       # right
print(dq.popleft())   # front



