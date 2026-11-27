
def registar_uma_consulta():
	print(r"""
	Deseja marcar consulta para que dia e para que profissional

	Insira para o dia da semana:      Insira o profissional:

	1 - Segunda-feira				  1 - Dra. Ana Silva - Medicina Geral
	2 - Terça-feira					  2 - Dr. Rui Costa - Dermatologia
	3 - Quarta-feira				  3 - Dra. Marta Reis - Pediatria
	4 - Quinta-feira
	5 - Sexta-feira

	""")
	dia = 0
	profissional = 0
	valido = False

	while not valido:
		try:
			dia = int(input("Dia (1-5): "))
			profissional = int(input("Profissional (1-3): "))
			if 1 <= dia <= 5 and 1<= profissional <= 3:
				valido = True
			else:
				print("O dia tem de estar entre 1 e 5 e o professional entre 1 e 3.")
		except ValueError:
			print("Entrada inválida. Escreva números.")
	
	dia -= 1
	profissional -= 1

	if consultas[profissional][dia] >= limite_de_consultas_diarias[profissional]:
		print("Limite de consultas atingido para este profissional\nPor favor tente marcar noutro dia ou com outro profissional")
	else: 
		consultas[profissional][dia] += 1
		print("A sua consulta foi resgistada")

def cancelar_uma_consulta():
	print(r"""
	Deseja cancelar uma consulta para que dia e para que profissional
	
	Insira para o dia da semana:      Insira o profissional:
	
	1 - Segunda-feira				  1 - Dra. Ana Silva - Medicina Geral
	2 - Terça-feira					  2 - Dr. Rui Costa - Dermatologia
	3 - Quarta-feira				  3 - Dra. Marta Reis - Pediatria
	4 - Quinta-feira
	5 - Sexta-feira
	
	""")
	dia = 0
	profissional = 0
	valido = False
	
	while not valido:
		try:
			dia = int(input("Dia (1-5): "))
			profissional = int(input("Profissional (1-3): "))
			if 1 <= dia <= 5 and 1<= profissional <= 3:
				valido = True
			else:
				print("O dia tem de estar entre 1 e 5 e o professional entre 1 e 3.")
		except ValueError:
				print("Entrada inválida. Escreva números.")
		
	dia -= 1
	profissional -= 1
	
	if consultas[profissional][dia] <= 0:
			print("Este profissional não tem consultas este dia que possa cancelar")
	else: 
		consultas[profissional][dia] -= 1
		print("A sua consulta foi cancelada")
