#!/bin/python3

# a) Usando o módulo glob do Python, escreva código para listar todos os ficheiros de um diretório.

import glob

for i in glob.glob(r'*'):
    print(i)

# b) Altere o código para listar apenas ficheiros com a extensão .py (Python).

import glob

for i in glob.glob('*.py'):
    print(i)

# c) Altere o código para gravar o output num ficheiro de texto, para além de a imprimir no terminal.
    
