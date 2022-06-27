class Pessoa:
    def __init__(self, nome, data, genero):
        self.nome = nome
        self.data = data
        self.genero = genero
    def __str__(self):
        return f"Nome: { self.nome }\
                \nData: { self.data }\
                \nGênero: { self.genero }"
                
class Professor(Pessoa):
    def alterarProfessor(self):
        self.nome = input("Digite o nome do Professor: ")
        self.data = input("Digite a data de nascimento do Professor: ")
        self.genero = input("Digite o gênero do Professor: ")
        return self

class Sala(Pessoa):
    def alterarSala(self):
        if (self == " "):
            print("Não existe Sala que possa ser editado!")
        else:
            self.numero = input("Digite o numero da Sala: ")
            self.data = input("Digite a data de construção da Sala: ")
            self.predio = input("Digite o predio da Sala: ")
        return self

class Aluno:
    def __init__(self, nome, dre, idade):
        self.nome = nome
        self.dre = dre
        self.idade = idade

    def __str__(self):
        return f"Nome: { self.nome }\
                \ndre: { self.dre }\
                \nidade: { self.idade }"
    
    def alterarAluno(self):
        self.nome = input("Digite o nome do Aluno: ")
        self.dre = input("Digite a dre do Aluno: ")
        self.idade = input("Digite o idade do aluno: ")
        return self

class Disciplina:
    def __init__(self, nomedisciplina, numero, Professor):
        self.nomedisciplina = nomedisciplina
        self.numero = numero
        self.lista_alunos = []
        self.Professor = Professor
        self.Sala = " "
    
    def __str__(self):
        return f"nomedisciplina: { self.nomedisciplina }\
                \nnumero: { self.numero }\
                \nProfessor: { self.Professor }\
                \nSala: { self.Sala }"

    def adicionarProfessor(self, Professor):
        print("O Professor foi removido da disciplina e movido para realocação!")
        ProfessorRemovido = self.Professor
        self.Professor = Professor
        print("O novo Professor foi adicionado a disciplina e saiu da realocação!")
        return ProfessorRemovido

    def adicionarSala(self, Sala):
        if (self.Professor != " "):
            pass
        else:
            print("O Professor foi removido da disciplina e movido para realocação!")
            SalaRemovido = self.Professor
        self.Sala = Sala
        print("A nova Sala foi adicionada a disciplina e saiu da realocação!")
        return SalaRemovido
    
    def adicionarAluno(self, idAluno, Aluno):
        self.lista_alunos.insert(idAluno, Aluno)

    def alterarDados(self):
        self.nomedisciplina = input("Digite a nome da disciplina: ")
        self.numero = input("Digite o numero de identificação da Disciplina: ")
