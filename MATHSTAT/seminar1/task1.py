import statfunction as st

# Задание 1
# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.

number_card = 52
take_card = 4

result_1_a = st.combinations(number_card//take_card, take_card) / \
    st.combinations(number_card, take_card)

print("\nРезультаты задания 1:")
print(f"Вероятность того, что все карты – крести = {round(result_1_a*100, 3)}%")

# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
tuz_card = 4

result_1_b = 1 - st.combinations(number_card - tuz_card, take_card) / \
    st.combinations(number_card, take_card)

print(f"Вероятность, что среди 4-х карт окажется хотя бы один туз = {round(result_1_b*100, 3)}%\n")


# Задание 2
# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

count_cutton = 10
count_cod = 3

result_2_a = 1/st.combinations(count_cutton,count_cod)

print("Результат задания 2:")
print(f"Вероятность того, что человек, не знающий код, откроет дверь с первой попытки = {round(result_2_a*100, 3)}%\n")

# Задание 3
# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

total_detail = 15
painted_detail = 9
take_detail = 3

result_3_a = st.combinations(painted_detail, take_detail) / \
    st.combinations(total_detail, take_detail)

print("Результат задания 3:")
print(f"Вероятность того, что все извлеченные детали окрашены = {round(result_3_a*100, 3)}%\n")


# Задание 4
# В лотерее 100 билетов. 
# Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

all_tickets = 100
win_tickets = 2
buy_tickets = 2


result_4_a = st.combinations(win_tickets, buy_tickets) / \
    st.combinations(all_tickets, buy_tickets)

print("Результат задания 4:")
print(f"Вероятность того, что 2 приобретенных билета окажутся выигрышными = {round(result_4_a*100, 3)}%\n")
