""" 
Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8.

Estado da memória: 0
Opções:
(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
 """

estado_memoria = 0;

op = 0

print('='*15)
print('Calculadora')
print('='*15)

def calculadora():
    print('1- Somar')
    print('2- Subtrair')
    print('3- Multiplicar')
    print('4- Dividir')
    print('5- Limpar memória')
    print('6- Sair do programa')
    return int(input('Digite sua opção: '))

def numero(estado_memoria):
    print('='*15)
    print(f'Memória: {estado_memoria:.0f}')
    print('='*15)
    num = float(input('Digite o número desejado: '));
    return num

def somar(num, memoria):
    return memoria + num

def subtrair(num, memoria):
    return memoria - num

def multiplicar(num, memoria):
    return memoria * num

def dividir(num, memoria):
    return memoria / num

def limparmemoria(memoria):
    memoria = 0
    return memoria


while op != 6:
    op = calculadora()
    if op == 1:
        print('===== SOMAR =====')
        num = numero(estado_memoria);
        estado_memoria = somar(num, estado_memoria);
        print('='*15)
        print(f'Memória: {estado_memoria:.1f}');
        print('='*15)
        
    elif op == 2:
        print('===== SUBTRAIR =====')
        num = numero(estado_memoria);
        estado_memoria = subtrair(num, estado_memoria);
        print('='*15)
        print(f'Memória: {estado_memoria:.1f}');
        print('='*15)
    
    elif op == 3:
        print('===== MULTIPLICAR =====')
        num = numero(estado_memoria);
        estado_memoria = multiplicar(num, estado_memoria);
        print('='*15)
        print(f'Memória: {estado_memoria:.1f}');
        print('='*15)

    elif op == 4:
        print('===== DIVIDIR =====')
        num = numero(estado_memoria);
        estado_memoria = dividir(num, estado_memoria);
        print('='*15)
        print(f'Memória: {estado_memoria:.1f}');
        print('='*15)
    
    elif op == 5:
        print('===== LIMPAR =====')
        estado_memoria = limparmemoria(estado_memoria);
        print('='*15)
        print(f'Memória: {estado_memoria:.1f}');
        print('='*15)
else:
    print('Saindo....')