def rlSpace(astr):
    if astr == '':
        return ''
    else:
        bstr = astr.strip()
        alist = list(bstr.split(' '))
        print alist
        return ('%20').join(alist)

def rlSpace2(astr):
    if astr == '':
        return ''
    else:
        bstr = astr.strip()
        nbstr = bstr.replace(' ', '%20')
        return nbstr

astr = 'Mr John Smith    '
print(rlSpace(astr))
print(rlSpace2(astr))
