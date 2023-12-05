import random
""" Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar:

a) De quem foi a melhor volta da prova, e em que volta
b) Classificação final em ordem (1º o campeão)
c) Qual foi a volta com a média mais rápida """

l = 6
c = 10

matriz = []
nomes = ['Julia','Rafael','Thiago','Giseli','Maria','Maya']

# Criar matriz com números aleatórios

for i in range(l):
    num = []
    for j in range(c):
        num.append(random.randint(100, 200))
    matriz.append([nomes[i], num])

# Matriz principal

print('\n', '*' * 19, "MATRIZ PRINCIPAL", '*' * 20, '\n')

print('Corredores        1    2    3    4    5    6    7    8    9    10')

for i in matriz:
    for j in i:
        print(j, end='\t\t')
    print()

# Descobrir qual o menor valor

menor = [matriz[0][0], matriz[0][1][0]]

for i in range(l):
    for j in range(c):
        if (matriz[i][1][j] <= menor[1]):
            menor = [matriz[i][0], matriz[i][1][j], j+1]

print(f'\na) A melhor volta da prova foi de {menor[0]}, na volta {menor[2]}.\n')

# Crir matriz com soma de valores

matriz2 = []

for i in range(l):
    lista = []
    soma = 0
    for j in range(c):
        soma += matriz[i][1][j]
    matriz2.append([matriz[i][0], soma])

# Ordenação

print('b) Classificação final: \n')

lista = []

for i in range(l):
    lista.append(matriz2[i][1])

lista_ordenada = sorted(lista)

index = 1
for num in lista_ordenada:
    for elemento in matriz2:
        if (elemento[1] == num):
            print(f'{index}º lugar: {elemento[0]}')
    index +=1

# Volta com média mais rápida

voltas = []

for i in range(c):
    soma = 0
    for elemento in matriz:
        soma += elemento[1][i]
    voltas.append(soma/l)

print(f'\nc) A volta com média mais rápida foi a {voltas.index(min(voltas))+1}º, com {min(voltas):.2f}s de média!\n')
