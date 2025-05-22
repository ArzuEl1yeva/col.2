def icecreamParlor(m, cost):
    seen = {}
    for i, price in enumerate(cost):
        target = m - price
        if target in seen:
            return [seen[target] + 1, i + 1]  # 1-based index
        seen[price] = i
