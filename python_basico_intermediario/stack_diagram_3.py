"""
Como falamos em listas, podemos fazer iterações na pilha normalmente, tanto com
while quanto com for.
"""

from copy import deepcopy
from typing import List

# Uma pilha vazia
stack: List[List[str]] = []

# Append adiciona elementos no topo da pilha
stack.append(['A'])
stack.append(['B'])
stack.append(['C'])

print('FOR:')
for item in stack[::-1]:
    print(item)

stack_copy = deepcopy(stack)

print('\nWHILE:')
while stack_copy:
    item = stack_copy.pop()
    item += ['Manipulei']
    print(item)

print('\nSUA PILHA:', stack)