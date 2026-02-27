print('sistema de verificaçao de media')

nome = input('digite o nome do aluno:')

print('digite a nota do aluno', nome)
n1 = float(input('digite sua nota 1'))
n2 = float(input('digite sua nota 2'))
n3 = float(input('digite sua nota 3'))
print('***' * 15) 
print('media da aluno(a)', nome)
media = (n1 + n2 + n3) / 3
print('media do aluno(a)', nome)
print(media)

aprovada = media >= 7
recuperacao = media >=5 and media <7
reprovada = media < 5

print(f'''
situacao da aluno(a) {nome}

aprovada? - {aprovada}
reprovada? - {reprovada}
recuperacao? - {recuperacao}


''')