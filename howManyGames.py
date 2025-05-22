def howManyGames(p, d, m, s):
    games = 0
    current_price = p
    total_spent = 0

    while total_spent + current_price <= s:
        total_spent += current_price
        games += 1
        current_price = max(current_price - d, m)

    return games
