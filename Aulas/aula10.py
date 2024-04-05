"""" 
constante = variaveis que nao vao mudar
"""

velocidade = 61 # velocidade do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade do radar 1
LOCAL_1 = 100 # local onde o radar está na estrada
RADAR_RANGE = 1 # range do radar

vel_carro_pass_radar_1 = velocidade > RADAR_1
multar_car_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if multar_car_radar_1 and vel_carro_pass_radar_1:
    print('Carro multado em radar 1')