# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from cmath import pi

def pi_accuracy(n, result=0.0):
    for i in range(n+1):
        result += 16**(-i)*((4/(8*i+1))-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6)))
    return result

def pi_accuracy_bellara(n, result=0):
    for i in range(n+1):
        result += (-1)**i/2**(10*i)*(-(2**5/(4*i+1))-(1/(4*i+3))+(2**8/(10*i+1))-(2**6/(10*i+3))-(2**2/(10*i+5))-(2**2/(10*i+7))+(1/(10*i+9)))
    return result*1/2**6

print(pi)
accuracy = 1
print(f'{pi_accuracy(accuracy)}')
print(f'{pi_accuracy_bellara(accuracy)}')

