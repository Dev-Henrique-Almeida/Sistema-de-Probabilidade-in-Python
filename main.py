import random
import time
import os
# os.system("pause")
# os.system('cls')


def visualizar():
    print(f'┌{"-" * 73}┐')
    print(f'|{" " * 20}R.P - SISTEMA DE PROBABILIDADES{" " * 22}|')
    print(f"|{'_' * 73}|")
    print(f'|{" " * 25}1 - VISUALIZAR COLUNAS {" " * 25}|')
    print(f'|{" " * 25}2 - VISUALIZAR LINHAS {" " * 26}|')
    print(f'|{" " * 25}3 - VISUALIZAR TODA A BASE DE DADOS {" " * 12}|')
    print(f'|{" " * 25}4 - SAIR {" " * 39}|')
    print(f'└{"-" * 73}┘')


def menu_arquivo_carregado():
    print(f'┌{"-" * 73}┐')
    print(f'|{" " * 20}R.P - SISTEMA DE PROBABILIDADES{" " * 22}|')
    print(f"|{'_' * 73}|")
    print(f'|{" " * 25}1 - SUBSTITUIR ARQUIVO {" " * 25}|')
    print(f'|{" " * 25}2 - CARREGAR COLUNAS {" " * 27}|')
    print(f'|{" " * 25}3 - SAIR {" " * 39}|')
    print(f'└{"-" * 73}┘')
    global option_menu_arquivo_carregado

    # carregar outro arquivo

    if option == 2:
        global colunas_usuario
        print(f"┌{'-' * 73}┐")
        colunas_usuario = input("| Quais colunas você desejar carregar? ").split()
        print(f"└{'-' * 73}┘")
        if colunas_usuario:
            print(f'┌{"-" * 73}┐')
            quantia = int(input("| Qual a quantidade de registros que deseja ver? "))  # funcao 2
            print(f"└{'-' * 73}┘")
            if quantia <= classe.linhas_tabela:  # 54
                classe.carregar_colunas(colunas_usuario, quantia)  # funcao 2
            elif quantia != classe.linhas_tabela:
                print(f'┌{"-" * 73}┐')
                print(f"|{' '*20} A quantidade de linhas vai de 1 á {classe.linhas_tabela}")
                pegar_linhas_try = int(input("| Informe novamente quantidade de registros que deseja ver: "))
                print(f'└{"-" * 73}┘')
                classe.carregar_colunas(colunas_usuario, pegar_linhas_try)
                os.system('cls')
            menu_colunas_carregadas()
        if not colunas_usuario:
            print(f"┌{'-' * 89}┐")
            print(f"| {' ' * 9} Coluna não encontrada! Por favor, informe novamente o nome da coluna {' ' * 9}|")
            print(f"└{'-' * 89}┘")
            menu_arquivo_carregado()


def menu_colunas_carregadas():
    print(f'┌{"-" * 73}┐')
    print(f'|{" " * 20}R.P - SISTEMA DE PROBABILIDADES{" " * 22}|')
    print(f"|{'_' * 73}|")
    print(f'|{" " * 22}1 - SUBSTITUIR ARQUIVO {" " * 28}|')
    print(f'|{" " * 22}2 - CALCULAR PROBABILIDADE APRIORI {" " * 16}|')
    print(f'|{" " * 22}3 - CALCULAR PROBABILIDADE APRIORI INTERVALO {" " * 6}|')
    print(f'|{" " * 22}4 - CALCULAR PROBABILIDADE CONDICIONAL {" " * 12}|')
    print(f'|{" " * 22}5 - CALCULAR PROBABILIDADE CONDICIONAL INTERVALO   |')
    print(f'|{" " * 22}6 - VISUALIZAR DADOS CARREGADOS                    |')
    print(f'|{" " * 22}7 - APAGAR DADOS {" " * 34}|')
    print(f'|{" " * 22}8 - SAIR {" " * 42}|')
    print(f'└{"-" * 73}┘')


def tela():
    print("┌-------------------------------------------------------------------------┐")
    print("|                      R.P - SISTEMA DE PROBABILIDADE                     |")
    print("└-------------------------------------------------------------------------┘")


def tela_final():
    print(''' 
    ┌-----------------------------------------------------┐
    |   Universidade Federal do Agreste de Pernambuco     |
    |       Bacharelado em Ciencia da Computação          |
    |-----------------------------------------------------|
    | Desenvolvido por:                                   |
    |                                                     |
    | Henrique de Almeida Silva                           |
    | Pablo Henrique Tavares da Silva                     |
    |                                                     |
    | Version 3.5.8     MEGAZORD             24/05/2022   |
    └-----------------------------------------------------┘
    ''')
    time.sleep(4)


class ExtratorDeProbabilidades:
    def __init__(self, base_dados):
        self.lista_colunas = None
        self.linhas_intervalo = None
        self.base_dados = base_dados

        self.lista_valor_aleatorio = []
        self.linhas_tabela = 0
        self.base_all = []  # este é o banco de dados
        global base_all
        self.primeira_linha = []

        tabela = open(self.base_dados, 'r', encoding='cp437')  # puxando o arquivo

        for linha_a_linha in tabela:
            if self.linhas_tabela == 0:
                self.primeira_linha = linha_a_linha.strip('"').strip("\n").strip(';').split(",")  # primeira_linha
            self.linhas_tabela += 1
        tabela.close()

    def carregar_colunas(self, lista_colunas, quantidade):
        lista_estrutura = []
        self.lista_colunas = lista_colunas
        for colunas_do_usuario in lista_colunas:
            if colunas_do_usuario in self.primeira_linha:
                lista_estrutura.append(self.primeira_linha.index(colunas_do_usuario))

            else:
                print(f'┌{"-" * 73}┐')
                print(f'| A coluna não foi encontrada {"" * 42} |')
                print(f"└{'-' * 73}┘")
                colunas_usuario.clear()
                continue

        self.linhas_intervalo = quantidade
        tabela = open(self.base_dados, 'r', encoding='cp437')
        lista_temp = []
        for i in range(self.linhas_tabela):
            lista_temp.append(i)
        self.lista_valor_aleatorio = random.sample(lista_temp, quantidade)  # valores aleatorios
        i = 0
        for linha in tabela:
            auxiliar = self.lista_valor_aleatorio.count(i)
            if auxiliar == 1 and i != 0:
                self.base_all.append([x for i, x in enumerate(linha.strip("").strip("\n").split(","))
                                      if i in lista_estrutura])
            i += 1

        tabela.close()

    def descarregar(self):
        self.base_all.clear()
        self.lista_colunas.clear()
        self.linhas_tabela = 0
        self.lista_valor_aleatorio = 0
        self.linhas_intervalo = 0

    def probabilidade_apriori(self, caracteristica, valor):

        i = 0
        contador_caracter, contador_valor = 0, 0

        for working_coluna in self.lista_colunas:
            if caracteristica == working_coluna:
                contador_caracter = i
            i += 1
# print(self.base_all) - para mostrar onde ta o erro da tabela, como ocorre na lista vehicles.csv
# print(f"LINHA: {working_linha[contador_caracter]}") - para mostrar onde ta o erro, ocorrido
# na lista vehicles.csv (OBS: COLOCAR NA ENTRE O FOR E O IF DA LINHA A BAIXO)
        for working_linha in self.base_all:
            if working_linha[contador_caracter] == valor:
                contador_valor += 1

        resultado_probabilidade = float((contador_valor / self.linhas_intervalo) * 100)
        print(f"┌{'-' * 100}┐")
        print(f"|{' ' * 10} A probabilidade apriori das caracteristicas {caracteristica}, em relação a {valor}")
        print(f"| {' ' * 37} é de {resultado_probabilidade:.2f}%")
        print(f"└{'-' * 100}┘")
        os.system('pause')
        os.system('cls')

    def probabilidade_apriori_intervalo(self, caracteristica, inicio, fim):
        i = 0
        contador_caracter, contador_valor = 0, 0
        for working_coluna in self.lista_colunas:
            if caracteristica == working_coluna:
                contador_caracter = i
            i += 1
        for working_linha in self.base_all:
            if working_linha[contador_caracter]:
                if (inicio < float(working_linha[contador_caracter])) and (float(working_linha[contador_caracter])
                                                                           < fim):
                    contador_valor += 1

        resultado_probabilidade_intervalo = float((contador_valor / self.linhas_intervalo) * 100)
        print(f"┌{'-' * 100}┐")
        print(f"|{' ' * 10} A probabilidade apriori das caracteristicas {caracteristica}, no intervalo de {inicio} e"
              f" {fim}")
        print(f"| {' ' * 37} é de {resultado_probabilidade_intervalo:.2f}%")
        print(f"└{'-' * 100}┘")
        os.system('pause')
        os.system('cls')

    def probabilidade_condicional(self, caracteristica_1, valor_1, caracteristica_2, valor_2):

        i = 0
        contador_caracter, contador_valor, contador_caracter_2, contador_compativel = 0, 0, 0, 0

        for working_coluna in self.lista_colunas:
            if {caracteristica_1, caracteristica_2}.issubset(self.lista_colunas):
                if caracteristica_1 == working_coluna.strip(' ').strip('"').strip("\n"):
                    contador_caracter = i
                if caracteristica_2 == working_coluna.strip(' ').strip('"').strip("\n"):
                    contador_caracter_2 = i
            else:
                print(f"┌{'-' * 89}┐")
                print(f"| {' ' * 37} Coluna não encontrada!   Por favor, informe novamente o nome da coluna |")
                print(f"└{'-' * 89}┘")
            i += 1
        for working_compatible in self.base_all:
            if working_compatible[contador_caracter_2] == valor_2:
                contador_compativel += 1

        for working_linha in self.base_all:
            if (working_linha[contador_caracter] == valor_1) and (working_linha[contador_caracter_2] == valor_2) \
                    and (working_linha[contador_caracter_2] == valor_2):
                contador_valor += 1

        resultado_probabilidade_condicional = float((contador_valor / contador_compativel) * 100)
        print(f"┌{'-' * 100}┐")
        print(f"|{' ' * 10} A probabilidade condicional das caracteristicas {caracteristica_1}, e"
              f" {caracteristica_2}, em relação "
              f"a "
              f"{valor_1} e {valor_2} ")
        print(f"| {' ' * 37} é de {resultado_probabilidade_condicional:.2f}%")
        print(f"└{'-' * 100}┘")
        os.system('pause')
        os.system('cls')

    def probabilidade_condicional_intervalo(self, caracter__1, inicio, fim, caracter__2, valor):
        i = 0
        contador_caracter, contador_caracter_2, contador_valor, contador_compativel = 0, 0, 0, 0
        for working_coluna in self.lista_colunas:
            if caracter__1 == working_coluna.strip(' ').strip('"').strip("\n"):
                contador_caracter = i
            if caracter__2 == working_coluna.strip(' ').strip('"').strip("\n"):
                contador_caracter_2 = i
            i += 1
        for working_compatible in self.base_all:
            if working_compatible[contador_caracter_2] == valor:
                contador_compativel += 1

        for working_linha in self.base_all:
            if working_linha[contador_caracter] and working_linha[contador_caracter_2]:
                if ((float(working_linha[contador_caracter]) > inicio) and (float(working_linha[contador_caracter]) <
                                                                            fim)) and \
                        (working_linha[contador_caracter_2] == valor):
                    contador_valor += 1
            if working_linha[contador_caracter] and working_linha[contador_caracter_2] == False:
                print(f"┌{'-' * 89}┐")
                print(f"| {' ' * 37} Coluna não encontrada!   Por favor, informe novamente o nome da coluna |")
                print(f"└{'-' * 89}┘")
                os.system('cls')
                continue  # VOLTAR PARA O MENU TABELA CARREGADA

        resultado_probabilidade_condicional_intervalo = float((contador_valor / contador_compativel) * 100)
        print(f"┌{'-' * 100}┐")
        print(f"| A probabilidade condicional das caracteristicas {caracter__1}, e {caracter__2}, no intervalo "
              f"{inicio} e {fim} ")
        print(f"| {' ' * 37} é de {resultado_probabilidade_condicional_intervalo:.2f}%")
        print(f"└{'-' * 100}┘")
        os.system('pause')
        os.system('cls')


def menu1():
    print(f'┌{"-" * 73}┐')
    print(f'|{" " * 20}R.P - SISTEMA DE PROBABILIDADES{" " * 22}|')
    print(f"|{'_' * 73}|")
    print(f'|{" " * 25}1 - ABRIR ARQUIVO {" " * 30}|')
    print(f'|{" " * 25}2 - SAIR {" " * 39}|')
    print(f'└{"-" * 73}┘')

    global option
    print(f'┌{"-" * 73}┐')
    option = (int(input("| Informe uma opção: ")))
    print(f'└{"-" * 73}┘')
    if option == 1:
        print(f"┌{'-' * 73}┐")
        nome_arquivo = input(f"| Qual o nome do arquivo de deseja abrir? ")  # funcao 1
        print(f"└{'-' * 73}┘")  # PRIMEIRO MENU
        global classe
        classe = ExtratorDeProbabilidades(nome_arquivo)  # funcao 1
        os.system('cls')
    if option == 2:
        tela_final()
        exit()


# INICIO DO PROGRAMA
T = 100
while True:
    menu_colunas_carregadas_disponivel = 0
    menu1()
    option = 0
    if option == 1:
        # menu_arquivo_carregado()      # TRANSIÇÃO PARA O SEGUNDO MENU
        option = 0
    while True:
        menu_arquivo_carregado()
        T += 1
        print(f'┌{"-" * 73}┐')
        option_menu_arquivo_carregado = (int(input("| Informe uma opção: ")))
        print(f'└{"-" * 73}┘')
        if option_menu_arquivo_carregado == 1:
            print(f"┌{'-' * 73}┐")
            nome_arquivo = input(f"| Qual o nome do arquivo de deseja abrir? ")  # funcao 1
            print(f"└{'-' * 73}┘")
            classe = ExtratorDeProbabilidades(nome_arquivo)
        if option_menu_arquivo_carregado == 2:
            print(f"┌{'-' * 73}┐")
            colunas_usuario = input("| Quais colunas você desejar carregar? ").split()
            print(f"└{'-' * 73}┘")
            if colunas_usuario:
                print(f'┌{"-" * 73}┐')
                quantia = int(input("| Qual a quantidade de registros que deseja ver? "))  # funcao 2
                print(f"└{'-' * 73}┘")
                if quantia <= classe.linhas_tabela:  # 54
                    classe.carregar_colunas(colunas_usuario, quantia)  # funcao 2
                    os.system('cls')
                elif quantia != classe.linhas_tabela:
                    print(f'┌{"-" * 73}┐')
                    print(f"|{' '*14} A quantidade de linhas vai de 1 á {classe.linhas_tabela}")
                    pegar_linhas_try = int(input(f"|{' '*6} Informe novamente quantidade de registros que deseja "
                                                 f"ver: "))
                    print(f'└{"-" * 73}┘')
                    classe.carregar_colunas(colunas_usuario, pegar_linhas_try)
                    os.system('cls')
                menu_colunas_carregadas_disponivel = 1
            if not colunas_usuario:
                print(f"┌{'-' * 89}┐")
                print(f"| {' ' * 9} Coluna não encontrada! Por favor, informe novamente o nome da coluna {' ' * 9}|")
                print(f"└{'-' * 89}┘")
                menu_arquivo_carregado()
                continue

        if option_menu_arquivo_carregado == 3:
            tela_final()
            exit()

        while T != 0:
            menu_colunas_carregadas()    # TRANSIÇÃO PARA O TERCEIRO MENU

            print(f'┌{"-" * 73}┐')
            option_menu_colunas_carregadas = (int(input("| Informe uma opção: ")))
            print(f'└{"-" * 73}┘')

            if option_menu_colunas_carregadas == 1:
                classe.descarregar()
                print(f'┌{"-" * 73}┐')
                nome_arquivo = input(f"| Qual o nome do arquivo de deseja abrir? ")  # funcao 1
                print(f"└{'-' * 73}┘")
                classe = ExtratorDeProbabilidades(nome_arquivo)
                T = 0

            if option_menu_colunas_carregadas == 2:  # probabilidade
                print(f'┌{"-" * 73}┐')
                caracter = input("| Qual a caracteristica que deseja calcular a probabilidade? ")  # funcao 3
                if {caracter}.issubset(classe.lista_colunas):
                    quantia_valor = input("| Qual o valor que deseja ver? ")  # funcao 3
                    print(f'└{"-" * 73}┘')
                    classe.probabilidade_apriori(caracter, quantia_valor)  # funcao 3
                else:
                    print(f"┌{'-' * 89}┐")
                    print(
                        f"| {' ' * 9} Coluna não encontrada! Por favor, informe novamente o nome da coluna {' ' * 9}|")
                    print(f"└{'-' * 89}┘")
                # exit()  # QUERO QUE AO INVES DE FECHAR, VOLTE OU PERGUNTE SE O USUARIO QUER OUTRO CALCULO

            if option_menu_colunas_carregadas == 3:  # probabilidade dentro de um intervalo
                print(f'┌{"-" * 100}┐')
                caracter = input("| Qual a caracteristica que deseja calcular a probabilidade dentro de um intervalo? ")
                if {caracter}.issubset(classe.lista_colunas):
                    inicial = float(input("| Qual o inicio do intervalo? "))  # funcao 4
                    final = float(input("| Qual o final do intervalo? "))  # funcao 4
                    print(f'└{"-" * 100}┘')
                    classe.probabilidade_apriori_intervalo(caracter, inicial, final)  # funcao 4
                else:
                    print(f"┌{'-' * 89}┐")
                    print(f"| {' ' * 9} Coluna não encontrada! Por favor, informe novamente o nome"
                          f" da coluna {' ' * 9}|")
                    print(f"└{'-' * 89}┘")
            if option_menu_colunas_carregadas == 4:  # probabilidade condicional
                print(f'┌{"-" * 100}┐')
                caracter_1 = input("| Qual a primeira caracteristica que deseja calcular a probabilidade condicional? ")
                valor1 = input("| Qual o primeiro valor que deseja calcular a probabilidade condicional? ")
                caracter_2 = input("| Qual a segunda caracteristica que deseja calcular a probabilidade condicional? ")
                valor2 = input("| Qual o segundo valor que deseja calcular a probabilidade condicional? ")
                if {caracter_1, caracter_2}.issubset(classe.lista_colunas):
                    print(f'└{"-" * 100}┘')
                    classe.probabilidade_condicional(caracter_1, valor1, caracter_2, valor2)
                else:
                    print(f"┌{'-' * 89}┐")
                    print(f"| {' ' * 9} Coluna não encontrada! Por favor, informe novamente o nome da "
                          f"coluna {' ' * 9}|")
                    print(f"└{'-' * 89}┘")

            if option_menu_colunas_carregadas == 5:  # probabilidade dentro de um intervalo
                print(f'┌{"-" * 110}┐')
                caracter = input("| Qual a primeira caracteristica que deseja calcular a probabilidade dentro"
                                 " de um intervalo? ")
                inicial = float(input("| Qual o inicio do intervalo? "))
                final = float(input("| Qual o final do intervalo? "))
                caracter_2 = input("| Qual a segunda caracteristica que deseja calcular a probabilidade dentro"
                                   " de um intervalo? ")
                quantia_valor = input("| Qual o valor que deseja ver? ")
                print(f'└{"-" * 110}┘')
                if {caracter, caracter_2}.issubset(classe.lista_colunas):
                    classe.probabilidade_condicional_intervalo(caracter, inicial, final, caracter_2, quantia_valor)
                else:
                    print(f"┌{'-' * 89}┐")
                    print(
                        f"| {' ' * 9} Coluna não encontrada! Por favor, informe novamente o nome da coluna {' ' * 9}|")
                    print(f"└{'-' * 89}┘")

            if option_menu_colunas_carregadas == 6:
                Z = 200
                while Z != 0:
                    option_menu_visualizar = 0
                    visualizar()
                    option_menu_visualizar = (int(input("| Informe uma opção: ")))

                    if option_menu_visualizar == 1:

                        os.system('cls')
                        print(f"Coluna: {classe.lista_colunas}")

                    if option_menu_visualizar == 2:

                        os.system('cls')
                        for linha_visual in classe.base_all:
                            print(f"Linha:  {linha_visual}")

                    if option_menu_visualizar == 3:

                        os.system('cls')
                        print(f"Coluna(s): {classe.primeira_linha}")
                        for linha_visual in classe.base_all:
                            print(f"Linha:  {linha_visual}")

                    if option_menu_visualizar == 4:
                        os.system('cls')
                        Z = 0

            if option_menu_colunas_carregadas == 7:
                classe.descarregar()
                print('''
                ┌------------------------------┐
                |  DADOS APAGADOS COM SUCESSO! |
                └------------------------------┘
                ''')

            if option_menu_colunas_carregadas == 8:
                tela_final()
                exit()
