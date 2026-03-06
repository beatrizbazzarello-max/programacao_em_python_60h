import random

banco_perguntas = [ 
   'pergunta: qual e o maior planeta do sistema solar?',
    'perguntas: qual pais tem o formato de uma bota?',
    'pergunta: quantos continentes existem na terra?'
]


respostas = [
    '',
    ' jupiter.',
    ' italia.',
    ' sete.',
]

print('jogo de perguntas acerte e ganhe 1 milhao')
print('***' * 20)
maquina = random.choice(banco_perguntas)
id_maquina = banco_perguntas.index(maquina)
print(maquina)
print('***' * 20)

print('escolha sua resposta')
r = input(f'{respostas[1]} , {respostas[2]} , {respostas[3]}')

if r == id_maquina:
    print('acertou em cheio')
else:
    print('errou feio')