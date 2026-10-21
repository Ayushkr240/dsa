import heapq
from collections import Counter

def huffman(text):
    freq = Counter(text)
    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for pair in left[1:]:
            pair[1] = "0" + pair[1]

        for pair in right[1:]:
            pair[1] = "1" + pair[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    return heap[0][1:]


text = "aabac"
codes = huffman(text)

print("Character : Huffman Code")
for char, code in codes:
    print(char, ":", code)