class Phonebook:

    msg_invalid_name = 'Nome inválido'
    msg_invalid_number = 'Número inválido'
    msg_add_name = 'Número adicionado'
    msg_name_duplicated = 'Usuário já existente'
    msg_absent_contact = 'Usuário não existe'
    msg_phonebook_empty = 'Agenda não possui contatos'

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    """
    Adição de um método para validar se o contato possue None ou Vazio.
    Este método pode ser usado tanto para o nome quanto para o telegone
    """
    # Verifica se o nome ou número é None ou vazio.
    def is_none_or_empty(self, contact):
        if contact is None or contact == '':
            return True
        else:
            return False

    """
    Adição de um método para validar o nome.
    """
    # Verificar se o nome é inválido.
    def validate_name(self, name):
        """
        Modificação da mensagem de retorno de usuário inválido corrigindo erros de ortografia.
        Refatoração da condicional e adição do nome == '' e nome == None.
        """
        # Validação do campo nome
        if '#' in name:
            return True
        if '@' in name:
            return True
        if '!' in name:
            return True
        if '$' in name:
            return True
        if '%' in name:
            return True

        return False

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        # Validações
        """
        1 - Nome vazio ou None.
        2 - Nome inválido.
        3 - Número vazio ou None
        """
        if self.is_none_or_empty(name):
            return self.msg_invalid_name

        if self.validate_name(name):
            return self.msg_invalid_name

        if self.is_none_or_empty(number):
            return self.msg_invalid_number

        """
        Modificação do retorno do usuário corrigindo erros de ortografia.
        Alteração do tamanho do número de telefone para 3 dígitos.
        """
        if len(number) < 3:
            return self.msg_invalid_number

        """
        Modificação do retorno do usuário corrigindo erros de ortografia.
        Adição de um else para caso o usuário já possua seu contato cadastrado na lista.
        """
        # Valida se o contato (nome+número) já existe na lista.
        if name not in self.entries:
            self.entries[name] = number
        else:
            return self.msg_name_duplicated

        return self.msg_add_name

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        """
        Remoção da validação do nome de usuário. Esta validação é realizada pelo método validate_name()
        """
        # Validações
        """
        1 - Nome vazio ou None.
        2 - Nome inválido.
        """
        if self.is_none_or_empty(name):
            return self.msg_invalid_name

        if self.validate_name(name):
            return self.msg_invalid_name

        """
        Adição de uma condicional para verificar se o contato existe na lista.
        """
        # Verifica se o contato está cadastrado.
        if name in self.entries:
            return self.entries[name]
        else:
            return self.msg_absent_contact

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        """
        Correção: Ajuste do retorno dos nomes de contato.
        Alteração do retorno do método. Neste caso será retornado uma lista contendo os nomes dos contatos.
        Caso a lista esteja vazia, será retornado para o usuário uma mensagem infoprmativa.
        """
        if len(self.entries) != 0:
            names_list = []
            for name in self.entries.keys():
                names_list.append(name)
            return names_list
        else:
            return self.msg_phonebook_empty

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        """
        Correção: Ajuste do retorno dos numeros de telefone.
        Neste caso será retornado uma lista contendo os números dos contatos.
        Caso a lista esteja vazia, será retornado para o usuário uma mensagem infoprmativa.
        """
        if len(self.entries) != 0:
            numbers_list = []
            for number in self.entries.values():
                numbers_list.append(number)
            return numbers_list
        else:
            return self.msg_phonebook_empty

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        """
        Alteração da mensagem de retorno.
        """
        self.entries = {}
        return self.msg_phonebook_empty

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        """
        Correção: dicionário em python não aceita chaves duplicadas.
        Neste caso, será alterado para retornar a listra com o contato pesquisado.
        """
        # Validações
        """
        1 - Nome vazio ou None.
        2 - Nome inválido.
        """
        if self.is_none_or_empty(search_name):
            return self.msg_invalid_name

        if self.validate_name(search_name):
            return self.msg_invalid_name

        """
        Adição de uma condicional para verificar se o contato existe na lista.
        """
        # Verifica se o contato está cadastrado.
        if search_name in self.entries:
            result = [search_name, self.entries[search_name]]
        else:
            return self.msg_absent_contact

        return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        '''
        Correção: o método foi alterado para retornar todos os números em ordem crescente.
        '''
        if len(self.entries) != 0:
            numbers_list = self.get_numbers()
            numbers_list.sort()
            return numbers_list
        else:
            return self.msg_phonebook_empty

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
