def k_closest(points, k):
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
