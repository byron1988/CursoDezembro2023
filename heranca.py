
class Funcionario:

	def __init__(self, nome, salario, cpf):
		self.nome = nome
		self.salario = salario
		self.cpf = cpf

	def get_bonificacao(self):
		return self.salario * 0.20

class Gerente(Funcionario):	
	
	def __init__(self, nome, salario, cpf, senha):
		super().__init__(nome, salario, cpf)
		self.senha = senha

	def get_bonificacao(self):
		return super().get_bonificacao() + 1000.00		

g = Gerente('Thomas', 3000.00, '32222222', 3333)
print(g.get_bonificacao())
print(g.senha)