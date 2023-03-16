import numpy as np
import scipy.stats as st


football_players=np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

alpha=0.05

print('\n'+'Проверка данных на нормальность распределения')
fp_pvalue = st.shapiro(football_players).pvalue
print(f'Значение pvalue для футболистов = {fp_pvalue}')
hp_pvalue = st.shapiro(hockey_players).pvalue
print(f'Значение pvalue для хоккеистов = {hp_pvalue}')
wl_pvalue = st.shapiro(weightlifters).pvalue
print(f'Значение pvalue для штангистов = {wl_pvalue}')
if fp_pvalue<alpha or hp_pvalue<alpha or wl_pvalue<alpha:
    print('Данные распределены ненормально')
else: 
    print('Данные распределены нормально')
    print('Проверка равенства дисперсий')
    equality_of_variances = st.bartlett(football_players, hockey_players, weightlifters).pvalue
    print(equality_of_variances)
    if equality_of_variances<alpha:
        print('Принимаем, что дисперсии неравны')
    else:
        print('Принимаем, что дисперсии равны')
        result = st.f_oneway(football_players, hockey_players, weightlifters).pvalue
        if result<alpha:
            print('Есть различия среднего роста у спортсменов из разных групп')
        else:
            print('Нет различий среднего роста у спортсменов из разных групп')
