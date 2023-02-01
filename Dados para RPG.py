import random
dado = str(input("Escolha o dado que você vai lançar (1d20, 3d6 ou 2d10): "))
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d6 = [1, 2, 3, 4, 5, 6]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if dado == ('1d20'):
    print("Você rolou {}".format(random.choice(d20)))
    if random.choice(d20) == 20:
        print ("Você teve um acerto critico")
    if random.choice(d20) == 1:
        print ("Você teve um erro critico")

if dado == ("3d6"):
    print("Você rolou {}, {} e {}".format(random.choice(d6), random.choice(d6), random.choice(d6)))

if dado == ("2d10"):
    print("Você rolou {} e {}".format(random.choice(d10), random.choice(d10)))
