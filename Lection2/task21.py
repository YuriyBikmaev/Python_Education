lst = ['H', 'G', 'h', '1', '4']
start = 32
for i in range(len(lst)):
    while True:
        if chr(start) in lst:
            lst[i], lst[lst.index(chr(start))] = lst[lst.index(chr(start))], lst[i]
            start += 1
            break
        else:
            start += 1
print(lst)
