import statfunction as st

# Задание 1
# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

print("\nРезультат задания 1:")
print(
    f"Вероятность того, что стрелок попадет в цель ровно 85 раз = {st.bernuli(100,85,0.8):.4f}")


# Задание 2
# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день?
# Какова вероятность, что перегорят ровно две?

print("\nРезультаты задания 2:")
print(
    f"Вероятность того, что ни одна из них не перегорит в первый день = {st.poison(0,5000,0.0004):.4f}")
print(f"Вероятность того, что перегорят ровно две = {st.poison(2,5000,0.0004):.4f}")

# Задание 3
# Монету подбросили 144 раза.
# Какова вероятность, что орел выпадет ровно 70 раз?

print("\nРезультат задания 3:")
print(
    f"Вероятность того, что орел выпадет ровно 70 раз = {st.bernuli(144,70,0.5):.4f}")

# Задание 4
# В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?

all_ball_box1 = 10
white_ball_box1 = 7
all_ball_box2 = 11
white_ball_box2 = 9

take_ball_from_box = 2


print("\nРезультаты задания 4:")

n_box1=st.combinations(all_ball_box1,take_ball_from_box)
n_box2=st.combinations(all_ball_box2,take_ball_from_box)
result_1 = st.combinations(white_ball_box1, take_ball_from_box) / n_box1 * \
    st.combinations(white_ball_box2, take_ball_from_box) / n_box2
print(f"Вероятность того, что все мячи белые = {result_1:.4f}")

m_a=st.combinations(7,2)
m_b=st.combinations(2,2)
m_c=st.combinations(7,1)*st.combinations(3,1)
m_d=st.combinations(9,1)*st.combinations(2,1)
m_e=st.combinations(3,2)
m_f=st.combinations(9,2)
result_2 = m_a/n_box1*m_b/n_box2+m_c/n_box1*m_d/n_box2+m_e/n_box1*m_f/n_box2

print(f"Вероятность того, что ровно два мяча белые = {result_2:.4f}")

result_3 = 1 - st.combinations(all_ball_box1-white_ball_box1, take_ball_from_box) / st.combinations(all_ball_box1, take_ball_from_box) * \
    st.combinations(all_ball_box2-white_ball_box2, take_ball_from_box) / st.combinations(all_ball_box2, take_ball_from_box)
print(
    f"Вероятность того, что хотя бы один мяч белый = {result_3:.4f}\n")
