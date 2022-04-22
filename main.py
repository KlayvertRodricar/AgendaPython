import Function


while True:
    
    escolha = int(input("Escolha uma opção:\n"
    "***********************\n"
    "1.Adicionar contato\n"
    "2.Ver lista contato\n"
    "3.Editar contato\n"
    "4.Remover contato\n"
    "0.Sair\n"
    "***********************\n"))
    if escolha == 1:
        Function.add_contato()
    elif escolha == 2:
        Function.ver_contato()
    elif escolha == 3:
        Function.editar_contato()
    elif escolha == 4:
        Function.remover_contato()
    elif escolha == 0:
        exit(0)
    else:
        print("Escolha somente uma das opções definidas pelo menu!")