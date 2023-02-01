import random
voce = str(input("Escolha: pedra, papel ou tesoura: "))
pc = ["pedra", "papel", "tesoura"]
pc1 = random.choice(pc)
print("O computador escolheu {}".format(pc1))

if pc1 == "pedra" and voce == "papel":
    print("Você GANHOU!")
elif pc1 == "pedra" and voce == "tesoura":
    print("O computador GANHOU!")
elif pc1 == "pedra" and voce == "pedra":
    print("EMPATE!")

if pc1 == "papel" and voce == "tesoura":
    print("Você GANHOU!")
elif pc1 == "papel" and voce == "pedra":
    print("O computador GANHOU!")
elif pc1 == "papel" and voce == "papel":
    print("EMPATE!")

if pc1 == "tesoura" and voce == "pedra":
    print("Você GANHOU!")
elif pc1 == "tesoura" and voce == "papel":
    print("O computador GANHOU!")
elif pc1 == "tesoura" and voce == "tesoura":
    print("EMPATE!")
