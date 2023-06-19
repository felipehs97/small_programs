import random

print ("Chute um valor de 1 a 10 para tentar acertar o valor aleatório")
valor_aleatorio = random.randint (1,10)
Errou = False
while True:
    chute_usuario = int (input("Digite o seu chute: "))
    if valor_aleatorio > chute_usuario:
        print ("O valor chutado foi menor que o valor aleatório")
    elif valor_aleatorio < chute_usuario:
        print ("O valor chutado foi maior que o valor aleatório")
    elif valor_aleatorio == chute_usuario:
        print ("Você Acertou")
        Errou = False
        break
    else:
        None
    

