import numpy as np


def mse_ab(a,b, x, y):
    return np.sum(((a+b*x)-y)**2)/len(x)

def mse_pa(a,b,x,y): 
    return 2*np.sum((a+b*x)-y)/len(x)

def mse_pb(a,b,x,y):
    return 2*np.sum(((a+b*x)-y)*x)/len(x)


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
alpha=5e-05

b=0.1
a=0.1
mseab_min=mse_ab(a,b,zp,ks)
i_min=1
b_min=b
a_min=a
   
for i in range(1000000):
    a-=alpha*mse_pa(a,b,zp,ks)
    b-=alpha*mse_pb(a,b,zp,ks)
    if i%50000==0:
        print(f'Итерация #{i}, a={a}, b={b}, mse={mse_ab(a, b, zp,ks)}')
    if mse_ab(a, b,zp,ks)>mseab_min:
        print(f'Итерация #{i_min}, a={a_min}, b={b_min}, mse={mseab_min},\nДостигнут минимум.')
        break
    else:
        mseab_min=mse_ab(a, b,zp,ks)
        i_min=i
        b_min=b
        a_min=a
print(f'a={a_min}\nb={b_min}')