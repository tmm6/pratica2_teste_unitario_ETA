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
    def name_user(self):
        return 'Violet Evergarden'

    @pytest.fixture
    def number_user(self):
        return '54654754'

    """
    Testes
    """
    # TESTES ADIÇÃO CONTATO
    # Teste para adição deu um contato válido
    def test_add_contato_valido(self, name_user, number_user, msg_add_name):
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

    def test_nome_invalido(self, number_user, msg_invalid_name):
        # Setup
        invalid_name_list = ['#alf', 'jk@h', 'df!hj', '$kh', '%kdsgh', '', None]
        length_contact_list = 1
        contact_list = Phonebook()
        result_list = []
        msg_list = [msg_invalid_name, msg_invalid_name, msg_invalid_name, msg_invalid_name, msg_invalid_name,
                    msg_invalid_name, msg_invalid_name]

        # Chamada
        for invalid_name in invalid_name_list:
            msg_result = contact_list.add(invalid_name, number_user)
            result_list.append(msg_result)

        # Asserts
        assert result_list == msg_list
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

    def test_numero_vazio(self, name_user, msg_invalid_number):
        # Setup
        invalid_number = ''
        length_contact_list = 1
        contact_list = Phonebook()

        # Chamada
        result = contact_list.add(name_user, invalid_number)

        # Asserts
        assert result == msg_invalid_number
        assert len(contact_list.entries) == length_contact_list

    def test_numero_none(self, name_user, msg_invalid_number):
        # Setup
        invalid_number = None
        length_contact_list = 1
        contact_list = Phonebook()

        # Chamada
        result = contact_list.add(name_user, invalid_number)

        # Asserts
        assert result == msg_invalid_number
        assert len(contact_list.entries) == length_contact_list

###################################
    # Teste para retornar o numero de telefone do usuario.
    def test_lookup_valido(self, name):
        # Setup
        numero_valido = '389457'

        # Chamada
        contatos = Phonebook()
        contatos.add(name, numero_valido)
        resultado = contatos.lookup(name)

        # Asserts
        assert resultado == numero_valido

    def test_get_names(self, name, number):
        # Setup
        contatos = Phonebook()
        contatos.add(name, number)
        resultado_esperado = ['POLICIA', 'Homem da meia noite']

        # Chamada
        resultado = contatos.get_names()

        # Asserts
        assert resultado == resultado_esperado

    def test_get_numbers_correto(self, nome_contato, numero_contato):
        # Setup
        contatos = Phonebook()
        contatos.add(nome_contato, numero_contato)
        resultado_esperado = ['190', '389457']

        # Chamada
        resultado = contatos.get_numbers()

        # Asserts
        assert resultado == resultado_esperado

    def test_clear_correto(self, nome_contato, numero_contato):
        # Setup
        mensagem_esperada = 'phonebook limpado'
        contatos = Phonebook()
        contatos.add(nome_contato, numero_contato)

        # Chamada
        resultado = contatos.clear()

        # Asserts
        assert resultado == mensagem_esperada
        assert contatos.entries == {}

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
