# summation = 0
# starting_index = 1
# index = starting_index
# maximum_index = 100

# while index < maximum_index:
    # summation += 1/index

# print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

# The three errors are:
# 1. The index should start at 1 instead of 0 to avoid division by zero.
# 2. The while loop condition should be <= maximum_index to include the maximum index.
# 3. The index should be incremented within the while loop.
# Summation by hand for Kmax=3: 1 + 1/2 + 1/3 = 11/6
# Code corrections by LLM: add 1/ to the denominator and start index from 1 for summation calculation.

summation = 0
starting_index = 1
index = starting_index
maximum_index = 3
while index <= maximum_index:
    summation += 1/index
    index += 1
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

summation = 0
starting_index = 1
index = starting_index
maximum_index = 100
while index <= maximum_index:
    summation += 1/index
    index += 1
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')