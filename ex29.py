def exibir_menu():
    print("Bem-vindo ao menu")
    print("1-Casdastrar")
    print("2-Login")
    print("3-Sair")
    print("----------------------------")

def cadastrar_pessoa(cadastro):
    nome = input("seu nome:")
    idade = input("sua idade:")
    turma = input("sua turma:")
    curso = input("seu curso:")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma,"Curso": curso})
    print("cadastro realizado com sucesso!")