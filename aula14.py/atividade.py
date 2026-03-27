#Exercício 1: Criar e ler um Arquivo**
# Renomeando o arquivo
os.rename('arquivo.txt', 'novo_nome.txt')
import os
with os.scandir('c:/Users/aluno/Desktop/aula12/') as entrada:
      for arquivo in entrada:
         print(f'Diretório encontrado: {arquivo.name}')


#Exemplo 2: Cria um Diretório**
import os
with os.scandir('C:/caminho da pasta(barra ao contrário)') as entrada:
    for arquivo in entrada:
         if arquivo.is_file():
             print(f'Arquivo encontrado: {arquivo.name}')



with os.scandir('C:/Users/aluno/Downloads/teste') as entrada :
       for n in entrada: 
           if 'teste.txt':
               with open('C:/Users/aluno/Downloads/teste/teste.txt', 'r')  as t:
                    content = t.read()

print(content) # fora do with, caso contrário ele irá se comportar
# como o loop    


#Exercício 3: Renomear um Diretório**
import os
os.rename('exemplo.txt', 'test5.txt')


#Exercício 4:  Listar Arquivos em um Diretório** 
import shutil
shutil.rmtree('c:/Users/aluno/Desktop/aula12/')


#Exercício 5:  Copiar Arquivos em um Diretório**
import os
with os.scandir('meu_diretorio') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')

#Exercício 6:  Remover**
import shutil
shutil.copytree('original', 'nome da copia')
# serve para pastas -> diretórios

