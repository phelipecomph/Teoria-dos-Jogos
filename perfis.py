class Player:  
    def __init__(self, perfil):
        self.coins = 10
        self.opponentPlays = []
        self.perfil = perfil

    def startMatch(self):
        self.opponentPlays = []
    

    def play(self):
        if self.perfil == "cooperativo":
            return 1
        elif self.perfil == "trapaceiro":
            return 0
        elif self.perfil == "rancoroso":
            if 0 in self.opponentPlays:
                return 0
            else: 
                return 1
        elif self.perfil == "copiador":
            if len(self.opponentPlays) == 0:
                return 1
            else:
                return self.opponentPlays[-1]
    

    def feedback(self, coinIn):
        if coinIn > 0:
            self.opponentPlays.append(1)
        else:
            self.opponentPlays.append(0)
        
        self.coins += coinIn