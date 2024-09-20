from abc import ABC, abstractmethod


class IExtratorDeDados(ABC):

    @abstractmethod
    def extrair(self, fonte):
        pass




class IFormatadorDeDados(ABC):

    @abstractmethod
    def formatar(self, dados_bruto):
        pass



