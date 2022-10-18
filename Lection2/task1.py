num = '23,5'
print([*filter(lambda c: c not in ['.',','], num)])
