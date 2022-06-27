from classes import *

dicionarioDisciplina = {} #Dicionário com disciplina
dicionarioAlunos = {} #Alunos não utilizados
dicionarioProfessores = {} #Professores não utilizados
dicionarioSalas = {} #Salas não utilizados
#Funções de criar
def criarDisciplina():
    nomedisciplina = input("Digite a nome da disciplina: ")
    numero = input("Digite o numero do disciplina: ")
    #Já que todo disciplina precisa de Professor
    nome = input("Digite o nome do Professor: ")
    data = input("Digite a data de nascimento do Professor: ")
    genero = input("Digite o gênero do Professor: ")
    comando = " "
    idDisciplina = 0
    while (comando != "ID disponível!"):
        idDisciplina += 1
        comando = dicionarioDisciplina.get(idDisciplina,"ID disponível!")
    dicionarioDisciplina[idDisciplina] = Disciplina(nomedisciplina, numero, Professor(nome, data, genero))
    print("ID do disciplina: "+str(idDisciplina))
def criarAlunos():
    nome = input("Digite o nome do Alunos: ")
    dre = input("Digite a dre do Alunos: ")
    idade = input("Digite o idade do Alunos: ")
    comando = " "
    idAlunos = 0
    while (comando != "ID disponível!"):
        idAlunos += 1
        comando = dicionarioAlunos.get(idAlunos, "ID disponível!")
    dicionarioAlunos[idAlunos] = Aluno(nome, dre, idade)
    print("ID do Alunos: "+str(idAlunos))
def criarProfessor():
    nome = input("Digite o nome do Professor: ")
    data = input("Digite a data de nascimento do Professor: ")
    genero = input("Digite o gênero do Professor: ")
    comando = " "
    idProfessor = 0
    while (comando != "ID disponível!"):
        idProfessor += 1
        comando = dicionarioProfessores.get(idProfessor, "ID disponível!")
    dicionarioProfessores[idProfessor] = Professor(nome, data, genero)
    print("ID do Professor: "+str(idProfessor))
def criarSala():
    numero = input("Digite o numero da Sala: ")
    data = input("Digite a data de costrução da Sala: ")
    predio = input("Digite o predio da Sala: ")
    comando = " "
    idSala = 0
    while (comando != "ID disponível!"):
        idSala += 1
        comando = dicionarioSalas.get(idSala, "ID disponível!")
    dicionarioSalas[idSala] = Sala(numero, data, predio)
    print("ID do Sala: "+str(idSala))

#Funções de relacionar
def relacionarProfessor():
    idProfessor = input("Digite o ID do Professor: ")
    idDisciplina = input("Digite o ID do disciplina: ")
    Professor = dicionarioProfessores[idProfessor]
    Disciplina = dicionarioDisciplina[idDisciplina]
    dicionarioProfessores[idProfessor] = Disciplina.adicionarProfessor(Professor)
    dicionarioDisciplina[idDisciplina] = Disciplina
def relacionarSala():
    idSala = input("Digite o ID do Sala: ")
    idDisciplina = input("Digite o ID do disciplina: ")
    Sala = dicionarioSalas[idSala]
    Disciplina = dicionarioDisciplina[idDisciplina]
    dicionarioSalas[idSala] = Disciplina.adicionarSala(Sala)
    dicionarioDisciplina[idDisciplina] = Disciplina
def relacionarAlunos():
    idAlunos = input("Digite o ID do Alunos: ")
    idDisciplina = input("Digite o ID do disciplina: ")
    Alunos = dicionarioAlunos[idAlunos]
    Disciplina = dicionarioDisciplina[idDisciplina]
    Disciplina.adicionarAlunos(idAlunos, Alunos)
    dicionarioDisciplina[idDisciplina] = Disciplina

#Funções de alterar
def alterarDisciplina():
    idDisciplina = int(input("Digite o ID da disciplina: "))
    Disciplina = dicionarioDisciplina[idDisciplina]
    Disciplina.alterarDados()#Altera somente nome da disciplina e numero
def alterarAlunos():
    identidade = int(input("Digite o ID do Alunos: "))
    Alunos = dicionarioAlunos[identidade]
    dicionarioAlunos[identidade] = Alunos.alterarAlunos()#Altera somente Alunos não utilizados
def alterarProfessor():
    resposta = input("Você deseja alterar um Professor Ativado ou Desativado no sistema de professores? ")
    if (resposta == "Ativado"):
        idDisciplina = int(input("Digite o ID do disciplina: "))
        Disciplina = dicionarioDisciplina[idDisciplina]
        Disciplina.Professor = Disciplina.Professor.alterarProfessor()
        dicionarioDisciplina[idDisciplina] = Disciplina
    elif (resposta == "Desativado"):
        idProfessor = input("Digite o ID do Professor: ")
        Professor = dicionarioProfessores[idProfessor]
        dicionarioProfessores[idProfessor] = Professor.alterarProfessor()
    else:
        print("Não foi feita alteração!")
def alterarSala():
    resposta = input("Você deseja alterar uma Sala Ativada ou Desativada? ")
    if (resposta == "Ativada"):
        idDisciplina = int(input("Digite o ID da disciplina: "))
        Disciplina = dicionarioDisciplina[idDisciplina]
        Disciplina.Sala = Disciplina.Sala.alterarSala()
        dicionarioDisciplina[idDisciplina] = Disciplina
    elif (resposta == "Desativada"):
        idSala = int(input("Digite o ID da Sala: "))
        Sala = dicionarioSalas[idSala]
        dicionarioSalas[Sala] = Sala.alterarSala()
    else:
        print("Não foi feita alteração!")
def alterarlista_alunos():
    idDisciplina = int(input("Digite o ID da disciplina que deseja alterar: "))
    Disciplina = dicionarioDisciplina[idDisciplina]
    for Alunos in Disciplina.lista_alunos:
        print(Alunos)
        resposta = input("Deseja Alterar/Remover/Manter esse Aluno? ")
        if (resposta == "Alterar"):
            comando = " "
            idAlunos = 0
            while (comando != "ID disponível!"):
                idAlunos += 1
                comando = dicionarioAlunos.get(idAlunos, "ID disponível!")
            dicionarioAlunos[idAlunos] = Disciplina.lista_alunos.pop(Alunos)
            idAlunos = int(input("Digite o ID do Aluno que deseja usar: "))
            Disciplina.adicionarAlunos(idAlunos, dicionarioAlunos.pop(idAlunos))
            print("ID do aluno:"+str(idAlunos))
        elif (resposta == "Remover"):
            comando = " "
            idAlunos = 0
            while (comando != "ID disponível!"):
                idAlunos += 1
                comando = dicionarioAlunos.get(idAlunos, "ID disponível!")
            dicionarioAlunos[idAlunos] = Disciplina.lista_alunos.pop(Alunos)
            print("ID do Alunos:"+str(idAlunos))
    dicionarioDisciplina[idDisciplina] = Disciplina

#Funções de deletar
def deletarDisciplina():
    idDisciplina = int(input("Digite o ID do disciplina: "))
    Disciplina = dicionarioDisciplina[idDisciplina]
    for Alunos in Disciplina.lista_alunos:
        comando = " "
        idAlunos = 0
        while (comando != "ID disponível!"):
            idAlunos += 1
            comando = dicionarioAlunos.get(idAlunos, "ID disponível!")
        dicionarioAlunos[idAlunos] = Alunos
    comando = " "
    idProfessor = 0
    while (comando != "ID disponível!"):
        idProfessor += 1
        comando = dicionarioProfessores.get(idProfessor, "ID disponível!")
    dicionarioProfessores[idProfessor] = Disciplina.Professor
    if (Disciplina.Sala != " "):
        comando = " "
        idSala = 0
        while (comando != "ID disponível!"):
            idSala += 1
            comando = dicionarioSalas.get(idSala, "ID disponível!")
        dicionarioSalas[idSala] = Disciplina.Sala
def deletarAlunos():
    idAlunos = int(input("Digite o ID do Alunos: "))
    dicionarioAlunos.pop(idAlunos)#Não é possível remover Alunos utilizados
def deletarProfessor():
    idProfessor = int(input("Digite o ID do Professor: "))
    dicionarioProfessores.pop(idProfessor)#Não é possível remover um Professor ativado para seguir lógica proposta
def deletarSala():
    resposta = input("Você deseja alterar uma Sala Ativado ou Desativado? ")
    if (resposta == "Ativado"):
        idDisciplina = int(input("Digite o ID da disciplina: "))
        Disciplina = dicionarioDisciplina[idDisciplina]
        Disciplina.Sala = " "
    elif (resposta == "Desativado"):
        idSala = int(input("Digite o ID da Sala: "))
        dicionarioSalas.pop(idSala)