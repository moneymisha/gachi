# 1. Построим единичную матрицу
import numpy as np
Ns = 1 #номер по списку
N = Ns + 5
# print(I)

# f = n+N*m
f = lambda m,n: n+N*m 

# A = ANxN
A = np.identity(N) #создаём единичную матрицу
A = np.fromfunction (f,(N,N), dtype = int) #наполняем значения матрицы значениями спомощью функции
#print(A)

# Выписать: 1 строку / 2 столбец
a = A [0,:]
b = A [:,1]
#print (a)
#print (b)

# Найти скалярное произведение векторов a и b 
sc = np.dot(a,b)
#print (sc)

#Найти det, транспортированную, обратную
det = np.linalg.det (A) #детерминант матрицы
#print (det)

#транспонированная
T = np.transpose (A)
#print (T)

#Найти обратную матрицу
#A_inv = np.linalg.inv(A) #данная функция находит обратную матрицу
#print (A_inv) #тут выведет ошибку, т.к. детерминант равен нулю

# B=U*A*U^(-1)
U = np.random.randint (0, 20, (6, 6))
#print (U)
TU = np.transpose (U) #трансп.
#print(TU)
det_U = np.linalg.det(U) #дет.
#print (det_U) 
U_inv = (1/det_U)*TU #обр.
#print(U_inv)
B = U*A*U_inv
print(B)