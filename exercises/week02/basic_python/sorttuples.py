def sorttuples(lst):
    return sorted(lst, key=lambda t: t[-1])

print(sorttuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))