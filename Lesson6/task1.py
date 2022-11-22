data = open('input.txt', 'r')
water = int(data.readline())
relief = data.readline().split()
print(water)
print(relief)
index = 0
max = int(relief[index])
result = 0
for i in range(1, len(relief)):
    if max >= int(relief[i]): 
        result += max-int(relief[i])
    else:
        max = int(relief[i])
print(result)
# result = open('output.txt', 'w')
# result.write(f'{int(a)+int(b)}')
# result.close()