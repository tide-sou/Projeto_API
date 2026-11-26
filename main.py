# Menu Principal:
#• Apresentar um menu com opções para consultar agendas, registar uma consulta, cancelar uma consulta, apresentar 
#estatísticas e terminar o programa.
#• O menu deverá repetir-se até o utilizador escolher a opção de terminar.
#• Informar o utilizador quando selecionar uma opção inválida.

import time

menu = 0
limite_de_consultas_diarias = [0,0,0] # Cada um destes valores é o limite diario respetivo de cada profissional
profissionais = ['Dra. Ana Silva', 'Dr. Rui Costa', 'Dra. Marta Reis']
especialidades = []  
dias = []
consultas = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]  # Nesta matriz as linhas são uma para cada um dos 3 profissionais e em cada linha tas as suas consultas 
]					 # Cada coluna é um dia, 1º coluna é segunda, 2º coluna é terça e por ai adiante

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
	5. Definir nr máx de consultas/dia/profissional
	6. Fechar o programa
	""")

	try:
		menu = int(input("O que deseja fazer: "))
	except ValueError:
		print("Entrada inválida. Por favor, insira um número de 1 a 5.")
		time.sleep(1.5)
		continue

	if menu == 1:
		pass  # fazer função Função do Jony
	elif menu == 2:
		pass  # fazer função Função do Brown    
	elif menu == 3:
		pass  # fazer função Função do Brown
	elif menu == 4:
		pass  # fazer função Função do Ramos
	elif menu == 5:
		pass  # fazer função Função do Jony
	elif menu == 6:
		print("Programa fechado.")      # Se em cima definir se que os profissionais e especialidades vao ser introduzidas
	else:                               # Então alguem irá ter essa função para fzr
		print("Opção inválida.")
		time.sleep(1.5)
			