from cliente import Cliente
from cadastro_clientes import CadastroCliente

def test_cadastro_cliente_sucesso():
    cliente =  Cliente('Will', 20, 'Will@teste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro realizado com sucesso!"

def test_cadastro_cliente_com_nome_menor_que_3_caracteres():
    cliente =  Cliente('Wi', 20, 'Will@teste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro não realizado! nome incorreto"

def test_cadastro_cliente_com_menos_de_18_anos():
    cliente =  Cliente('Will', 12, 'Will@teste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Erro ao cadastrar! menor de idade"

def test_cadastro_cliente_email():
    cliente = Cliente('Will', 18, 'Willteste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Erro ao cadastrar! Email invalido"