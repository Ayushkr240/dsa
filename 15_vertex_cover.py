def vectex_cover(edges):

    cover=set()
    for u,v in edges:
        if u not in cover and v not in cover:
            cover.add(u)
            cover.add(v)

    return cover


if __name__ == "__main__":
    edges = [(1, 2), (2, 4),
             (3, 4), (4, 5), (5, 6)]

    cover = vectex_cover(edges)

    print("Approximate vertex cover:", cover)
    print("Cover size:", len(cover))