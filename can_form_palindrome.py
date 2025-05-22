from collections import Counter

def can_form_palindrome(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)

    return "YES" if odd_count <= 1 else "NO"
