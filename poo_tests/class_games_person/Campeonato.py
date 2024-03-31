import random


class Campeonato:
    def __init__(self, jogador1, jogador2, plataforma):
        self.jogador1 = jogador1;
        self.jogador2 = jogador2;
        self.plataforma = plataforma;
        self.showPlayersInfo();

    def showPlayersInfo(self):
        print('INFORMAÇÕES DOS JOGADORES');
        print('============================');
        print(f'JOGADOR 1: {self.jogador1.jogador.nome} {self.jogador1.nickName} {self.jogador1.jogador.sobrenome}');
        print(f'Idade: {self.jogador1.jogador.showBornDate()}');
        print('----------------------------');
        print(f'JOGADOR 2: {self.jogador2.jogador.nome} {self.jogador2.nickName} {self.jogador2.jogador.sobrenome}');
        print(f'Idade: {self.jogador2.jogador.showBornDate()}');
        print('============================');

    def fightPlayers(self):
        players = [self.jogador1, self.jogador2];
        winner = random.choice(players);
        players.remove(winner);
        loser = players[0];
        winner.setVitorias();
        loser.setDerrotas();
        print(f'Inacreditável! O jogador {winner.nickName} GANHA a partida. Agora o seu número de vitórias é de {winner.vitorias}');
        print(f'Enquanto isso, O jogador {loser.nickName} Despede-se da partida! Agora o seu número de derrotas é de {loser.derrotas}');