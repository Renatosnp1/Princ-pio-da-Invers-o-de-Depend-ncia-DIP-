from controller.extrator import ExtratordeDados
from controller.formatador import FormatadorDeDados



class Pipeline:

    def __init__(self, extrator: ExtratordeDados, formatador: FormatadorDeDados) -> None:
        
        self.__extrator = extrator
        self.__formatador = formatador


    def executa(self, fonte) -> str:

        fonte = self.__extrator.extrair(fonte)
        fonte = self.__formatador.formatar(fonte)

        return fonte