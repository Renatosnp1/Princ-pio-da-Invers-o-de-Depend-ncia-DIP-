from controller.abstract import IExtratorDeDados


class ExtratordeDados(IExtratorDeDados):

    def extrair(self, fonte):
        
        if 'vinicius' in fonte.lower():

            dados_bruto = fonte.split(" ")[-1]

        else:

            dados_bruto = ''
        
        return dados_bruto