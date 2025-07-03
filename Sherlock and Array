def balancedSums(arr):
    total = 0
    for num in arr:
        total += num

    left_sum = 0

    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]
        if left_sum == right_sum:
            return "YES"
        left_sum += arr[i]

    return "NO"
