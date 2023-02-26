class Phonebook:

    msg_invalid_name = 'Nome inválido'
    msg_invalid_number = 'Número inválido'
    msg_add_name = 'Número adicionado'
    msg_name_duplicated = 'Usuário já existente'
    msg_absent_contact = 'Usuário não existe'
    msg_phonebook_empty = 'Agenda não possui contatos'
    msg_delete_contact = 'Contato excluído'
    msg_edit_contact = 'Contato atualizado'

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    """
    Adição de um método para validar se o contato é None ou vazio.
    Este método pode ser usado tanto para o nome quanto para o telefone.
    """

    # Verifica se o nome ou número é None ou vazio.
    def is_none_or_empty(self, contact):
        return contact is None or contact == ''

    """
    Adição de um método para validar o nome. A verificação foi removida dos métodos que a utilizam.
    """

    # Verificar se o nome é inválido.
    def validate_name(self, name):
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

    """
    Adição de um método para validar o número de telefone.
    Alteração do tamanho do número de telefone para 3 dígitos.
    """
    # Verifica se o número de telefone contém mais de 3 dígitos
    def valid_number(self, number):
        return len(number) < 3

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        # Validações
        """
        Retorna True para o caso de algum cado incorreto
        1 - Nome vazio ou None.
        2 - Nome inválido.
        3 - Número vazio ou None.
        4 - Número de telefone menor que 3 dígitos.
        """
        if self.is_none_or_empty(name):
            # Modificação do retorno do usuário corrigindo erros de ortografia.
            return self.msg_invalid_name

        if self.validate_name(name):
            # Modificação do retorno do usuário corrigindo erros de ortografia.
            return self.msg_invalid_name

        if self.is_none_or_empty(number):
            # Modificação do retorno do usuário corrigindo erros de ortografia.
            return self.msg_invalid_number

        if self.valid_number(number):
            # Modificação do retorno do usuário corrigindo erros de ortografia.
            return self.msg_invalid_number

        """
        Verifica se o contato já existe.
        Caso não exista, adiciona o contato no dicionário.
        """
        if name in self.entries:
            # Modificação do retorno do usuário corrigindo erros de ortografia.
            return self.msg_name_duplicated
        else:
            self.entries[name] = number
            return self.msg_add_name

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        # Validações
        """
        Remoção da validação do nome de usuário. Esta validação é realizada pelo método validate_name()
        1 - Nome vazio ou None.
        2 - Nome inválido.
        """
        if self.is_none_or_empty(name):
            return self.msg_invalid_name

        if self.validate_name(name):
            return self.msg_invalid_name

        # Verifica se o contato está cadastrado.
        if name in self.entries:
            return self.entries[name]
        else:
            # Mensagem de retorno informando que o contato não existe.
            return self.msg_absent_contact

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        """
        Correção: Ajuste do retorno dos nomes de contato. O retorno é uma lista de nomes.
        Alteração do retorno do método. Neste caso será retornado uma lista contendo os nomes dos contatos.
        Caso a lista esteja vazia, será retornado para o usuário uma mensagem infoprmativa.
        """
        if self.entries:
            names_list = []
            for name in self.entries.keys():
                names_list.append(name)
            return names_list
        else:
            # Mensagem de retorno informando que não existe contatos na lista.
            return self.msg_phonebook_empty

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        """
        Correção: Ajuste do retorno dos numeros de telefone. O retorno é uma lista de números.
        Neste caso será retornado uma lista contendo os números dos contatos.
        Caso a lista esteja vazia, será retornado para o usuário uma mensagem infoprmativa.
        """
        if self.entries:
            numbers_list = []
            for number in self.entries.values():
                numbers_list.append(number)
            return numbers_list
        else:
            # Mensagem de retorno informando que não existe contatos na lista.
            return self.msg_phonebook_empty

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        # Alteração da mensagem de retorno.. Mensagem de retorno informando que a lista está vazia.
        return self.msg_phonebook_empty

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        """
        Correção: dicionário em python não aceita chaves duplicadas.
        Neste caso, será alterado para retornar uma lista com o contato pesquisado.
        """
        # Validações
        """
        1 - Nome vazio ou None.
        2 - Nome inválido.
        """
        if self.is_none_or_empty(search_name):
            # Modificação do retorno do usuário corrigindo erros de ortografia.
            return self.msg_invalid_name

        if self.validate_name(search_name):
            # Modificação do retorno do usuário corrigindo erros de ortografia.
            return self.msg_invalid_name

        # Verifica se o contato está cadastrado e consequentemente se a lista está vazia..
        if search_name in self.entries:
            result = [search_name, self.entries[search_name]]
            return result
        else:
            # Mensagem de retorno informando que o contato não existe na lista.
            return self.msg_absent_contact

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        '''
        Correção: o método foi alterado para retornar todos os números em ordem crescente.
        '''
        if self.entries:
            numbers_list = self.get_numbers()
            numbers_list.sort()
            return numbers_list
        else:
            # Mensagem de retorno informando que não existe contatos na lista.
            return self.msg_phonebook_empty

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        '''
        Correção: o método foi alterado para retornar todos os números em ordem decrescente.
        '''
        if self.entries:
            numbers_list = self.get_numbers()
            numbers_list.sort(reverse=True)
            return numbers_list
        else:
            # Mensagem de retorno informando que não existe contatos na lista.
            return self.msg_phonebook_empty

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
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
            self.entries.pop(name)
            return self.msg_delete_contact
        else:
            return self.msg_absent_contact

    """
    Método novo.
    """
    def change_number(self, name, new_number):
        """
        Edit a user number
        :param name: name of person in string
        :param new_number: number of person in string
        :return: return 'Contato atualizado' or 'Contato inexistente'
        """
        # Validações
        """
        1 - Número vazio ou None.
        2 - Número de telefone menor que 3 dígitos.
        """
        if self.is_none_or_empty(new_number):
            # Mensagem de retorno informando que o número é inválido.
            return self.msg_invalid_number

        if self.valid_number(new_number):
            # Mensagem de retorno informando que o número é inválido.
            return self.msg_invalid_number

        """
        Verifica se o contato já existe.
        """
        if name in self.entries:
            self.entries[name] = new_number
            return self.msg_edit_contact
        else:
            return self.msg_absent_contact

    def get_name_by_number(self, number):
        """
        Search for a user by number
        :param number: number of person in string
        :return: return name or 'Contato inexistente'
        """
        for name in self.entries:
            if self.entries[name] == number:
                return name
        return self.msg_absent_contact
