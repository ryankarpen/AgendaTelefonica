import agenda


def menu():
    print('\033[34m-=-\033[m' * 34)
    print('\033[1:36:40m{:^100}\033[m'.format('AGENDA TELEFÔNICA'))
    print('\033[34m-=-\033[m' * 34)
    print('1 - Cadastrar novo contato')
    print('2 - Mostrar sua lista de contatos')
    print('3 - Excluir contato')
    print('4 - Atualizar nome do contato')
    print('5 - Atualizar número do contato')
    print('6 - Sair da Agenda Telefônica')


while True:
    menu()
    resp = int(input('Informe a opção desejada:'))
    pessoa = agenda.Agenda()
    if resp == 6:
        break

    elif resp == 1:
        pessoa.cadastrar_contato(str(input('Informe o nome do contato:')), int(input('Informe seu DDD:')),
                                 int(input('Informe seu telefone:')))
    elif resp == 2:
        pessoa.mostrar_agenda()

    elif resp == 3:
        pessoa.excluir_contato(str(input('informe o nome do contato que deseja excluir:')))

    elif resp == 4:
        pessoa.atualizar_nome(str(input('Informe o contato que deseja renomear:')),
                              str(input('Informe seu novo nome:')))

    elif resp == 5:
        pessoa.atualizar_numero(str(input('informe o contato que deseja atualizar o número:')),
                                int(input('Informe o novo número:')))


