from collections import deque
import numpy as np
import re

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Separating the Original Stack from the Moves
for index, row in enumerate(lines):
    if row == '\n':
        cutoff = index

original_stack = lines[:cutoff]
moves = lines[cutoff+1:]

# Reintepreting the original_stacks as an array
## Building an Empty Array
n_cols = len(original_stack[-1].strip().split('  '))
n_rows = cutoff-1
original_stack_array = np.empty((n_rows, n_cols), dtype=object)

# Finding the Index of the Columns
index_map = {column: index for index, column in enumerate(original_stack[-1]) if column not in [" ", '\n']}

# Iterating through the original_stack
for i in range(cutoff-1):
    j = original_stack[i]
    print(i, j)
    for key in index_map:
        entry = j[index_map[key]]
        original_stack_array[(int(i), int(key)-1)] = entry

print(original_stack_array)

# Creating a Dictionary of Stacks
stack_dict = {key: deque() for key in index_map}

# Reading through each Column of the Array to build each Stack
for i in range(n_cols):
    crate = list(original_stack_array[:, i])

    for crate in reversed(crate):
        if crate != ' ':
            stack_dict[str(i+1)].append(crate)

# Going through the Moves
for move in moves:
    n_moves, from_stack, to_stack = re.findall('[0-9]+', move)

    # Part 1 (1 Crate at a Time)
    # for _ in range(1, int(n_moves)+1):
    #     stack_dict[to_stack].append(stack_dict[from_stack].pop())

    # Part 2 (Multiple Crates at a Time)
    temp_stack = deque()
    for _ in range(1, int(n_moves)+1):
        temp_stack.append(stack_dict[from_stack].pop())
    
    for _ in range(len(temp_stack)):
        stack_dict[to_stack].append(temp_stack.pop())

# Getting the top crate of each stack
top_values = ''.join(stack[-1] for stack in stack_dict.values())
print(top_values)