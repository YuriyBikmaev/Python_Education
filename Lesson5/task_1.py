# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

source_str = "привет абв как абвышные дела?"
sub_str = "абв"

result = ' '.join(filter(lambda el: sub_str not in el, source_str.split()))
print(result)