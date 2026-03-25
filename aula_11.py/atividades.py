# 1 - comparar 2 numeros (par ou impar)
def comparar (n1, n2):
    if n1 % 2 == 0:
        print('primeiro numero e par')
    else:
        print('o primeiro numero e impar')
    
    if n2 % 2 == 0:
        print('segundo numero e par')
    else:
        print('segundo numero e impar')
comparar(20, 5)

# 2 - multiplicar 3 numeros 
def multiplicar(n1, n2, n3):
    n1 = int(input('digite o primeiro numero'))
    n2 = int(input('digite o segundo numero'))
    n3 = int(input(' digite o terceiro numero'))

    resultado = n1 * n2 * n3 
    print('resultado:', resultado)
multiplicar(3,3,3,)

# atividade 3
def valor_elevado(f):
    print(f**2)
valor_elevado(5)

# atividade 4
def msg(idade):
    if idade == 18:
        print('idade especial: 18 anos')
msg(18)

# atividade 5
def calc_idade(ano):
    print(2026 - ano)
calc_idade(2010)

# atividade 6
def brasil_1999():

    ganhos = [1958, 1962,1970,1994,2002]
    op = int(input('ano:'))
    if op  in ganhos:
        print('brasil nao ganhou') 
    else:
        print('o brasil ganhou')
    
brasil_1999()