from src.phonebook import Phonebook

contatos = Phonebook()
#
# contatos.add('Enquanto isso', '9978876')
# contatos.add('Galo da madrugada', '10000000')


nome_valido = 'Homem da meia noite'
numero_valido = '389457'
nome_valido2 = 'Zomem da meia noite'
numero_valido2 = '0'

contatos.add(nome_valido, numero_valido)
contatos.add(nome_valido2, numero_valido2)

resultado = contatos.get_phonebook_reverse()
print(resultado)

# lista = contatos.get_phonebook_sorted()

# print(lista)


# contatos_lista = contatos.get_names()
# a = dict(contatos_lista)
# print(a)

#print(contatos.entries)

# print(contatos.get_names())

# print(['POLICIA', 'Homem da meia noite'] == ['POLICIA', 'Homem da meia noite'])
# lista = contatos.get_phonebook_sorted()
# print(lista)
#
# lista_esperada = {'Homem da meia noite': '389457', 'POLICIA': '190', 'Zomem da meia noite': '0'}
#
# for n in lista_esperada.values():
#     print(n)
