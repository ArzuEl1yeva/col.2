def pickingNumbers(a: list[int]) -> int:
    freq = [0] * 101

    for num in a:
        freq[num] += 1

    max_length = 0
    for i in range(1, 100):
        max_length = max(max_length, freq[i] + freq[i + 1])

    return max_length

