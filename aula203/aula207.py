from dataclasses import asdict, astuple, dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
   
   
if __name__ == '__main__':
    p1 = Pessoa('André', 'Chagas')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])