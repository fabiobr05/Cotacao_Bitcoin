# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:55:29 2021
Program: bitcoin.py
@author: Fabio Batista Rodrigues
"""
# Este programa recebe dados atuais do bitcoin por um determinado tempo e imprimi 
# ao final um grafico 
# Ou seja, enquanto estiver rodando recebe e armazena 

# Importar bibliotecas
import requests as r
import time
from tqdm import tqdm

# receber numero de dados que deseja armazenar
numero_dados = int(input('Insira o numero de linhas que deseja: '))
# Contabilizar o tempo de execuçao do programa
# tempo inicial
inicio = time.time()
# Inicializar lista
dados = [[0]*2 for i in range(numero_dados)]
# Inserir na primeira linha o rotulo das colunas
dados.insert(0,['Tempo', 'Cotacao'])
# Loop que armazena os dados coletados de nlinhas na lista dados
for i in tqdm(range(1, numero_dados+1), colour='blue',desc='REQUISITANDO E ARMAZENANDO' ):
    url = "https://www.mercadobitcoin.net/api/BTC/ticker/"
    # Quardar numa variavel resposta
    resp = r.get(url)
    # Quardar dados retornados da API em uma variavel
    raw_data = resp.json() # Do tipo dicionario
    # Armazenar os dados de raw_data em uma lista dados
    # Coletar tempo atual
    tempo = time.strftime('%H:%M:%S', time.localtime())
    # Armazenar
    dados[i][0] = tempo
    dados[i][1] = float(raw_data['ticker']['last'])
    # Aguardar 3 segundos
    time.sleep(5)
    
print("\nDados coletados e armazenados")

# Criar um documento csv e armazenando os dados apenas para utilizaçao posterior
# Antes de fazer a converçao dos dados vamos armzenar eles em um arquivo csv
import csv
# Criando arquivo e armazenar o que esta em final_data e colocar la
with open('dados_bitcoin.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(dados)

print('Documento Criado')

# Plotar grafico
import matplotlib.pyplot

y = []
for i in range(1, len(dados)):
    y.append(dados[i][1])
x = []
for i in range(1, len(dados)):
    x.append(dados[i][0])
    
matplotlib.pyplot.title('Cotaçao BitCoin')
matplotlib.pyplot.xlabel('Horario de Campo Grande MS')
matplotlib.pyplot.ylabel('Cotação $')
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

# Contabilizar o tempo
fim = time.time()
print(f'O tempo de execuçao foi de {fim - inicio} segundos')

