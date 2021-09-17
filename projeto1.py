#Exemplo 5 - fatorial de um número
'''
Crie um programa que receber um numero e imprima o fatorial daquele numero
#Metodo 5Q's para montar um algoritimo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações;invetigue mais até compreender completamente o problema.)

1. Quais são os dados de entrada necessaria?
- numero
2. O que devo fazer com estes dados?
eu devo calcular o fatorial do numero que for passado para o meu programa e o exibir na tela.
3. Quais sao as restrições deste problema?
- o numero deve ser um valor positivo
- o numero deve ser um valor inteiro
4. Qual é o resultado esperado?
- O resultado esperado é que o fatorial do numero providenciado seja exibido.
5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?
input numero
if numero for > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
  fatorial = fatorial * numero
print (fatorial)
'''
numero = int(input('digite um numero '))
if numero > 0:
  fatorial = 1
  for item in range(1,numero +1):
    fatorial = fatorial * item
print(fatorial)
