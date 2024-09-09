from cliente_pacote import Cliente
from pacote_viagem import PacoteViagem

class Venda:
    def __init__(self, codigo, cliente: Cliente, descricao, pacote: PacoteViagem, quantidade):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__descricao = descricao
        self.__pacote = pacote
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def pacote(self) -> PacoteViagem:
        return self.__pacote

    @pacote.setter
    def pacote(self, pacote: PacoteViagem):
            self.__pacote = pacote

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__durante = duracao
