def minimum_distances(a: list[int]) -> int:
    indices = {}
    min_dist = float('inf')

    for i, val in enumerate(a):
        if val in indices:
            dist = i - indices[val]
            if dist < min_dist:
                min_dist = dist
        indices[val] = i

    return min_dist if min_dist != float('inf') else -1
