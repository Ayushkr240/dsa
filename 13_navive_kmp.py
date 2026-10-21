def naive_search(text , pattern):
    n=len(text)
    m=len(pattern)

    for i in range(n-m+1):
        j=0
        while j<m    and (text[i+j]==pattern[j]):
            j+=1

        if j==m:
            print("Pattern is found at ",i)
            


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)

    # Create LPS array
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    # Search pattern in text
    i = j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print("Pattern found at index", i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

kmp(text, pattern)

text = "ABABC"
pattern = "ABC"

naive_search(text, pattern)


