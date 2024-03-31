'''
    A utilização do Getter e Setter no Python não é uma melhor opção, justamente em decorrência da repetitividade. Como um substituto para esses métodos temos o Properties que seguem a mesma ideia do Getter e o Setter porém estes métodos são feitos por "debaixo dos panos"

    De acordo com a própria documentação do Python é sugerível que se utilize dos atributos públicos e, caso esses atributos exijam de um comportamento funcional, aí sim utilizaremos os properties

    O que diz a documentação do Python sobre Atributos Privados?

    9.6. Variáveis privadas
    Variáveis de instância “privadas”, que não podem ser acessadas, exceto em métodos do próprio objeto, não existem em Python. No entanto, existe uma convenção que é seguida pela maioria dos programas em Python: um nome prefixado com um sublinhado (por exemplo: _spam ) deve ser tratado como uma parte não-pública da API (seja uma função, um método ou um atributo de dados). Tais nomes devem ser considerados um detalhe de implementação e sujeito a alteração sem aviso prévio.
'''
import datetime

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome;
        self.sobrenome = sobrenome;
        self.idade = idade;

    def showFullName(self):
        return f"{self.nome} {self.sobrenome}";

    def showBornDate(self):
        today = datetime.date.today();
        return int(today.year - self.idade);



