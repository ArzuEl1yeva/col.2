from itertools import combinations

def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for a, b in combinations(unique_chars, 2):
        filtered = [c for c in s if c == a or c == b]

        valid = True
        for i in range(1, len(filtered)):
            if filtered[i] == filtered[i - 1]:
                valid = False
                break

        if valid:
            max_length = max(max_length, len(filtered))

    return max_length
