from time import sleep
def lin():
    print("-=-=" * 8)


vel = float(input("Qual é a velocidade do carro? "))
print("Um momento...")
sleep(3)
if vel > 80:
    multa = (vel - 80) * 7
    print(f"MULTADO!! Você excedeu o limite permitido  que é de 80km/h \nVocê deverá pagar uma multa de R${multa},00")
    print("Tenha um bom dia!")
else:
    print("Você está no limite da via! Continue digirindo em segurança!")
