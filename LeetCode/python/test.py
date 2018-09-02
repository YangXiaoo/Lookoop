from queue import PriorityQueue

import time

q = PriorityQueue()

q.put((1, 'code'))
q.put((1, 'eat'))
q.put((1, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)
    time.sleep(1)