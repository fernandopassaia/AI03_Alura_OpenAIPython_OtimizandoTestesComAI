from gerador_casos_de_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *


def main():
    # Passo 1 - vai gerar nosso caso de uso
    casos_uso = gerar_caso_uso()
    print("\nCaso de Uso:\n", casos_uso)

    # Passo 2 - vai gerar nosso cenário de teste
    cenario_teste = gerar_cenario_teste(caso_uso=casos_uso)
    print("\nCenario Teste\n", cenario_teste)

    # Passo 3 - vai gerar o nosso script em python
    script_teste = gerar_script_teste(caso_uso=casos_uso, cenario_teste=cenario_teste)
    print("\nScript Teste\n", script_teste)
    salva("script_temp_ia.py", script_teste)


if __name__ == "__main__":
    main()
