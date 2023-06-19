import random

print("Chute um valor de 1 a 10 para tentar acertar o valor aleatório")
random_value = random.randint(1, 10)
wrong_guess = False
while True:
    user_guess = int(input("Digite seu chute: "))
    if random_value > user_guess:
        print("O valor chutado foi menor que o valor aleatório")
    elif random_value < user_guess:
        print("O valor chutado foi maior que o valor aleatório")
    elif random_value == user_guess:
        print("Você Acertou")
        wrong_guess = False
        break
    else:
        None