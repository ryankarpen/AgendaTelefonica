from vetores import vetor
from Listas import lista_ligada

print('-'*30, 'MENU', '-'*30)
print('1 - Vetores')
print('2 - Listas Ligadas')

menu = int(input('Informe a opção desejada:'))

if menu == 1:
    vetor_teste = vetor.Vetor(3)
    # vetor_teste.inserir_elemento_posicao(1, 0)
    # vetor_teste.inserir_elemento_posicao(5, 1)
    vetor_teste.inserir_elemento_final(1)
    vetor_teste.inserir_elemento_final(2)
    print(vetor_teste)

elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(5)
    lista_teste.inserir(7)
    print(lista_teste)







