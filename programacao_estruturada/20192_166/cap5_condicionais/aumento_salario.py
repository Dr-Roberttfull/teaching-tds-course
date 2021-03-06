# As Organizações Tabajara resolveram dar um aumento de salário
# aos seus colaboradores e lhe contrataram para desenvolver o
# programa que calculará os reajustes. Escreva um algoritmo que
# leia o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
# o salários até R$ 280, 00 (incluindo): aumento de 20%
# o salários entre R$ 280, 00 e R$ 700, 00: aumento de 15%
# o salários entre R$ 700, 00 e R$ 1500, 00: aumento de 10%
# o salários de R$ 1500, 00 em diante: aumento de 5 %
#
# Após o aumento ser realizado, informe na tela:
# · o salário antes do reajuste
# · o percentual de aumento aplicado
# · o valor do aumento
# · o novo salário, após o aumento.


def programa():
    salario = float(input('Salário: '))

    reajuste = calcula_aumento(salario)

    novo_salario = salario + reajuste

    print('Novo Salário = R$ %.2f' % novo_salario)


def calcula_aumento(salario):
    if salario <= 280:
        return salario * (20/100)
    elif salario <= 700:
        return salario * (15/100)
    elif salario <= 1500:
        return salario * (10/100)
    else:
        return salario * (5/100)


programa()
