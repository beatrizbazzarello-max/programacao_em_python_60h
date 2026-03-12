# atividade 1
numero = int(input('digite um numero:'))


match numero % 2:
    case 0:
        print('o numero é par')
    case _:
        print('o numero é impar')

# atividade 2
numero = int(input('digite um numero'))

match True:
    case _ if numero > 0:
        print('numero positivo')
    case _ if numero < 0:
        print('numero negativo')
    case _:
        print('numero é zero')

# atividade 3
texto = input('digite algo:')

match texto:
    case "":
        print('a string esta vazia')
    case _: 
        print('a string não esta vazia')

# atividade 4
numero = int(input('digite um numero:'))
match True:
    case _ if numero > 10:
        print('maior que 10')
    case _ if numero < 10:
        print('menor que 10')
    case _:
        print('igual a 10')

#  atividade 5

idade = int(input('digite a idade:'))
match True:
    case _ if idade <= 12:
        print('criança')  
    case _ if idade <= 17:
        print('adolescente')
    case _ if idade <= 35:
        print('jovem')
    case _ if idade < 65:
        print('adulto')
    case _:
        print('idoso')      