while True:
    speed = int(input("Qual é sua velocidade?: "))
    
    if speed <= 80:
        print ("Não Houve Multa !!!")
    elif speed >= 81 and speed <= 90:
        print ("Multa Leve !!!")
    elif speed >=91 and speed <= 100:
        print ("Levou Multa Grave !!!")
    elif speed > 101:
        print ("Levou Multa Gravíssima !!!")
   
    sair = input("Deseja sair do programa? (s/n): \n")
    if sair == "s":
        break 

