# Class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos
# Os objetos gerados pela classe poder usar dados internos para realizar várias ações
# Por convenção, usamos PascalCase para nomes de classes

class Pessoa:
     ...

p1 = Pessoa()
p1.nome = 'André'
p1.sobrenome = 'Chagas'

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)