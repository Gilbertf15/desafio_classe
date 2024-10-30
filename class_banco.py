from abc import ABC, abstractclassmethod
from typing import Type
lista_conta = []
lista_cliente = []
lista_historico = []

class Cliente:
    def __init__(self, endereço:str,):
        self.endereco = endereço
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
            
class PessoaFisica(Cliente):
    def __init__(self, endereço, cpf:str, nome:str, data_nascimento:str):
        super().__init__(endereço)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    def retornar_cpf(self):
        return self.cpf
    
class Conta:
    def __init__(self, numero:int, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = '001'
        self.cliente = cliente
        self.historico = Historico

    def Saldo(self) -> float:
        return self.saldo
    
    def Nova_conta(self, cliente, numero:int):
        try:
            def __str__(self):
                return f'Conta criada {cliente}: numero conta {numero}'
        except:
            return "Dados invalidos"
        
    def Sacar(self, valor:float) -> bool:
        try:
            if self.saldo > 0:
                saque = Saque(valor)
                saque.registrar(Conta.cliente)
                return True, self.saldo - valor
            else:
                print("Saldo insuficiente")
        except:
            print("saldo insuficiente")
            return False
        
    def Depositar(self, valor:float) -> bool:
        try:
            if valor > 0:
                self.saldo += valor
                depositar = Depositar(valor)
                depositar.registrar
                return True , f'valor depositado {valor}'

            else:
                print("valor incorreto para deposito")
        except:
            print("Valor invalido para deposito")
            return False
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente,):
        super().__init__( numero, cliente,)
        self.saldo = 0
        self.cliente = cliente
        self.agencia = "001"
        self.limite = 500
        self.limite_saque = 5

    def verificar(self, valor:int):
        if self.limite_saque > 5:
            print('nao pode mais sacar')
            return
        if self.limite > 500:
            print('valor muito alto para sacar')
            return
        elif self.limite_saque < 5 or self.limite < 500:
            ContaCorrente.Sacar()

class Transacao(ABC):
    @abstractclassmethod
    def registrar(self, conta:Conta):
        pass

class Saque(Transacao):
    def __init__(self, valor:float):
        self.valor = valor
    
    def registrar(self, conta:Conta):
        registro =  f"conta : {conta} operação : {self.__class__.__name__} valor {self.valor}"
        lista_historico.append(registro)
        return registro 
class Depositar(Transacao):
    def __int__(self, valor:float):
        self.valor = valor

    def registrar(self, conta:Conta):
        registro = f"conta : {conta} operação : {self.__class__.__name__} valor :{self.valor}"
        lista_historico.append(registro)
        return registro
    
class Historico:
    def adicionar_transacao(self, transacao:Type[Transacao]):
        try:
            
            if  transacao == Saque:
                print("*************EXTRATO*********")
                Saque.registrar()
                lista_historico_saque = f'{Saque.registrar()}  / '
                return lista_historico_saque
            
            elif transacao == Depositar:
                print("*************EXTRATO*********")
                Depositar.registrar()
                lista_historico = f'{Depositar.registrar()}  / '
                return lista_historico
        except:
            print("erro ao realizar registro de historico")


def main():
    while True:

        comandos = """
        [d] Depositar
        [sc] sacar conta corrente
        [sd] depositar conta corrente
        [s] Sacar
        [x] Extrato
        [q] Sair
        [u] criar usuario
        [c] para criar conta
        [z] visualizar contas
        
        [co] criar conta corrente
        => """
        print(comandos)
        entrada = input("Digite a operação que deseja")
        if entrada == 'u':
            endereco_ = ('digite endereço')
            cpf_cliente = input('digite cpf')
            nome_ = input('digite nome : ')
            data_nascimento_ = input('digite data de nascimento')
            PessoaFisica(endereco_, cpf_cliente, nome_, data_nascimento_ )
            lista_cliente.append(PessoaFisica)
            print('Cliente criado')

        elif entrada == 'c':
            numero = int(input('numero da conta :'))
            cliente = input('digite o cpf de um cliente existente')
            if cliente == PessoaFisica.retornar_cpf(lista_cliente):
                Conta(numero, cliente)
                print("conta criada")
               
        elif entrada == 'd':
            acesso_conta = int(input('digite numero da conta :'))
            for cliente_ in lista_cliente:
                if lista_cliente[cliente_].numero == acesso_conta: 
                    print('CONTA ENCONTRADA..')
                    deposito = float(input('digite valor para deposito'))
                    cliente_.Depositar(deposito)
                    print('deposito feito')
                else :
                    print("erro ao depositar")

        elif entrada == 's':
            acesso_conta_saque = int(input('digite numero da conta :'))
            for cliente_ in lista_cliente:
                if lista_cliente[cliente_].numero == acesso_conta_saque: 
                    print('CONTA ENCONTRADA..')
                    saque_ = float(input('digite valor para saque'))
                    cliente_.sacar(saque_)
                    print('saque feito')
                else :
                    print("erro ao sacar")

        elif entrada == 'x':
            Historico.adicionar_transacao()

        elif entrada == 'co':
            numero_conta_corrente = int(input('Digite numero da conta :'))
            nome_cliente = input("Digite seu nome :")
            for cliente_ in lista_cliente:
                if lista_cliente[cliente_].numero == numero_conta_corrente: 
                    print('conta ja existente tente outro acesso..')
                    return
                
                else:   
                    print("Conta corrente criada")
                    Conta_corrente = ContaCorrente(numero_conta_corrente, nome_cliente)
                    lista_cliente.append(Conta_corrente)
        elif entrada == 'z':
            print(lista_conta)
        elif entrada == 'q':
            print("saindo do sistema...")
            break
main()