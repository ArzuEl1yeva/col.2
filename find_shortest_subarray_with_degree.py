from collections import defaultdict

def find_shortest_subarray_with_degree(nums):
    left = {}
    right = {}
    count = defaultdict(int)

    for i, num in enumerate(nums):
        if num not in left:
            left[num] = i
        right[num] = i
        count[num] += 1

    degree = max(count.values())
    min_length = len(nums)

    for num in count:
        if count[num] == degree:
            min_length = min(min_length, right[num] - left[num] + 1)

    return min_length
