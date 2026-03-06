# produtos do e-commerce
produtos = {
    'livros': {'nome': 'coraline', 'preço': 50},
    'tablet': {'nome': 'tablet samsung', 'preço': 1200},
    'fone': {'nome': 'fone JBL', 'preco': 150}
}

# compras 
compra1 = produtos['livros']['preço']
compra2 = produtos['fone']['preco']

# valor total 
total = compra1 + compra2

# mostrar compras
print('livro comprado:', produtos['livros']['nome'])
print('fone comprado:', produtos['fone']['nome'])

# mostrar valor da compra
print('valor da compra: R$', total)