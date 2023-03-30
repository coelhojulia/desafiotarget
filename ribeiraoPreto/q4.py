
distancia = 100


velocidade_carro = 110


velocidade_caminhao = 80


tempo = distancia / (velocidade_carro + velocidade_caminhao)


distancia_carro = velocidade_carro * tempo


distancia_caminhao = velocidade_caminhao * tempo


if distancia_carro > distancia / 2:
    print("O carro estará mais próximo de Ribeirão Preto.")
else:
    print("O caminhão estará mais próximo de Ribeirão Preto.")
