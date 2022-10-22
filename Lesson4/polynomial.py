def create_polynomial(ratio_list):
    result = ''
    for i, j in enumerate(ratio_list):
        if i == 0:
            k = ''
        elif i == 1:
            k = 'x'
        else:
            k = f'x^{i}'
        if j > 1:
            result = f'{j}*' + k + ' ' + result
        elif j == 1:
            result += k + ' ' + result
    if result[-2] == '*':
        result = result[:-2] + ''
    return ' + '.join(result.split())+' = 0'


def write_polynomial_in_file(file, poly):
    data = open(file, 'w', encoding='utf-8')
    data.write(poly)
    data.close


def sum_polynomial(poly_1, poly_2):
    result = []
    if len(poly_1) == len(poly_2):
        for i in range(len(poly_1)):
            result.append(int(poly_1[i])+int(poly_1[i]))
    return result


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_file_polynomial(file):
    result = ''
    data = open(file, 'r', encoding='utf-8')
    result = data.readline()
    data.close
    return result
