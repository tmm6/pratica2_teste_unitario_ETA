class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nme invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalio'
        if '%' in name:
            return 'Nome invalido'

        if len(number) < 0:
            return 'Numero invalid'

    # Retirar essa condicional para o search fazer sentido de retornar uma lista.
        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nme invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome nvalido'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()
    '''
    lista = []
        for name in self.entries.keys():
            lista.append(name)
        return lista
    '''
    ''' Fazer tratamento para o retorno dos contatos ser mais amigavel ['POLICIA', 'Homem da meia noite']'''

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        '''
        Correção: Ajuste do retorno dos numeros de telefone
        '''
        lista_numeros = []
        for number in self.entries.values():
            lista_numeros.append(number)
        return lista_numeros

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        # Sera que nao teria que criar um outro contato para limpar o dicionario?
        # Existe algum outro metodo mais correto.
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        '''
        Correção: o método foi alterado para retornar todos os números em ordem crescente.
        '''
        lista_numeros = self.get_numbers()

        lista_numeros.sort()
        return lista_numeros

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        '''
        Correção: o método foi alterado para retornar todos os números em ordem decrescente.
        '''
        lista_numeros = self.get_numbers()

        lista_numeros.sort(reverse=True)
        return lista_numeros


    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'
