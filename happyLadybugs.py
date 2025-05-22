from collections import Counter


def happyLadybugs(b):
    counts = Counter(b)

    if '_' not in counts:
        for i in range(1, len(b) - 1):
            if b[i] != b[i - 1] and b[i] != b[i + 1]:
                return "NO"
        return "YES"

    for bug, cnt in counts.items():
        if bug != '_' and cnt == 1:
            return "NO"

    return "YES"
