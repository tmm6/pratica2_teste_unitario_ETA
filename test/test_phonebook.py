import pytest

from src.phonebook import Phonebook


class TestPhonebook:
    """
    Utilização do fixture.
    """
    @pytest.fixture
    def msg_add_name(self):
        return 'Número adicionado'
    @pytest.fixture
    def msg_invalid_name(self):
        return 'Nome inválido'

    @pytest.fixture
    def msg_invalid_number(self):
        return 'Número inválido'

    @pytest.fixture
    def msg_name_duplicated(self):
        return 'Usuário já existente'

    @pytest.fixture
    def msg_absent_contact(self):
        return 'Usuário não existe'

    @pytest.fixture
    def msg_phonebook_empty(self):
        return 'Agenda não possui contatos'

    @pytest.fixture
    def msg_delete_contact(self):
        return 'Contato excluído'

    @pytest.fixture
    def msg_change_number(self):
        return 'Número modificado'
    @pytest.fixture
    def name_user(self):
        return 'Violet Evergarden'

    @pytest.fixture
    def number_user(self):
        return '54654754'

    """
    Testes
    """
    # TESTES VALIDAÇÃO DOS CAMPOS
    def test_contato_invalido(self):
        # Setup
        invalid_name_list = ['#alf', 'jk@h', 'df!hj', '$kh', '%kdsgh']
        contact_list = Phonebook()
        result_list = []
        msg_list = [True, True, True, True, True]

        # Chamada
        for invalid_name in invalid_name_list:
            result = contact_list.validate_name(invalid_name)
            result_list.append(result)

        # Asserts
        assert result_list == msg_list

    def test_contato_vazio_none(self):
        # Setup
        invalid_name_list = ['', None]
        contact_list = Phonebook()
        result_list = []
        msg_list = [True, True]

        # Chamada
        for invalid_name in invalid_name_list:
            result = contact_list.is_none_or_empty(invalid_name)
            result_list.append(result)

        # Asserts
        assert result_list == msg_list


    # TESTES ADIÇÃO CONTATO
    # Teste para adição de um contato válido
    def test_add_contato(self, name_user, number_user, msg_add_name):
        # Setup
        contact_list = Phonebook()
        length_contact_list = 2
        # Chamada
        result = contact_list.add(name_user, number_user)

        # Asserts
        assert result == msg_add_name
        assert contact_list.entries[name_user] == number_user
        assert len(contact_list.entries) == length_contact_list

    def test_add_contato_duplicado(self, name_user, number_user, msg_name_duplicated):
        # Setup
        length_contact_list = 2
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)

        # Chamada
        result = contact_list.add(name_user, number_user)

        # Asserts
        assert result == msg_name_duplicated
        assert len(contact_list.entries) == length_contact_list

    def test_numero_invalido(self, name_user, msg_invalid_number):
        # Setup
        invalid_number = '1'
        length_contact_list = 1
        contact_list = Phonebook()

        # Chamada
        result = contact_list.add(name_user, invalid_number)

        # Asserts
        assert result == msg_invalid_number
        assert len(contact_list.entries) == length_contact_list

    # TESTES PARA O MÉTODO LOOKUP
    def test_lookup(self, name_user, number_user):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)

        # Chamada
        result = contact_list.lookup(name_user)

        # Asserts
        assert result == number_user

    def test_lookup_contato_inexistente(self, name_user, number_user, msg_absent_contact):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        absent_name = 'Gilbert'

        # Chamada
        result = contact_list.lookup(absent_name)

        # Asserts
        assert result == msg_absent_contact

    # TESTES PARA O MÉTODO GET_NAMES
    def test_get_names(self, name_user, number_user):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        result_names_list = ['POLICIA', name_user]

        # Chamada
        result = contact_list.get_names()

        # Asserts
        assert result == result_names_list

    def test_get_names_lista_vazia(self, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.clear()
        length_contact_list = 0

        # Chamada
        result = contact_list.get_names()

        # Assert
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == length_contact_list

    # TESTES PARA O MÉTODO GET_NUMBERS
    def test_get_numbers(self, name_user, number_user):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        result_numbers_list = ['190', number_user]

        # Chamada
        result = contact_list.get_numbers()

        # Asserts
        assert result == result_numbers_list

    def test_get_numbers_lista_vazia(self, name_user, number_user, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.clear()
        length_contact_list = 0

        # Chamada
        result = contact_list.get_numbers()

        # Asserts
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == length_contact_list

    # TESTES PARA O MÉTODO CLEAR
    def test_clear(self, name_user, number_user, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        length_contact_list = 0

        # Chamada
        result = contact_list.clear()

        # Asserts
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == length_contact_list

    # TESTES PARA O MÉTODO DE SEARCH
    def test_search_valido(self, name_user, number_user):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        result_search = [name_user, number_user]

        # Chamada
        result = contact_list.search(name_user)

        #Asserts
        assert result == result_search

    def test_search_contato_inexistente(self, name_user, number_user, msg_absent_contact):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)

        # Chamada
        result = contact_list.search('Nome')

        #Asserts
        assert result == msg_absent_contact

    # TESTES PARA ORDENAÇÃO DOS NÚMEROS DE TELEFONE
    def test_phonebook_sorted(self, name_user, number_user):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        result_numbers_list_sorted = ['190', number_user]

        # Chamada
        result = contact_list.get_phonebook_sorted()

        #Asserts
        assert result == result_numbers_list_sorted

    def test_phonebook_sorted_lista_vazia(self, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.clear()
        length_contact_list = 0

        # Chamada
        result = contact_list.get_phonebook_sorted()

        #Asserts
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == length_contact_list

    # TESTES PARA ORDENAÇÃO DECRESCENTE DOS NÚMEROS DE TELEFONE
    def test_phonebook_reverse(self, name_user, number_user):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        result_numbers_list_sorted = [number_user, '190']

        # Chamada
        result = contact_list.get_phonebook_reverse()

        #Asserts
        assert result == result_numbers_list_sorted

    def test_phonebook_reverse_lista_vazia(self, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.clear()
        length_contact_list = 0

        # Chamada
        result = contact_list.get_phonebook_reverse()

        #Asserts
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == length_contact_list

    # TESTES PARA EXCLUSÃO DE UM CONTATO
    def test_delete_contact(self, name_user, number_user, msg_delete_contact):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        length_contact_list = 1

        # Chamada
        result = contact_list.delete(name_user)

        # Asserts
        assert result == msg_delete_contact
        assert len(contact_list.entries) == length_contact_list

    def test_delete_contato_inexistente(self, name_user, number_user, msg_absent_contact):
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        length_contact_list = 2

        # Chamada
        result = contact_list.delete('Nome')

        # Assert
        assert result == msg_absent_contact
        assert len(contact_list.entries) == length_contact_list

    def test_delete_contact_lista_vazia(self, name_user, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.clear()
        length_contact_list = 0

        # Chamada
        result = contact_list.delete(name_user)

        #Asserts
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == length_contact_list

    # TESTES PARA MUDAR O NÚMERO DO CONTATO
    def test_change_number_valido(self, name_user, number_user, msg_change_number):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        new_number = '0987654321'

        # Chamada
        result = contact_list.change_number(name_user, new_number)

        # Assert
        assert result == msg_change_number
        assert contact_list.entries[name_user] == new_number

    def test_change_number_contato_inexistente(self, name_user, number_user, msg_absent_contact):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        new_number = '0987654321'

        # Chamada
        result = contact_list.change_number('Nome', new_number)

        # Assert
        assert result == msg_absent_contact
        assert contact_list.entries[name_user] == number_user
