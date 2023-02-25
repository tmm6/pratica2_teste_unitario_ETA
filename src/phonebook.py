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
    def is_none_or_empty(self, contact):
        return contact is None or contact == '' # Verifica se o nome ou número é None ou vazio.

    """
    Adição de um método para validar o nome.
    """
    def validate_name(self, name): # Verificar se o nome é inválido.
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
    def valid_number(self, number): # Verifica se o número de telefone contém mais de 3 dígitos
        return len(number) < 3

    """
    Adição de um método para validar se a lista telefônica está vazia.
    """
    def phonebook_is_empty(self):
        return len(self.entries) == 0

    """
    Adição de um método para identificar se um nome existe no dicionário.
    Adição de um else para caso o usuário já possua seu contato cadastrado na lista.
    """
    def contact_in_list(self, name): # Verifica se o nome já existe no dicionário.
        if name in self.entries:
            return True
        else:
            return False



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
            return self.msg_invalid_name # Modificação do retorno do usuário corrigindo erros de ortografia.

        if self.validate_name(name):
            return self.msg_invalid_name # Modificação do retorno do usuário corrigindo erros de ortografia.

        if self.is_none_or_empty(number):
            return self.msg_invalid_number # Modificação do retorno do usuário corrigindo erros de ortografia.

        if self.valid_number(number):
            return self.msg_invalid_number # Modificação do retorno do usuário corrigindo erros de ortografia.

        """
        Verifica se o contato já existe.
        Caso não exista, adiciona o contato no dicionário.
        """
        if self.contact_in_list(name):
            return self.msg_name_duplicated # Modificação do retorno do usuário corrigindo erros de ortografia.
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
        3 - Verifica se a lista está vazia.
        """
        if self.is_none_or_empty(name):
            return self.msg_invalid_name

        if self.validate_name(name):
            return self.msg_invalid_name

        if self.phonebook_is_empty():
            return self.msg_phonebook_empty  # Mensagem de retorno informando que não existe contatos na lista.

        # Verifica se o contato está cadastrado.
        if self.contact_in_list(name):
            return self.entries[name]
        else:
            return self.msg_absent_contact # Mensagem de retorno informando que o contato não existe.

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        """
        Correção: Ajuste do retorno dos nomes de contato. O retorno é uma lista de nomes.
        Alteração do retorno do método. Neste caso será retornado uma lista contendo os nomes dos contatos.
        Caso a lista esteja vazia, será retornado para o usuário uma mensagem infoprmativa.
        """
        if self.phonebook_is_empty():
            return self.msg_phonebook_empty # Mensagem de retorno informando que não existe contatos na lista.
        else:
            names_list = []
            for name in self.entries.keys():
                names_list.append(name)
            return names_list

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        """
        Correção: Ajuste do retorno dos numeros de telefone. O retorno é uma lista de números.
        Neste caso será retornado uma lista contendo os números dos contatos.
        Caso a lista esteja vazia, será retornado para o usuário uma mensagem infoprmativa.
        """
        if self.phonebook_is_empty():
            return self.msg_phonebook_empty # Mensagem de retorno informando que não existe contatos na lista.
        else:
            numbers_list = []
            for number in self.entries.values():
                numbers_list.append(number)
            return numbers_list

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        """
        Alteração da mensagem de retorno.
        """
        self.entries = {}
        return self.msg_phonebook_empty # Mensagem de retorno informando que a lista está vazia.

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
        3 - Verifica se a lista está vazia.
        """
        if self.is_none_or_empty(search_name):
            return self.msg_invalid_name # Modificação do retorno do usuário corrigindo erros de ortografia.

        if self.validate_name(search_name):
            return self.msg_invalid_name # Modificação do retorno do usuário corrigindo erros de ortografia.

        if self.phonebook_is_empty():
            return self.msg_phonebook_empty  # Mensagem de retorno informando que não existe contatos na lista.

        if self.contact_in_list(search_name):
            # Verifica se o contato está cadastrado.
            result = [search_name, self.entries[search_name]]
            return result
        else:
            return self.msg_absent_contact # Mensagem de retorno informando que o contato não existe na lista.

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        '''
        Correção: o método foi alterado para retornar todos os números em ordem crescente.
        '''
        if self.phonebook_is_empty():
            return self.msg_phonebook_empty # Mensagem de retorno informando que não existe contatos na lista.
        else:
            numbers_list = self.get_numbers()
            numbers_list.sort()
            return numbers_list

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        '''
        Correção: o método foi alterado para retornar todos os números em ordem decrescente.
        '''
        if self.phonebook_is_empty():
            return self.msg_phonebook_empty # Mensagem de retorno informando que não existe contatos na lista.
        else:
            numbers_list = self.get_numbers()
            numbers_list.sort(reverse=True)
            return numbers_list

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
        3 - Verifica se a lista está vazia
        """
        if self.is_none_or_empty(name):
            return self.msg_invalid_name

        if self.validate_name(name):
            return self.msg_invalid_name

        if self.phonebook_is_empty():
            return self.msg_phonebook_empty  # Mensagem de retorno informando que não existe contatos na lista.
        """
        Adição de uma condicional para verificar se o contato existe na lista.
        """
        # Verifica se o contato está cadastrado.
        if self.contact_in_list(name):
            self.entries.pop(name)
            return self.msg_delete_contact
        else:
            return self.msg_absent_contact

    """
    Método novo.
    """
    def change_number(self, name, new_number):
        # Validações
        """
        1 - Número vazio ou None.
        2 - Número de telefone menor que 3 dígitos.
        3 - Agenda vazia.
        """

        if self.is_none_or_empty(new_number):
            return self.msg_invalid_number # Mensagem de retorno informando que o número é inválido.

        if self.valid_number(new_number):
            return self.msg_invalid_number # Mensagem de retorno informando que o número é inválido.

        if self.phonebook_is_empty():
            return self.msg_phonebook_empty  # Mensagem de retorno informando que não existe contatos na lista.

        """
        Verifica se o contato já existe.
        """
        if self.contact_in_list(name):
            self.entries[name] = new_number
            return self.msg_edit_contact
        else:
            return self.msg_absent_contact

    def get_name_by_number(self, number):
        if self.phonebook_is_empty():
            return self.msg_phonebook_empty  # Mensagem de retorno informando que não existe contatos na lista.

        for name in self.entries:
            if self.entries[name] == number:
                return name
        return self.msg_absent_contact






