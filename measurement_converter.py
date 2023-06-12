#Conversor de unidades: este programa permite ao usuário converter unidades de medida diferentes.
# O programa solicita ao usuário uma entrada e a converte em outra unidade de medida usando uma fórmula matemática apropriada.

print ("!!! CONVERSOR DE UNIDADES !!!")
    
def converter_unidades (valor, unidade_de, unidade_para):
    if unidade_de == "cm" and unidade_para == "m":
        return valor/100
    elif unidade_de == "m" and unidade_para == "cm":
        return valor*100
    elif unidade_de == "km" and unidade_para == "m":
        return valor*1000
    elif unidade_de == "m" and unidade_para == "cm":
        return valor/1000
    elif unidade_de == "kg" and unidade_para == "g":
        return valor*1000
    elif unidade_de == "g" and unidade_para == "kg":
        return valor/1000
    else:
        return None

valor = float(input("Digite o valor a ser convertido: "))
unidade_de = input ("Digite a unidade de medida atual (cm, m, kg, g): ")
unidade_para = input ("Digite a unidade de medida desejada (cm, m, kg, g): ")
resultado = converter_unidades (valor, unidade_de, unidade_para)

if resultado is not None:
    print (f"{valor}{unidade_de} é equivalente a {resultado}{unidade_para}.")
else:
    print('As unidades de medida selecionadas não são compatíveis para conversão.')