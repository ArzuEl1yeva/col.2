def caesarCipher(s, k):
    result = []
    k = k % 26

    for char in s:
        if char.islower():
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        elif char.isupper():
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)
