# O(n) complexity.
def decidePermutation1(astr, bstr):

    found = False
    asc_a = [0] * 256
    asc_b = [0] * 256

    if len(astr) != len(bstr):
        return found
    else:
        for index in range(0, len(astr) - 1, 1):
            asc_a[ord(astr[index])] += 1
        for index in range(0, len(bstr) - 1, 1):
            asc_b[ord(bstr[index])] += 1

    if asc_a == asc_b:
        found = True
    return found


# Convert string to list O(n), sort in Python is O(n*logn), go through list O(n)
# total would be O(n*logn)
def decidePermutation2(astr, bstr):

    match = True

    if len(astr) != len(bstr):
        return False
    else:
        alist = list(astr)
        blist = list(bstr)

        alist.sort()
        blist.sort()

        index = 0

        while match and index < len(alist) - 1:
            if alist[index] != blist[index]:
                match = False
            index += 1

    return match

# depends on the cost of string sorting.
def decidePermutation3(astr, bstr):

    if len(astr) != len(bstr):
        return False
    return sorted(astr) == sorted(bstr)

astr = 'abbcdef'
bstr = 'eaabcdf'
print(decidePermutation1(astr, bstr))
print(decidePermutation2(astr, bstr))
print(decidePermutation3(astr, bstr))
