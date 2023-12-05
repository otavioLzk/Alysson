import random
""" 1 - Programa que armazena os nomes e idades de 10 pessoas em uma matriz, e imprime o nome da pessoa mais nova """

nomes = ['Beatriz','Rafael','Mariana','Thiago','Isabela','Lucas','Julia','Matheus','Juliana','Giseli']

L = 10
C = 2

matriz = []

for lin in range(L):
    matriz.append([nomes[lin], random.randint(1, 100)])

menor = [matriz[0][0], matriz[0][1]]

for lin in matriz:
    if (lin[1] <= menor[1]):
        menor = [lin[0], lin[1]]

print('********* MATRIZ *********\n')

for linha in matriz:
    for elemento in linha:
        print(elemento, end='\t')
    print()

print(f"\nA pessoa mais nova é: {menor[0]}, com {menor[1]} anos.")