def alternate(s: str) -> int:
    unique_chars = []
    for c in s:
        if c not in unique_chars:
            unique_chars.append(c)

    max_length = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            a = unique_chars[i]
            b = unique_chars[j]
            filtered = ''
            for ch in s:
                if ch == a or ch == b:
                    filtered += ch
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    valid = False
                    break

            if valid:
                max_length = max(max_length, len(filtered))

    return max_length
