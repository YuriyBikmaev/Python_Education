# Напишите программу, удаляющую из текста все слова, содержащие "абв".


source_str = "привет абв как абвышные дела?"
sub_str = "абв"

result = source_str.split()
res = ' '.join(filter(lambda el: sub_str not in el, result))
print(res)