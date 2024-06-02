from enum import Enum

class MoedaEnum(Enum):
    BRL = 1.0, 'Real Brasileiro'
    USD = 5.25, 'Dólar'
    EUR = 5.70, 'Euro'
    GBP = 6.68, 'Libra Esterlina'
    CHF = 5.81, 'Franco Suíço'
    ARS = 0.0059, 'Peso Argentino'
    CAD = 3.84, 'Dólar Canadense'

    def __init__(self, valor, descricao):
        self._value_ = valor
        self.descricao = descricao

    @property
    def valor(self):
        return self._value_
    

def inflacaoReal():
    print("Ajustando inflação para Real...")

def inflacaoEUA():
    print("Ajustando inflação para EUA...")

def inflacaoEuro():
    print("Ajustando inflação para Euro...")

def inflacaoLibra():
    print("Ajustando inflação para Libra...")

def inflacaoFrancoSuico():
    print("Ajustando inflação para Franco Suíço...")

def inflacaoPesoArgentino():
    print("Ajustando inflação para Peso Argentino...")

def inflacaoDolarCanadense():
    print("Ajustando inflação para Dólar Canadense...")
                

def converterMoeda():
    import sys
    import re
    from functools import partial
    import re

    continuar = True
    
    def obter_moeda(mensagem):
        print(mensagem)
        for moeda in MoedaEnum:
            print(f'{moeda.name} - {moeda.descricao}')
        while True:
            opcao = input().upper()
            if opcao in MoedaEnum.__members__:
                return MoedaEnum[opcao]
            print('Moeda Inválida. Tente Novamente. ')
    
    def obter_valor():
        while True:
            try:
                return float(input('Digite aqui o valor a ser convertido: '))
            except ValueError:
                print('Valor Inválido. Tente Novamente. ')
    
    def realizar_conversao(op1, op2, valorintro):
        v1 = valorintro / op1.valor * op2.valor
        inflacao_map[op2.name]()
        print(f'De {op1.descricao} para {op2.descricao}: {v1:.2f} {op2.name}')

        inflacao_map = {
            'BRL': inflacaoReal,
            'USD': inflacaoEUA,
            'EUR': inflacaoEuro,
            'GBP': inflacaoLibra,
            'CHF': inflacaoFrancoSuico,
            'ARS': inflacaoPesoArgentino,
            'CAD': inflacaoDolarCanadense
        }
        


    while continuar:
            print("Bem vindo ao conversor de moedas! \nPara continuar selecione uma das opções abaixo:\n"
                "1 - Converter\n"
                "2 - Sair do programa")
            escolha = input()

            if escolha == '2':
                print("Finalizando...")
                continuar = False
            elif escolha == '1':
                opcao1 = obter_moeda("Selecione a moeda a ser convertida:")
                opcao2 = obter_moeda("Para:")
                valorintro = obter_valor()
                realizar_conversao(opcao1, opcao2, valorintro)
            else:
                print("Opção inválida. Tente novamente.")

converterMoeda()

        


    
    
    
