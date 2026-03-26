# desafio 2
import statistics
empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

def analisar(nome,lista):
    print(f'\n{nome}')
    print('media:', statistics.mean(lista))
    print('mediana:', statistics.median(lista))
    print('moda:', statistics.mode(lista))
    print('desvio padrao:', round(statistics.stdev(lista), 2))

analisar('empresa1', empresa1)
analisar('empresa2', empresa2)
analisar('empresa3', empresa3)
analisar('empresa4', empresa4)

