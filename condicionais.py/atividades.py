# atividade 1

numero = float(input('digite um numero:'))

if numero > 0:
    print('numero positivo')

elif numero < 0:
    print('numero negativo')

else:
    print('numero zero')

# atividade 2

idade = int(input('digite sua idade:'))
if idade >= 16:
    print('pode votar!')

else: 
    print('não pode votar!')

# atividade 3'

numero = int(input('digite um numero:'))
if numero % 2 == 0:
    print('numero par')

else:
    print('numero impar ')

# atividade 4

a = float(input('digite o primeiro lado:'))
b = float(input('digite o segundo lado:'))
c = float(input('digite o terceiro lado:'))
if a == b and b == c:
    print('triangulo equilatero')

elif a == b or a == c or b == c:
    print('triangulo isosceles')
else:
    print('triangulo escaleno')

# atividade 5

numero = int(input('digite um numero:'))
if numero % 5 == 0 and numero % 7 == 0:
    print('é multiplo de 5 e 7')

else:
    print('não é multiplo de 5 e 7')

# atividade 6

numero = float(input('digite um numero:'))
if numero > 0 and  numero > 10:
    print('o numero é positivo ')

else:
    print('nao e maior que 10')

# atividade 7

n = int(input('digite um numero:'))
if n % 3 == 0 and n % 5 == 0:
    print('é divisivel')
else:
    print('nao é divisivel')


