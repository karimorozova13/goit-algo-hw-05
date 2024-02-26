
def polynomial_hash(pattern, base=256, modulus=101):
    n = len(pattern)
    hash_val = 0

    for i, char in enumerate(pattern):
        power_of_base = pow(base, n - i -1) % modulus
        hash_val = (hash_val + ord(char) * power_of_base) % modulus

    return hash_val

def rabin_karp_search(text, pattern):
    M = len(pattern)
    N = len(text)

    base = 256
    modulus = 101

    pattern_hash =  polynomial_hash(pattern, base, modulus)
    cur_slice_hash = polynomial_hash(text[:M], base, modulus)

    h_multiplier = pow(base, M - 1) % modulus

    for i in range(N - M + 1): 
        if pattern_hash ==cur_slice_hash:
            if text[i:i + M] == pattern:
                return i
        if i < N - M:
            cur_slice_hash = (cur_slice_hash - ord(text[i]) * h_multiplier) % modulus
            cur_slice_hash = (cur_slice_hash * base + ord(text[i + M])) % modulus
            if cur_slice_hash < 0:
                cur_slice_hash += modulus
    return -1

             