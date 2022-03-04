def flatten(l):
    res = []
    for i in l:
        if type(i) == list:
            res.extend(flatten(i))
        else:
            res.append(i)
    return res


def reverse(l):
    for i in l:
        if type(i) == list:
            reverse(i)
    l.reverse()


l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], [[[4]]], 5]
print(flatten(l))

l1 = [[1, 2], [3, 4], [5, 6, 7]]
reverse(l1)
print(l1)
