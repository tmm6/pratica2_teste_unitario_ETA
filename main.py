from src.phonebook import Phonebook

contatos = Phonebook()
result = contatos.add('Bruce Wayne', '9978876')
# print(result)
print('\n')
# result = contatos.add('Bruce Wayne', '9978798876')
# print(result)
# print('Duplicado \n')
contatos.add('Kal-el', '76786786')
print(contatos.entries)

# result = contatos.get_name_by_number('00000')
# print(result)
#
# result = contatos.get_name_by_number('9978876')
# print(result)


# print('\n Lookup')
# print(contatos.lookup(None))
#
# print(contatos.lookup('Kal-el'))
# print(contatos.lookup('Gilbert'))
# print(contatos.lookup(''))
#
# print('\nGet names')
# print(contatos.get_names())
# #contatos.clear()
# print(contatos.get_names())

# print('\nGet numbers')
# print(contatos.get_numbers())
# contatos.clear()
# print(contatos.get_numbers())

# result = contatos.add('Kal-el', '76786786')
# print(result)
# print('Adicionado \n')


# result = contatos.add('Kal-el', '1')
# print(result)
# print('Número < 3 \n')

# print('\nValidacao nome e numero')
# result = contatos.add('', '675')
# print(result)
# print('Nome == vazio \n')

# result = contatos.add('Kal-el', None)
# print(result)
# print('Número == None \n')


# result = contatos.add(None, '675')
# print(result)
# print('Nome == None \n')
#
# result = contatos.add('Kal-el', '')
# print(result)
# print('Número == vazio \n')


# print('\nSearch')
# result = contatos.search('Kal-el')
# print(result)
#
# result = contatos.search('Damian')
# print(result)

# contatos.clear()
# result = contatos.search('Kal-el')
# print(result)

# print('\nSort')
# result = contatos.get_phonebook_sorted()
# print(result)
# #
# print('\nSort reverse')
# result = contatos.get_phonebook_reverse()
# print(result)

# contatos.clear()
# result = contatos.get_phonebook_reverse()
# print(result)

# print('\nDelete')
# result = contatos.delete('Kalel')
# print(result)
#
# result = contatos.delete('Bruce Wayne')
# print(result)
# print(contatos.entries)
#
# contatos.clear()
# result = contatos.delete('Kal-el')
# print(result)

# print('\nChange number')
# resultado = contatos.change_number('Kal-el', '000000')
# print(resultado)
# print(contatos.entries)
#
# resultado = contatos.change_number('Kalel', '0080000')
# print(resultado)
# print(contatos.entries)
#
# resultado = contatos.change_number('Kalel', '0')
# print(resultado)
# print(contatos.entries)
#
# resultado = contatos.change_number('Kalel', None)
# print(resultado)
# print(contatos.entries)
#
# resultado = contatos.change_number('@', '0080000')
# print(resultado)
# print(contatos.entries)
#
# contatos.clear()
# resultado = contatos.change_number('Kalel', '0089080000')
# print(resultado)
# print(contatos.entries)

# print('\nGet name by number')
# resultados = contatos.get_name_by_number('76786786')
# print(resultados)