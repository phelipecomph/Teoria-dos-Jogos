import perfis as p

#Recebe uma lista da ação dos 2 jogadores e retorna a saida da maquina
def match(inputs):
    if (inputs[0] == 0 and inputs[1] == 0):
        return ([0,0])
    elif (inputs[0] == 1 and inputs[1] == 1):
        return ([1,1])
    elif (inputs[0] == 0 and inputs[1] == 1):
        return ([2,-1])
    elif (inputs[0] == 1 and inputs[1] == 0):
        return ([-1,2])

def confronto(Jogador_1, Jogador_2, matches):
    Jogador_1.startMatch()
    Jogador_2.startMatch()
    for i in range(0,matches):
        inputs = [0,0]
        if Jogador_1.perfil == "humano":
            inputs[0] = int(input("Sua jogada? "))
        else:
            inputs[0] = Jogador_1.play()

        inputs[1] = Jogador_2.play()
        outputs = match(inputs)
        if Jogador_1.perfil == "humano":
            print(outputs)
        Jogador_1.feedback(outputs[0])
        Jogador_2.feedback(outputs[1])

def game():
    if int(input("Autoplay? ")) == 0:
        Jogador_1 = p.Player("humano")
        Jogador_2 = p.Player(input("Qual o perfil do bot? "))
    else:
        Jogador_1 = p.Player(input("Qual o perfil do Jogador 1? "))
        Jogador_2 = p.Player(input("Qual o perfil do Jogador 2? "))
    
    while(1):
        print("O Jogador 1 é " + Jogador_1.perfil)
        print("O Jogador 2 é " + Jogador_2.perfil)

        confronto(Jogador_1, Jogador_2, 10)

        print("Moedas do Jogador 1: " + str(Jogador_1.coins))
        print("Moedas do Jogador 2: " + str(Jogador_2.coins))
        
        if Jogador_1.perfil == "humano":
            if int(input("Quer mudar o perfil do seu oponente? ")) == 1:
                Jogador_2 = p.Player(input("Qual o perfil do Jogador 2? ")) 
            
        else:
            if int(input("Quer mudar o perfil de algum jogador? ")) == 1:
                Jogador_1 = p.Player(input("Qual o perfil do Jogador 1? "))
                Jogador_2 = p.Player(input("Qual o perfil do Jogador 2? "))

# Inicio do programa
game()
