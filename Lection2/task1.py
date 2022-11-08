# num = '23,5'
# print([*filter(lambda c: c not in ['.',','], num)])

lst = [4,2,11,7]
number = 9
for i in range(len(lst)):
    z = number-lst[i]
    if z in lst[i+1:]:
        print([i, lst[i+1:].index(z)+i])
        break