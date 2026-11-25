# Menu Principal:
#• Apresentar um menu com opções para consultar agendas, registar uma consulta, cancelar uma consulta, apresentar 
#estatísticas e terminar o programa.
#• O menu deverá repetir-se até o utilizador escolher a opção de terminar.
#• Informar o utilizador quando selecionar uma opção inválida.

import time

menu = 0
profissionais = []
especialidades = []
dias = []
consultas = []

while menu != 5:
    print(r"""
    /===========================\
    |Bem vindo/a à plataforma de|
    |    Gestão de Consultas    |
    \===========================/

    Escolha uma opção:

    1. Consultar agendas
    2. Registar uma consulta
    3. Cancelar uma consulta
    4. Apresentar estatística
    5. Fechar o programa
    """)

    try:
        menu = int(input("O que deseja fazer: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número de 1 a 5.")
        time.sleep(1.5)
        continue

    if menu == 1:
        pass  # fazer função
    elif menu == 2:
        pass  # fazer função
    elif menu == 3:
        pass  # fazer função
    elif menu == 4:
        pass  # fazer função
    elif menu == 5:
        print("Programa fechado.")
    else:
        print("Opção inválida.")
        time.sleep(1.5)