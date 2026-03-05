import sys


def insertion_sort_with_step(nums: list[int], step_limit: int) -> int:
    step = 0
    change_index = 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                step += i - j
    return -1


length, step_count = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
print(insertion_sort_with_step(numbers, step_count))
