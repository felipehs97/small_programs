import random
import string

print ("##### GERADOR DE SENHA #####")

size = input("Digite quantos digitos deverá ter a senha: ")
if not size.isdigit():
    print("Digite somente números para o tamanho da senha.")
    exit()

size = int(size)
uppercase = input("Gostaria que fosse adicionado letras maiúsculas? (sim/nao): ")
lowercase = input("Gostaria que fosse adicionado letras minúsculas? (sim/nao): ")

if uppercase == "sim" and lowercase == "sim":
    str_aleatoria = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=size))
    print(str_aleatoria)
elif uppercase == "sim" and lowercase == "nao":
    str_aleatoria = ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))
    print(str_aleatoria)
elif uppercase == "nao" and lowercase == "sim":
    str_aleatoria = ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
    print(str_aleatoria)
elif lowercase == "nao" and uppercase == "nao":
    str_aleatoria = ''.join(random.choices(string.digits, k=size))
    print(str_aleatoria)
else:
    print("Erro, digite somente 'sim' ou 'nao'.")