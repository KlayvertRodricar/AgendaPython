import Action as act
import time

def add_contato():
    lista_celular = []
    while True:
        nome_cntt = str(input("Nome: ")).title()
        if act.checkup(nome_cntt):
            print("Este contato já existe, insira um difente")
        else:
            break
    sobnome_cntt = str(input("Digite o sobrenome: ")).title()
    while True:
        celular = int(input("Digite o celular: "))
        lista_celular.append(celular)
        decisao = str(input("Deseja adicionar outro número de celular?(S/N)")).upper()
        if decisao == "S":
            pass
        else:
            break
    endereco = str(input("Digite o endereço: ")).title()
    act.add(nome_cntt, sobnome_cntt, lista_celular, endereco)

def ver_contato():
    print("Mostrando lista...")
    act.ver()

def editar_contato():
    choice = int(input("Escolha a opção que deseja editar:\n1.Nome\n2.Sobrenome\n3.Celular\n4.Endereço\n"))
    aux_busca = str(input("Digite o nome do contato que deseja editar: ")).title()
    act.editar(choice, aux_busca)
    
def remover_contato():
    aux_busca = str(input("Digite o nome de quem você deseja deletar: ")).title()
    act.apagar(aux_busca)