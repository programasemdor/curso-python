#coding: utf-8

primo = True

#Entrada de dados
numero = int(input('Digite um número: '))

#Processamento
for i in range(2, numero):
    if numero % i == 0:
        primo = False

#Saída de dados
if primo:
    print('Número primo')
else:
    print('Não é primo')
