def luckBalance(k: int, contests: list[list[int]]) -> int:
    important = []
    luck = 0

    for l, t in contests:
        if t == 1:
            important.append(l)
        else:
            luck += l

    important.sort(reverse=True)

    luck += sum(important[:k])

    luck -= sum(important[k:])

    return luck

