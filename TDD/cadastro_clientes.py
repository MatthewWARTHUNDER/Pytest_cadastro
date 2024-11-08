IDADE_MINIMA = 18
CARACTER_OBRIGATORIO = '@'



class CadastroCliente():
    def __init__(self):
        self.cadastro = []
    
    def cadastrar_cliente(self, cliente):
        if cliente.idade <IDADE_MINIMA:
            return "Erro ao cadastrar! menor de idade"
        if not '@' in cliente.email:
            return "Erro ao cadastrar! Email invalido"
        if len(cliente.nome) <3:
            return "Cadastro não realizado! nome incorreto"
        self.cadastro.append(cliente)
        return "Cadastro realizado com sucesso!"