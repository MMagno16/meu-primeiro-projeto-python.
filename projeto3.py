velocidade = int(input('digite sua velocidade'))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print('não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print('levou multa leve')
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
   print('levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print('levou multa gravissima')