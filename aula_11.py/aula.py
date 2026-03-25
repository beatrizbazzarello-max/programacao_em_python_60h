
# atividade 1

try:
    numero = int(input('digite um numero inteiro:'))
    print('voce digitou:', numero)
except:
    print('erro! nao e um numero inteiro')
                 
# atividade 2

try:
    n1 = int(input('digite o primeiro numero:'))
    n2 = int(input('digite o segundo numero:'))
    resultado = n1 / n2
    print('resultado:', resultado)
except ZeroDivisionError:
    print('erro! nao pode dividir por 0:')

# atividade 3

try:
    l = [1,2,3]
    print(l[2])
except IndexError:
    print('erro! indice invalido')
