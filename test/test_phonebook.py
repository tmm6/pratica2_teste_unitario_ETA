from unittest import TestCase

import pytest

from src.phonebook import Phonebook


class TestPhonebook(TestCase):
    # Utilizar o fixture para reaproveitar codigo
    @pytest.fixture
    def msg_contato_add(self):
        return 'Numero adicionado'

    @pytest.fixture
    def nome_contato(self):
        return 'Homem da meia noite'

    @pytest.fixture
    def numero_contato(self):
        return '389457'

    # Teste para adicao deu um contato valido
    def test_add_contato_valido(self, nome_contato, msg_contato_add):
        # Setup
        numero_valido = '389457'

        # Chamada
        contatos = Phonebook()
        resultado = contatos.add(nome_contato, numero_valido)

        # Asserts
        assert resultado == msg_contato_add
        assert contatos.entries[nome_contato] == numero_valido

    # Teste para retornar o numero de telefone do usuario.
    def test_lookup_valido(self, nome_contato):
        # Setup
        numero_valido = '389457'

        # Chamada
        contatos = Phonebook()
        contatos.add(nome_contato, numero_valido)
        resultado = contatos.lookup(nome_contato)

        # Asserts
        assert resultado == numero_valido

    def test_get_names(self, nome_contato, numero_contato):
        # Setup
        contatos = Phonebook()
        contatos.add(nome_contato, numero_contato)
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
