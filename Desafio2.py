#!/bin/python3

# a) Utilizando listas e um ciclo for, escreva código que guarde numa lista o endereço IP dos primeiros 50 dispositivos numa rede. No fim, imprima a lista de IPs.

import ipaddress
lista_IP=[]

ip_inicial = ipaddress.IPv4Address('192.168.56.0')
ip_final = ipaddress.IPv4Address('192.168.56.50')

for ip_int in range(int(ip_inicial), int(ip_final)):
    print(ipaddress.IPv4Address(ip_int))

# b) Escreva agora uma função para imprimir um IP por linha. Para o efeito, utilize um ciclo for. A lista deverá receber a variável ListaIPs.
print("________________________________________")
Lista_IPs=input("ListaIPs: ")

net = Lista_IPs.split('.')
total = open('Lista_IPs.txt', 'w')

for x in range(1,256):
    print(net[0] + '.' + net[1] +'.' + net[2] + '.' + str(x))
    total.write(net[0] + '.' + net[1] +'.' + net[2] + '.' + str(x) + '\n')

total.close()
