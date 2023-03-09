import numpy as np


def mse(b, x, y):
    return np.sum((b*x-y)**2)/len(x)

def mse_p(b,x,y):
    return (2/len(x))*np.sum((b*x-y)*x)

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

alpha=1e-06
b=0.1
mse_min=mse(b,zp,ks)
i_min=1
b_min=b
for i in range(10000):
    b-=alpha*mse_p(b,zp,ks)
    if i%100==0:
        print(f'Итерация #{i}, b={b}, mse={mse(b, zp,ks)}')
    if mse(b,zp,ks)>mse_min:
        print(f'Итерация #{i_min}, b={b_min}, mse={mse_min},\nДостигнут минимум.')
        break
    else:
        mse_min=mse(b,zp,ks)
        i_min=i
        b_min=b

print(b_min)