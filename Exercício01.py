pessoas = int(input("Índice de contágio: "))
if pessoas < 5:    
    print("Baixo")
elif pessoas >= 5 and < 10:
    print("Médio")
elif pessoas > 11 and <= 15:
    print("Elevado")
else pessoas > 15:
    print("Extremo")