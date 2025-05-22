from collections import Counter

def isValidStringSameOccurence(s: str) -> str:
    freq = Counter(s)
    values = list(freq.values())
    counts = Counter(values)

    if len(counts) == 1:
        return "YES"  # tüm harfler eşit sıklıkta
    elif len(counts) == 2:
        key1, key2 = counts.keys()
        # 1 defa görünen karakter 1 kez fazla olabilir veya 1 kez görülen bir karakter olabilir
        if (counts[key1] == 1 and (key1 - 1 == key2 or key1 == 1)) or \
           (counts[key2] == 1 and (key2 - 1 == key1 or key2 == 1)):
            return "YES"
    return "NO"
