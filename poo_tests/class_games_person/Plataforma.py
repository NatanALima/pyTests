class Plataforma:
    plataformList = ["Xbox", "Playstation", "Pc"];

    def __init__(self):
        self.plataforma = None
        self.showPlataformOptions();

    def showPlataformOptions(self):
        print("Plataformas Disponíveis para o Campeonato");
        print('===================================')
        for plataform in self.plataformList:
            print(f"{self.plataformList.index(plataform)}: {plataform}")
        print('===================================')

    def selectPlataform(self):
        while True:
            index = int(input("Informe o Número correspondente à sua Plataforma: "));
            if self.verifyValueInPlataform(index):
                break;

    def verifyValueInPlataform(self, valueIndex):
        if valueIndex > len(self.plataformList) - 1 or valueIndex < 0:
            print("Valor inválido! Insira o Valor Correto!")
        else:
            self.plataforma = self.plataformList[valueIndex];
            print(f'Plataforma Selecionada: {self.plataforma}')

        return 1 if self.plataforma is not None else 0

