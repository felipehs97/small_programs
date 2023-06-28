#Analisador de texto: este programa analisa o texto do usuário e informa estatísticas sobre o número de palavras, frases e parágrafos, bem como a contagem de palavras-chave ou frases.
import re

print ("##### ANALISADOR DE TEXTO 1.0")

user_text = input ("Digite seu texto :")
option = input ("DIGITE 1: PARA CONTAGEM NÚMERO DE CARACTERES\nDIGITE 2: PARA NÚMERO DE PALAVRAS\nDIGITE 3: PARA CONTAGEM DE PALAVRAS REPETIDAS\nDIGITO ESCOLHIDO: ")


if option == "1":
    counter = 0
    for char in user_text:
        if char != " ":
            counter += 1
    print("O número de caracteres do seu texto foi de: ", counter)

elif option == "2":
    user_text = len(user_text.split())
    print ("O numero de palavras do seu texto foi de: ", user_text)

elif option == "3":
    keyword = input("Digite a palavra chave que seja encontrar em seu texto: ")
    num_occourrences = user_text.count (keyword)
    print ("O número de palvras repetidas encontradas foi de: ", num_occourrences)

else:
    print ("Erro")
