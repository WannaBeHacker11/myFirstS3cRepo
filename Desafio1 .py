#!/bin/python3
#coding: utf-8
# a) Usando o módulo glob do Python, escreva código para listar todos os ficheiros de um diretório.

import glob
lista_ficheiros=[]

for i in glob.glob('*'):
    lista_ficheiros.append(i)
    print(i)

# b) Altere o código para listar apenas ficheiros com a extensão .py (Python).
print("___________________________________________________")

for py in glob.glob("*.py"):
    lista_ficheiros.append(py)
    print(py)

# c) Altere o código para gravar o output num ficheiro de texto, para além de a imprimir no terminal.
    
import sys
sys.stdout = open("resultados.txt", "w")
print(lista_ficheiros)
sys.stdout.close()