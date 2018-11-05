

a = [3, 1, 9, 5, 4, 7]

def countsort(a, k):

    # auxillary array with first element unused
    c = []

    # output array initialized with None
    b = [0] * len(a)

    for i in range(0, k + 1, 1):
        c.append(0)

    for j in range(0, len(a), 1):
        c[a[j]] += 1

    for i in range(2, k + 1, 1):
        c[i] = c[i] + c[i-1]

    for i, e in reversed(list(enumerate(a))):
        b.insert(c[a[i]], a[i])
        c[a[i]] -= 1

    return(b)


b = countsort(a, max(a))

print(b)


