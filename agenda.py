contatos = [
    {'nome': 'Ana Silva', 'telefone': '11999990001', 'email': 'ana@email.com', 'favorito': True},
    {'nome': 'Bruno Costa', 'telefone': '11999990002', 'email': 'bruno@email.com', 'favorito': False},
    {'nome': 'Carla Dias', 'telefone': '11999990003', 'email': 'carla@email.com', 'favorito': True},
]

def adicionar_contato(contatos, nome, telefone, email, favorito):
    contato = {'nome': nome, 'telefone': telefone, 'email': email, 'favorito': favorito}
    contatos.append(contato)
    print(f"\nContato '{nome}' adicionado com sucesso!\n")
    return

def ver_lista(contatos):
    if contatos == []:
        print("\nnao ha nenhum contato cadastrado, adicione contatos primeiro\n")
    else:
        for indice, contato in enumerate(contatos, start=1):
            favorito_str = "sim" if contato['favorito'] else "nao"
            print(f"----------  {indice}  ----------")
            print(f"nome : {contato['nome']}")
            print(f"telefone : {contato['telefone']}")
            print(f"email : {contato['email']}")
            print(f"favorito : {favorito_str}\n")
    return

def editar_contato(contatos):
    if contatos == []:
        print("\nnao ha nenhum contato cadastrado, adicione contatos primeiro\n")
    else:
        indices = []
        for indice, contato in enumerate(contatos, start=1):
            indices.append(str(indice))
            print(f"{indice} -- {contato['nome']}")

        while True:
            escolha = input("\nescolha um contato para editar (use o indice)\n")
            if escolha in indices:
                break
            else:
                print("\nDIGITE UM VALOR VALIDO\n")

        contato = contatos[int(escolha) - 1]

        while True:
            print(f"\nEditando contato '{contato['nome']}':")
            print(f"1- alterar nome (atual: '{contato['nome']}')")
            print(f"2- alterar telefone (atual: '{contato['telefone']}')")
            print(f"3- alterar email (atual: '{contato['email']}')")
            print("4- concluir edicao")

            campo = input("o que deseja alterar? ")

            if campo == "1":
                novo = input(f"novo nome (atual '{contato['nome']}'): ")
                contato['nome'] = novo or contato['nome']
                print("nome atualizado!\n")
            elif campo == "2":
                novo = input(f"novo telefone (atual '{contato['telefone']}'): ")
                contato['telefone'] = novo or contato['telefone']
                print("telefone atualizado!\n")
            elif campo == "3":
                novo = input(f"novo email (atual '{contato['email']}'): ")
                contato['email'] = novo or contato['email']
                print("email atualizado!\n")
            elif campo == "4":
                print("edicao concluida!\n")
                break
            else:
                print("\nDIGITE UM VALOR VALIDO\n")

    return contatos

def alternar_favorito(contatos):
    if contatos == []:
        print("\nnao ha nenhum contato cadastrado, adicione contatos primeiro\n")
    else:
        indices = []
        for indice, contato in enumerate(contatos, start=1):
            indices.append(str(indice))
            favorito_str = "sim" if contato['favorito'] else "nao"
            print(f"{indice} -- {contato['nome']} | favorito: {favorito_str}")

        while True:
            escolha = input("\nescolha um contato para marcar/desmarcar como favorito (use o indice)\n")
            if escolha in indices:
                break
            else:
                print("\nDIGITE UM VALOR VALIDO\n")

        contato = contatos[int(escolha) - 1]
        contato['favorito'] = not contato['favorito']
        status = "marcado como favorito" if contato['favorito'] else "removido dos favoritos"
        print(f"\n'{contato['nome']}' foi {status}!\n")

    return contatos

def ver_favoritos(contatos):
    favoritos = [c for c in contatos if c['favorito']]
    if favoritos == []:
        print("\nnao ha nenhum contato favorito cadastrado\n")
    else:
        print("\n===== CONTATOS FAVORITOS =====\n")
        for indice, contato in enumerate(favoritos, start=1):
            print(f"----------  {indice}  ----------")
            print(f"nome : {contato['nome']}")
            print(f"telefone : {contato['telefone']}")
            print(f"email : {contato['email']}\n")
    return

def apagar_contato(contatos):
    if contatos == []:
        print("\nnao ha nenhum contato cadastrado, adicione contatos primeiro\n")
    else:
        ver_lista(contatos)
        indices = [str(i + 1) for i in range(len(contatos))]

        while True:
            escolha = input("digite o indice do contato que deseja apagar ")
            if escolha in indices:
                break
            else:
                print("\nDIGITE UM VALOR VALIDO\n")

        contato = contatos[int(escolha) - 1]

        while True:
            confirma = input(f"tem certeza que deseja apagar '{contato['nome']}' ? (s/n)\n").lower()
            if confirma == "s":
                contatos.pop(int(escolha) - 1)
                print(f"o contato '{contato['nome']}' foi apagado!\n")
                break
            elif confirma == "n":
                print("operacao cancelada\n")
                break
            else:
                print("\nDIGITE UM VALOR VALIDO\n")

    return contatos


while True:
    input("-----------------------------------------")

    print("1- Adicionar contato")
    print("2- Visualizar lista de contatos")
    print("3- Editar contato")
    print("4- Marcar/desmarcar contato como favorito")
    print("5- Visualizar contatos favoritos")
    print("6- Apagar contato")
    print("7- Sair")

    opcao = input("escolha ")

    if opcao == "1":
        nome = input("nome do contato: ")
        telefone = input("telefone do contato: ")
        email = input("email do contato: ")
        while True:
            fav = input("favorito? (s/n) ").lower()
            if fav == "s":
                favorito = True
                break
            elif fav == "n":
                favorito = False
                break
            else:
                print("\nDIGITE UM VALOR VALIDO\n")
        adicionar_contato(contatos, nome or "sem nome", telefone or "sem telefone", email or "sem email", favorito)

    elif opcao == "2":
        ver_lista(contatos)

    elif opcao == "3":
        contatos = editar_contato(contatos)

    elif opcao == "4":
        contatos = alternar_favorito(contatos)

    elif opcao == "5":
        ver_favoritos(contatos)

    elif opcao == "6":
        contatos = apagar_contato(contatos)

    elif opcao == "7":
        break

    else:
        print("\nDIGITE UM VALOR VALIDO\n")

print("\n-----------------------------------------------\n voce encerrou o programa")
print("o programa foi encerrado")
