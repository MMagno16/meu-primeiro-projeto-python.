# Projeto - Chute o Numero
'''
Escreva um programa que, ao iniciar gera um valor aleatorio de 1 ao 10 e permite que o usuario chute um numero ate que o valor aleatorio gerado no inicio do programa seja chutado corretamente.
O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no inicio do programa.


#Metodo 5Q's para montar um algoritimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações;invetigue mais até compreender completamente o problema.)

1. Quais são os dados de entrada necessaria?
2. O que devo fazer com estes dados?
3. Quais sao as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?
'''
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('chute um valor de 1 a 10'))
  if chute > valor_aleatorio:
    print('chute foi maior que o valor gerado')
  elif chute < valor_aleatorio:
    print('chute foi menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('voce acertou!')
    

