# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

from itertools import count, groupby
import re
from tokenize import group


def read_file(file):
    result = []
    data_file = open(file, 'r', encoding='utf8')
    result = data_file.readlines()
    data_file.close
    return result


def write_file(file, list_lines):
    data_file = open(file, 'w', encoding='utf8')
    data_file.writelines(list_lines)
    data_file.close


def encoding_rle(file):
    lines = read_file(file)
    res = []
    for line in lines:
        res += [''.join([f'{len(list(k))}{char}' for char, k in groupby(line)])]
    write_file(file, res)


def decoding_rle(file):
    lines = read_file(file)
    result = []
    for line in lines:
        i = 0
        midle_res = []
        while i < len(line):
            s_int = ''
            a = line[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i<len(line):
                    a = line[i]
                else:
                    break
            if s_int != '':
                midle_res.append((int(s_int), line[i]))
            i += 1
        result.append(''.join([f'{c*k}' for c, k in midle_res])) 
    write_file(file, result)

            

file_path = 'RLE_coding_task_4.txt'
print('='*20 + '\nИсходный файл:')
print(*read_file(file_path))
print('='*20 + '\nЗакодированная информация:')
encoding_rle(file_path)
print(*read_file(file_path))

print('='*20 + '\nРаскодированная информация:')
decoding_rle(file_path)
print(*read_file(file_path))
print('='*20)
