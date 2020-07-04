#Recebe uma lista da ação dos 2 jogadores e retorna a saida da maquina
def game(inputs):
    if (inputs[0] == 0 and inputs[1] == 0):
        return ([0,0])
    elif (inputs[0] == 1 and inputs[1] == 1):
        return ([2,2])
    elif (inputs[0] == 0 and inputs[1] == 1):
        return ([3,0])
    elif (inputs[0] == 1 and inputs[1] == 0):
        return ([0,3])

# Inicio do programa
inputs = [0,0]


# Loop principal
while(1):
    inputs[0] = int(input("Jogador 1: "))
    inputs[1] = int(input("Jogador 2: "))
    print(game(inputs))