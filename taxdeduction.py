# Pega o seu salário e faz o enquadramento de acordo com a aliquota de imposto, resulta o valor de imposto a ser pago e qual será o salário liquido
gross_salary = float(input("Digite o seu Salário: "))

if gross_salary <= 1903.98:
    print ("Isento de imposto ")
elif gross_salary >= 1903.99 and gross_salary <= 2826.65:
    tax_value = gross_salary*0.075
    deducted_salary = gross_salary - tax_value
    print ("Aliquota de 7,5%, valor do imposto a ser pago R$: ", tax_value)
    print ("O salário liquido será de R$: ", deducted_salary)
elif gross_salary >= 2826.66 and gross_salary <= 3751.05:
    tax_value = gross_salary*0.15
    deducted_salary = gross_salary - tax_value
    print ("Aliquota de 15%, valor do imposto a ser pago R$: ", tax_value)
    print ("O salário liquido será de R$: ", deducted_salary)
elif gross_salary >= 3751.06 and gross_salary <= 4664.68:
    tax_value = gross_salary*0.225
    deducted_salary = gross_salary - tax_value
    print ("Aliquota de 22,5%, valor do imposto a ser pago R$: ", tax_value)
    print ("O salário liquido será de R$: ", deducted_salary)
elif gross_salary > 4664.68:
    tax_value = gross_salary*0.275
    deducted_salary = gross_salary - tax_value
    print ("Aliquota de 27,5%, valor do imposto a ser pago R$", tax_value)
    print ("O salário liquido será de R$: ", deducted_salary)