'''

Constante = "Variáveis" que o valor não vai mudar
Muitas condições no if (ruim)

     <-Contagem de complexidade(ruim)

'''

velocidade_carro = 60 # Velocidade atual do carro
local_carro = 108 # Local em que o carro está na rodovia. Ex: Km 100

RADAR_1 = 60 # A velocidade máxima do radar 1.
LOCAL_RADAR = 110   # Local do radar 1 em que se encontra na rodovia.
RADAR_RANGE = 2 # O raio de alcançe do radar. Ex: 2m

velocidade_maxima_multa = velocidade_carro > RADAR_1
radar_alcance_multa = (local_carro == (LOCAL_RADAR - RADAR_RANGE) or local_carro == (LOCAL_RADAR + RADAR_RANGE))

if  velocidade_maxima_multa and radar_alcance_multa:
    print('Atenção! Você foi multado por excesso de velocidade.')
else:
    print('Dirija com atenção.')