# atividade 1
import random
numero = random.randint(5, 10)
print(numero)

# atividade 2
def tres_numeros():
    return [random.randint(1,100) for _ in range(3)]
print(tres_numeros())

# atividade 3
def num_range():
    lista = list(range(10,31))
    return random.choice(lista)
print(num_range())

# atividade 4
def contagem_regressiva():
    for i in range(10,0,-1):
        print(i)
    print('fogo!')
contagem_regressiva()

# atividade 5
def soma_pares():
    numero = int(input('digite um numero:'))
    soma = 0
    for i in range(2, numero + 1,2):
        soma += i
    print('soma dos pares:', soma)
soma_pares()

# atividade 6
def tabuada():
    numero = int(input('digite um numero:'))
    for i in range(1,11):
        print(numero, 'x', i, '=', numero * i)
tabuada()

# atividade 7
def impares_reverso():
    for i in range(99, 1, -2):
        print(i)
impares_reverso()