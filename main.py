import perfis as p

#Recebe uma lista da ação dos 2 jogadores e retorna a saida da maquina
def game(inputs):
    if (inputs[0] == 0 and inputs[1] == 0):
        return ([0,0])
    elif (inputs[0] == 1 and inputs[1] == 1):
        return ([2,2])
    elif (inputs[0] == 0 and inputs[1] == 1):
        return ([3,-1])
    elif (inputs[0] == 1 and inputs[1] == 0):
        return ([-1,3])

# Inicio do programa
inputs = [0,0]
Jogador_1 = p.Player("copiador")
Jogador_2 = p.Player("rancoroso")

# Loop principal
for i in range(0,10):
    inputs[0] = int(input("Sua jogada? "))
    # inputs[0] = Jogador_1.play()
    inputs[1] = Jogador_2.play()
    outputs = game(inputs)
    print(outputs)
    Jogador_1.feedback(outputs[0])
    Jogador_2.feedback(outputs[1])