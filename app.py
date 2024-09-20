from controller.pipeline import Pipeline
from controller.extrator import ExtratordeDados
from controller.formatador import FormatadorDeDados


extrator=ExtratordeDados() 
formatador=FormatadorDeDados()


p = Pipeline(extrator=extrator, formatador=formatador)

texto = 'Renato Vinicius Carneiro de Mattos'
print(p.executa(texto))