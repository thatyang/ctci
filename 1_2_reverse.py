# implement a function that reverses a string

#Strings are immutable so each concat creates a new presentation
def rev1(astr):
    nstr = ''
    for index in range(len(astr) - 1, -1, -1):
        nstr += astr[index]
    return nstr
#Use list, does not create new presentation
def rev2(astr):
    nstr = []
    for index in range(len(astr) - 1, -1, -1):
        nstr.append(astr[index])

    return ('').join(nstr)

def rev3(astr):
    return ('').join([astr[index] for index in range(len(astr) - 1, -1, -1)])

def rev4(astr):
    if astr != '':
        return astr[-1:] + rev4(astr[:-1])
    else:
        return ''

astr = 'abcdefg'
print(rev1(astr))
print(rev2(astr))
print(rev3(astr))
print(rev4(astr))

