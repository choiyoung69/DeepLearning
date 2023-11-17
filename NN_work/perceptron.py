# -*- coding: KOREAN(EUC-KR) -*-
#perceptron의 output을 구하는 코드

x = [[0.3, 0.1, 0.8],
     [0.5, 0.6, 0.3],
     [0.1, 0.2, 0.1],
     [0.8, 0.7, 0.7],
     [0.5, 0.5, 0.6]]

w = [0.2, -0.1, 0.3]

b = 0
seta = 0

for i in range(len(x)):
    v = x[i][0]*w[0] + x[i][1]*w[1] + x[i][2]*w[2] + b
    if v <= seta:
        y = 0
    elif v > seta:
        y = v
    print("%d번째에서 y는 %.3f" %(i+1, y))