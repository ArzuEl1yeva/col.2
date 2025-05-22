def repeatedString(s: str, n: int) -> int:
    count_a = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    total_a = full_repeats * count_a + s[:remainder].count('a')
    return total_a
