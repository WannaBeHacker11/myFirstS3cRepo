#!/bin/python3

# a) e b) Utilizando listas e um ciclo for, escreva código que guarde numa lista o endereço IP dos primeiros 50 dispositivos numa rede. No fim, imprima a lista de IPs ; Escreva agora uma função para imprimir um IP por linha. Para o efeito, utilize um ciclo for. A lista deverá receber a variável listaIPs como input.

import ipaddress
lista_IP=[]

ip_inicial = ipaddress.IPv4Address('192.168.56.0')
ip_final = ipaddress.IPv4Address('192.168.56.50')

for ip_int in range(int(ip_inicial), int(ip_final)):
    print(ipaddress.IPv4Address(ip_int))