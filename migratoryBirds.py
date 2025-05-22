def migratoryBirds(arr):
    counts = {}
    for bird in arr:
        counts[bird] = counts.get(bird, 0) + 1

    max_count = max(counts.values())
    result = min(bird for bird, count in counts.items() if count == max_count)
    return result
