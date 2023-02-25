import pytest

from src.phonebook import Phonebook


class TestPhonebook:
    """
    Utilização do fixture.
    """

    # Before
    @pytest.fixture(autouse=True)
    def contact_obj(self):
        return Phonebook()

    @pytest.fixture
    def name_user(self):
        return 'Violet Evergarden'

    @pytest.fixture
    def number_user(self):
        return '54654754'

    @pytest.fixture
    def msg_absent_contact(self):
        return 'Usuário não existe'

    @pytest.fixture
    def msg_phonebook_empty(self):
        return 'Agenda não possui contatos'

    """
    Testes
    """
    # TESTES VALIDAÇÃO DOS CAMPOS
    #
    @pytest.mark.parametrize('chars', ['', None]) # Utilização de parametrização.
    def test_is_none_or_empty_contato_vazio_none(self, contact_obj, chars):
        # Setup
        result_is_invalid = True

        # Chamada
        result = contact_obj.is_none_or_empty(chars)

        # Asserts
        assert result == result_is_invalid

    @pytest.mark.parametrize('chars', ['#', '@', '!', '$', '%'])# Utilização de parametrização.
    def test_validate_name_contato_invalido(self, contact_obj, name_user, chars):
        # Setup
        invalid_name = name_user + chars
        result_is_char = True

        # Chamada
        result = contact_obj.validate_name(invalid_name)

        # Asserts
        assert result == result_is_char

    def test_validate_name_contato_valido(self, contact_obj, name_user):
        # Setup
        invalid_name = name_user
        result_is_char = False

        # Chamada
        result = contact_obj.validate_name(invalid_name)

        # Asserts
        assert result == result_is_char

    def test_valid_number_numero_invalido(self, contact_obj):
        # Setup
        invalid_number = '1'
        result_is_invalid = True

        # Chamada
        result = contact_obj.valid_number(invalid_number)

        # Asserts
        assert result == result_is_invalid

    def test_valid_number_numero_valido(self, contact_obj, number_user):
        # Setup
        result_is_invalid = False

        # Chamada
        result = contact_obj.valid_number(number_user)

        # Asserts
        assert result == result_is_invalid


    # TESTES ADIÇÃO CONTATO
    # Teste para adição de um contato válido
    def test_add_contato(self, contact_obj, name_user, number_user):
        # Setup
        length_contact_list = 2
        msg_add_name = 'Número adicionado'

        # Chamada
        result = contact_obj.add(name_user, number_user)

        # Asserts
        assert result == msg_add_name
        assert contact_obj.entries[name_user] == number_user
        assert len(contact_obj.entries) == length_contact_list

    def test_add_contato_duplicado(self, contact_obj, name_user, number_user):
        # Setup
        length_contact_list = 2
        contact_obj.add(name_user, number_user)
        msg_name_duplicated = 'Usuário já existente'

        # Chamada
        result = contact_obj.add(name_user, number_user)

        # Asserts
        assert len(contact_obj.entries) == length_contact_list
        assert contact_obj.entries[name_user] == number_user

    # TESTES PARA O MÉTODO LOOKUP
    def test_lookup(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)

        # Chamada
        result = contact_obj.lookup(name_user)

        # Asserts
        assert result == number_user

    def test_lookup_contato_inexistente(self, contact_obj, name_user, number_user, msg_absent_contact):
        # Setup
        contact_obj.add(name_user, number_user)
        absent_name = 'Gilbert'

        # Chamada
        result = contact_obj.lookup(absent_name)

        # Asserts
        assert result == msg_absent_contact

    # TESTES PARA O MÉTODO GET_NAMES
    def test_get_names(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)
        result_names_list = ['POLICIA', name_user]

        # Chamada
        result = contact_obj.get_names()

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
    def test_get_numbers(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)
        result_numbers_list = ['190', number_user]

        # Chamada
        result = contact_obj.get_numbers()

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
    def test_clear(self, contact_obj, name_user, number_user, msg_phonebook_empty):
        # Setup
        contact_obj.add(name_user, number_user)
        length_contact_list = 0

        # Chamada
        result = contact_obj.clear()

        # Asserts
        assert result == msg_phonebook_empty
        assert len(contact_obj.entries) == length_contact_list

    # TESTES PARA O MÉTODO DE SEARCH
    def test_search_valido(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)
        result_search = [name_user, number_user]

        # Chamada
        result = contact_obj.search(name_user)

        #Asserts
        assert result == result_search

    def test_search_contato_inexistente(self, contact_obj, name_user, number_user, msg_absent_contact):
        # Setup
        contact_obj.add(name_user, number_user)

        # Chamada
        result = contact_obj.search('Nome')

        #Asserts
        assert result == msg_absent_contact

    # TESTES PARA ORDENAÇÃO DOS NÚMEROS DE TELEFONE
    def test_phonebook_sorted(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)
        result_numbers_list_sorted = ['190', number_user]

        # Chamada
        result = contact_obj.get_phonebook_sorted()

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
    def test_phonebook_reverse(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)
        result_numbers_list_sorted = [number_user, '190']

        # Chamada
        result = contact_obj.get_phonebook_reverse()

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
    def test_delete_contact(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)
        length_contact_list = 1
        contact_list = {'POLICIA': '190'}
        msg_delete_contact = 'Contato excluído'

        # Chamada
        result = contact_obj.delete(name_user)

        # Asserts
        assert result == msg_delete_contact
        assert len(contact_obj.entries) == length_contact_list
        assert contact_obj.entries == contact_list

    def test_delete_contato_inexistente(self, contact_obj, name_user, number_user, msg_absent_contact):
        # Setup
        contact_obj.add(name_user, number_user)
        length_contact_list = 2
        contact_list = {'POLICIA': '190', name_user: number_user}

        # Chamada
        result = contact_obj.delete('Nome')

        # Assert
        assert result == msg_absent_contact
        assert len(contact_obj.entries) == length_contact_list
        assert contact_obj.entries == contact_list

    # TESTES PARA MUDAR O NÚMERO DO CONTATO
    def test_change_number_valido(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)
        new_number = '0987654321'
        length_contact_list = 2
        msg_change_number = 'Contato atualizado'

        # Chamada
        result = contact_obj.change_number(name_user, new_number)

        # Assert
        assert result == msg_change_number
        assert contact_obj.entries[name_user] == new_number
        assert len(contact_obj.entries) == length_contact_list

    def test_change_number_contato_inexistente(self, contact_obj, name_user, number_user, msg_absent_contact):
        # Setup
        contact_obj.add(name_user, number_user)
        new_number = '0987654321'

        # Chamada
        result = contact_obj.change_number('Nome', new_number)

        # Assert
        assert result == msg_absent_contact
        assert contact_obj.entries[name_user] == number_user

    # TESTES PARA PESQUSAR CONTATO PELO NÚMERO
    def test_get_name_by_number_valido(self, contact_obj, name_user, number_user):
        # Setup
        contact_obj.add(name_user, number_user)

        # Chamada
        result = contact_obj.get_name_by_number(number_user)

        # Assert
        assert result == name_user

    def test_get_name_by_number_contato_inexistente(self, contact_obj, name_user, number_user, msg_absent_contact):
        # Setup
        contact_obj.add(name_user, number_user)
        absent_numer = '00002'

        # Chamada
        result = contact_obj.get_name_by_number(absent_numer)

        # Assert
        assert result == msg_absent_contact

