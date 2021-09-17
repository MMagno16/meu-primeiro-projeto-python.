#Variáveis.

#Números.
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 #float
#Valores boleanos.
esta_aberto = True
#Strings.
nome_do_curso =  'Logica de Programação'

#Como variaveis seriam usadas em um programa real?

#Problema1 - valor por hora
#Escreva um programa que retorna o valor hora de um funcionario com base no seu salário mensal e horas trabalhadas por mês.
'''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal/ horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input('Qual é o seu salario mensal?')
horas_trabalhadas_por_mes = input('quantas horas trabalha por mes?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)
