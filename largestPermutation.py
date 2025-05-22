def largestPermutation(k, arr):
    n = len(arr)
    pos = {v: i for i, v in enumerate(arr)}  # her elemanın konumu

    for i in range(n):
        if k == 0:
            break
        max_val = n - i  # o pozisyonda olması gereken en büyük değer
        if arr[i] != max_val:
            max_idx = pos[max_val]
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            pos[arr[max_idx]] = max_idx
            pos[arr[i]] = i
            k -= 1
    return arr
