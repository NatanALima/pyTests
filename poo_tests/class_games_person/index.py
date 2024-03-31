from Pessoa import Pessoa
from Jogador import Jogador
from Plataforma import Plataforma
from Campeonato import Campeonato

pessoa1 = Pessoa("Claudio", "Pereira", 20);
plataforma1 = Plataforma();
plataforma1.selectPlataform();

pessoa2 = Pessoa("Manuel", "Gomes", 21);
plataforma2 = Plataforma();
plataforma2.selectPlataform();

jogador1 = Jogador(pessoa1, "o brabo", plataforma1, 15, 3);
jogador2 = Jogador(pessoa2, "blue pen", plataforma2, 22, 0);

print(f'MOSTRANDO AS VITÓRIAS DOS JOGADORES {jogador1.vitorias}, {jogador2.vitorias}');
print(f'MOSTRANDO AS DERROTAS DOS JOGADORES {jogador1.derrotas}, {jogador2.derrotas}');

campeonato1 = Campeonato(jogador1, jogador2, "PC");
campeonato1.fightPlayers();





