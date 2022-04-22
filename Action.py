import Function
lista_contato = []
    
def checkup(nome_cntt):
    if len(lista_contato) > 0:
        for c in range(len(lista_contato)):
            if lista_contato[c][0] == nome_cntt:
                return True
    else:
        return False

def add(nome_cntt, sobnome_cntt, lista_celular, endereco):
    lista_contato.append([nome_cntt, sobnome_cntt, lista_celular, endereco])

def ver():
    if len(lista_contato) < 1:
        print("Lista de contatos vazia")
        print("")
    else:
        for c in range(len(lista_contato)):
            print(f"Nome: {lista_contato[c][0]}\n"
            f"sobrenome: {lista_contato[c][1]}\n"
            f"Celular: {lista_contato[c][2]}\n"
            f"Endereço: {lista_contato[c][3]}\n")


def editar(choice, aux_busca):
    if len(lista_contato) > 0:
        while True:
            for c in range(len(lista_contato)):
                if aux_busca == lista_contato[c][0]:

                    if choice == 1:
                        novo_nome = str(input("Novo nome: ")).title()
                        lista_contato[c][0] = novo_nome
                        break

                    elif choice == 2:
                        novo_sobnome = str(input("Novo sobrenome: ")).title()
                        lista_contato[c][1] = novo_sobnome
                        break

                    elif choice == 3:
                        lista_novo_celular = []
                        while True:
                            novo_celular = int(input("Novo celular: "))
                            lista_novo_celular.append(novo_celular)
                            choice = str(input("Deseja adicionar mais algum número?(S/N)")).upper()
                            if choice == "S":
                                pass
                            else:
                                lista_contato[c][2] = lista_novo_celular
                                break

                    elif choice == 4:
                        novo_endereço = str(input("Novo endereço: ")).title()
                        lista_contato[c][3] = novo_endereço
                        break

                    else:
                        print("Escolha somente opções válida do menu")

                else:
                    pass
            break
    else:
        print("Sua lista de contato está vazia")

def apagar(aux_busca):
    while True:
        for n in range(len(lista_contato)):
            if aux_busca == lista_contato[n][0]:
                confirmacao = str(input(f"Realmente deseha deletar o contato: {lista_contato[n]}.(S/N)")).title()
                if confirmacao == "S":
                    lista_contato.pop(n)
                    print("Contato removido!")
                    break
                else:
                    pass
            else:
                pass
            print("Contato não localizado!")
        break