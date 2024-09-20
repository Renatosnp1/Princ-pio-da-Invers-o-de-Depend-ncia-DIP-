from controller.abstract import IFormatadorDeDados


class FormatadorDeDados(IFormatadorDeDados):

    def formatar(self, dados_bruto):

        dados_formatado = dados_bruto.upper()

        return "********* Bem vindo!!! " + dados_formatado + " *********"