pessoas = int(input("Índice de contágio: "))
if pessoas < 5:    
    print("Baixo")
elif pessoas >= 5 and pessoas < 10:
    print("Médio")
elif pessoas > 11 and pessoas <= 15:
    print("Elevado")
else:
    print("Extremo")