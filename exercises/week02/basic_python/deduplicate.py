def deduplicate(lst):
    return list(dict.fromkeys(lst))

print(deduplicate([1, 2, 3, 3, 2, 2, 4]))