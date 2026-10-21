
# def rabinKarp(text, pattern):
#     n = len(text)
#     m = len(pattern)

#     pattern_hash = sum(ord(c) for c in pattern)
#     text_hash = sum(ord(c) for c in text[:m])

#     for i in range(n - m + 1):
#         if pattern_hash == text_hash:
#             if text[i:i + m] == pattern:
#                 print("Pattern found at index", i)

#         if i < n - m:
#             text_hash = text_hash - ord(text[i]) + ord(text[i + m])


def rabin_karp(text,pattern):
    n,m=len(text),len(pattern)

    if m == 0 or m > n:
        return

    text_hash= sum(ord(c) for c in text[:m])
    pattern_hash= sum(ord(c) for c in pattern)

    for i in range(n-m+1):
        if text_hash==pattern_hash:
            if text[i:i+m]==pattern:
                print("Pattern found at ",i)
                return


        if i < n-m:
            text_hash=text_hash - ord(text[i])+ ord(text[i+m])


text = "AABAACAADAABAABA"
pattern = "BA"
rabin_karp(text,pattern)