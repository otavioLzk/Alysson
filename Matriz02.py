import random

""" 2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
número k. Imprima a matriz na tela antes e depois da multiplicação.
ex:     
input
|  4     6    9 |
|  3     2    7 |
|  1     2    5 |

ouput, suponha k = 5
|  20     6     9 |
|  3       10    7 |
|  1     2      25 | """

l = 3

k = int(input('Digite um número que deseja multiplicar a diagonal principal da matriz: '))

matriz = []

for i in range(l):
    num = []
    for j in range(l):
        num.append(random.randint(1, 100))
    matriz.append(num)

print('********* MATRIZ *********\n')

for i in matriz:
    for j in i:
        print(j, end='\t')
    print()

for i in range(l):
    for j in range(l):
        if (i == j):
            matriz[i][j] *= k

print('\n********* MATRIZ ATUALIZADA *********\n')

for i in matriz:
    for j in i:
        print(j, end='\t')
    print()