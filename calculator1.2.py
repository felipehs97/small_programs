#Calculadora: este programa realiza operações básicas de matemática, como adição, subtração, multiplicação e divisão, com base em entradas fornecidas pelo usuário.

print("########### CALCULADORA ###########")

print("OPERAÇÕES OFERECIDAS")
print("[1] - [ADIÇÃO] \n[2] - [SUBTRAÇÃO] \n[3] - [MULTIPLICAÇÃO] \n[4] - [DIVISÃO]")
choice = int(input("DIGITE A OPERAÇÃO DESEJADA: "))

if choice >= 1 and choice <= 4:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    result = 0 
  
    if choice == 1:
        result = n1 + n2
        print("Resultado é:", result)
    elif choice == 2:
        result = n1 - n2
        print("Resultado é:", result)
    elif choice == 3:
        result = n1 * n2
        print("Resultado é:", result)
    elif choice == 4:
        result = n1 / n2
        print("Resultado é:", result)
else:
    print("OPÇÃO INEXISTENTE")