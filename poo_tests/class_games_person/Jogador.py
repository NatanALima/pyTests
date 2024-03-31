class Jogador:
    def __init__(self, jogador, nickName: str, plataforma, vitorias: int, derrotas: int):
        self.jogador = jogador;
        self.nickName = nickName;
        self.plataforma = plataforma;
        self.vitorias = vitorias;
        self.derrotas = derrotas;

    @property
    def nickName(self):
        return self._nickName.upper();

    @nickName.setter
    def nickName(self, value):
        self._nickName = value

    def setVitorias(self):
        self.vitorias += 1;

    def setDerrotas(self):
        self.derrotas += 1;

