# preço dos quartos
simples = 100
duplo = 150
luxo = 250

# cliente 1
nome1 = input('nome do cliente 1:')
idade1 = int(input('idade:'))
quarto1 = input('tipo de quarto (simples, duplo, luxo:)')
dias1 = int(input('quantos dias vai ficar:'))

if quarto1 == 'simples':
    total1 = simples * dias1
elif quarto1 == 'duplo':
    total1 = duplo * dias1
else:
    total1 = luxo * dias1
    print('total a pagar:', total1)

# cliente 2

nome2 = input('nome do cliente 2:')
idade2 = int(input('idade:'))
quarto2 = input('tipo de quarto (simples, duplo, luxo:)')
dias2 = int(input('quantos dias vai ficar:'))

if quarto2 == 'simples':
    total2 = simples * dias2
elif quarto2 == 'duplo':
    total2 = duplo * dias2
else:
    total2 = luxo * dias2
    print('total a pagar:', total2)

# cliente 3

nome3 = input('nome do cliente 3:')
idade3 = int(input('idade:'))
quarto3 = input('tipo de quarto (simples, duplo, luxo:)')
dias3 = int(input('quantos dias vai ficar:'))

if quarto3 == 'simples':
    total3 = simples * dias3
elif quarto3 == 'duplo':
    total3 = duplo * dias3
else:
    total3 = luxo * dias3
    print('total a pagar:', total3)
