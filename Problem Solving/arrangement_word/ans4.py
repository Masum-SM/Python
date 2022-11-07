def anagrams(lst):
    l_dict = {}
    for string in lst:
        sortLs = str(sorted(string))
        if sortLs in l_dict:
            l_dict[sortLs].append(string)
        else:
            l_dict[sortLs] = [string]
    print(list(l_dict.values()))

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
