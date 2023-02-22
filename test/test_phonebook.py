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
        result_list_name = ['POLICIA', name_user]

        # Chamada
        result = contact_list.get_names()

        # Asserts
        assert result == result_list_name

    def test_get_names_lista_vazia(self, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.clear()
        lenght_contact_list = 0

        # Chamada
        result = contact_list.get_names()

        # Assert
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == lenght_contact_list

    # TESTES PARA O MÉTODO GET_NUMBERS
    def test_get_numbers(self, name_user, number_user):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        result_list_number = ['190', number_user]

        # Chamada
        result = contact_list.get_numbers()

        # Asserts
        assert result == result_list_number

    def test_get_numbers_lista_vazia(self, name_user, number_user, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.clear()
        lenght_contact_list = 0

        # Chamada
        result = contact_list.get_numbers()

        # Asserts
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == lenght_contact_list

    # TESTES PARA O MÉTODO CLEAR
    def test_clear(self, name_user, number_user, msg_phonebook_empty):
        # Setup
        contact_list = Phonebook()
        contact_list.add(name_user, number_user)
        lenght_contact_list = 0

        # Chamada
        result = contact_list.clear()

        # Asserts
        assert result == msg_phonebook_empty
        assert len(contact_list.entries) == lenght_contact_list


###################################

    def test_search_valido(self, nome_contato, numero_contato):
        # Setup
        contatos = Phonebook()
        contatos.add(nome_contato, nome_contato)

        # Chamada
        resultado = contatos.search(nome_contato)

        #Asserts
        assert resultado == [{nome_contato, numero_contato}]

    def test_sorted_crescente(self):
        # Setup
        nome_valido = 'Homem da meia noite'
        numero_valido = '389457'
        nome_valido2 = 'Zomem da meia noite'
        numero_valido2 = '0'
        lista_ordenada = ['0', '190', '389457']

        # Chamada
        contatos = Phonebook()
        contatos.add(nome_valido, numero_valido)
        contatos.add(nome_valido2, numero_valido2)

        resultado = contatos.get_phonebook_sorted()

        #Asserts
        self.assertEqual(resultado, lista_ordenada)

    def test_sorted_decrescente(self):
        # Setup
        nome_valido = 'Homem da meia noite'
        numero_valido = '389457'
        nome_valido2 = 'Zomem da meia noite'
        numero_valido2 = '0'
        lista_ordenada = ['389457', '190', '0']
        contatos = Phonebook()
        contatos.add(nome_valido, numero_valido)
        contatos.add(nome_valido2, numero_valido2)

        # Chamada
        resultado = contatos.get_phonebook_reverse()

        #Asserts
        assert resultado == lista_ordenada
        # self.assertEqual(resultado, lista_ordenada)