#Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para
#obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a
#distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de
#combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade mé
#dia, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

tempo = float(input("Digite o tempo gasto na viagem: "))
velocidade = float(input("Informe a velocidade média durante a viagem: "))
distancia = tempo * velocidade
litros = distancia / 12

print(f"Velocidade: {velocidade} Km/h")
print(f"Tempo Gasto: {tempo} horas")
print(f"Distância Percorrida: {distancia} Km")
print(f"Quantidade de Combustível: {round(litros, 1)} litros")