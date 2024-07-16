from collections import Any, Deque
from typing import deque

queue: Deque[Any] = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print('Removido', queue.popleft())
print('Removido', queue.popleft())
print('Removido', queue.popleft())
print('Removido', queue.popleft())


print('For inútil')
for item in queue:
    print(item)
