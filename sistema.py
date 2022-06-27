from func import *

print("Bem vindo ao sistema escolar de organização de disciplinas\n Qual função voce deseja realizar?")

comando=""
while (comando != "Sair"):
    acao = input("Que ação você deseja tomar (Criar/Mostrar/Relacionar/Alterar/Deletar/Sair)?\n")
    opcao= " "
    if (acao == "Criar"):
        opcao = input("Digite uma das seguintes opções (Disciplinas/Alunos/Professor/Sala):\n")
        if (opcao == "Disciplinas"):
            criarDisciplina()
        elif (opcao == "Alunos"):
            criarAlunos()
        elif (opcao == "Professor"):
            criarProfessor()
        elif (opcao == "Sala"):
            criarSala()
        else:
            print("Essa opção não existe!")
    elif(acao == "Mostrar"):
        opcao = input("Digite uma das seguintes opções (Disciplinas/Alunos/Professores/Salas):\n")
        if (opcao == "Disciplinas"):
            for idDisciplina in dicionarioDisciplina:
                print(dicionarioDisciplina[idDisciplina])
        elif (opcao == "Alunos"):
            for idAlunos in dicionarioAlunos:
                print(dicionarioAlunos[idAlunos])
        elif (opcao == "adicionar Professores"):
            for idProfessor in dicionarioProfessores:
                print(dicionarioProfessores[idProfessor])
        elif (opcao == "adicionar Salas"):
            for idSala in dicionarioSalas:
                print(dicionarioSalas[idSala])
        else:
            print("Essa opção não existe!")
    elif(acao == "Relacionar"):
        opcao = input("Digite uma das seguintes opções (Professor/Sala/Alunos):\n")
        if (opcao == "Professor"):
            relacionarProfessor()
        elif (opcao == "Sala"):
            relacionarSala()
        elif (opcao == "Alunos"):
            relacionarAlunos()
        else:
            print("Essa opção não existe!")
    elif(acao == "Alterar"):
        opcao = input("Digite uma das seguintes opções (Disciplinas/Alunos/Professor/Sala):\n")
        if (opcao == "Disciplinas"):
            alterarDisciplina()
        elif (opcao == "Alunos"):
            alterarAlunos()
        elif (opcao == "Professor"):
            alterarProfessor()
        elif (opcao == "Sala"):
            alterarSala()
        elif (opcao == "Alunos"):
            alterarAlunos()
        else:
            print("Essa opção não existe!")
    elif(acao == "Deletar"):
        opcao = input("Digite uma das seguintes opções (Disciplinas/Alunos/Professor/Sala):\n")
        if (opcao == "Disciplinas"):
            deletarDisciplina()
        elif (opcao == "Alunos"):
            deletarAlunos()
        elif (opcao == "Professor"):
            deletarProfessor()
        elif (opcao == "Sala"):
            deletarSala()
        else:
            print("Essa opção não existe!")
    elif(acao == "Sair"):
        comando = acao
    else:
        print("Essa opção não existe!")
