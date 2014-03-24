# O(N**2)
def checkUnique0(alist):

    for char in alist:
        found = 0
        for char2 in alist:
            if char == char2:
                found += 1
            if found > 1:
                return False
    return True


# O(N) go through list twice
def checkUnique1(alist):

    chalist = [0] * 256

    index = 0

    Unique = True

    while index < len(alist) - 1:
        chalist[ord(alist[index])] += 1
        index += 1

    for char in chalist:
        if char > 1:
            Unique = False
    return Unique


# O(N) + 1 = O(N). Set() function has O(n)
def checkUnique2(alist):
    return len(set(alist)) == len(alist)


# convert string to list is O(N)
# sorting in Python takes O(n*logn)
# for loop O(N)
# Total is O(n*logn)
def checkUnique3(alist):
    newlist = list(alist)
    newlist.sort()
    for i in range(len(newlist) - 1):
        if newlist[i] == newlist[i + 1]:
            return False
    return True


alist = 'abcdabc'
print(checkUnique0(alist))
print(checkUnique1(alist))
print(checkUnique2(alist))
print(checkUnique3(alist))
