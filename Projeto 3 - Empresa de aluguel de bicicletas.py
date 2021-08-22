class Cliente(object):
    def __init__(self, nome, cpf, carteira):
        self.nome = nome
        self.cpf = cpf
        self.carteira = carteira
        self.conta = 0

    def locacaoHora(self, valor = 5.0, quantidade):
        self.custohora = valor * quantidade
        
    def locacaoDia(self, valor = 25.0, quantidade):
        self.custodia = valor * quantidade
        
    def locacaoSemana(self, valor = 100.0, quantidade):
        self.custosemana = valor * quantidade
        
    def locacaoFamilia(self, bikes, dias):
        self.custohora = (valor * quantidade) * 0.7
        self.custodia = (valor * quantidade) * 0.7
        self.custosemana = (valor * quantidade) * 0.7
            
    # verifica o estoque disponível de bicicletas
    def ver_Estoque(self, estoque, objectLoja):
        self.estoque = estoque
        print(f'A Loja {objectLoja} tem em estoque {self.estoque}')
    

    # calcula o valor da locação horária
    def locacaoHora(self, valor, quantidade):
        self.custohorario *= valor * quantidade

    def pagaConta(self, valorPagto, objectLoja):
        try:
            if valorPagto <= 0:
                raise ValueError('Valor não pode ser zero ou negativo')

            if valorPagto > self.carteira:
                raise ArithmeticError(
                    'Pagamento maior que o dinheiro disponível')

            if not isinstance(objectLoja, Loja):
                raise SystemError(
                    'Não recebeu uma loja')

            self.carteira -= valorPagto
            aPagar = objectLoja.receberPagto(self.conta, valorPagto)
            
            print(
                f'Cliente {self.nome} - Pagamento de R${valorPagto} da conta de R${self.conta} feito. Conta R${self.conta}. Carteira: R${self.carteira}')
            
            if aPagar == 0:
                self.conta = 0
            elif aPagar > 0:
                self.conta = aPagar
            else:
                self.carteira -= aPagar
                self.conta = 0

            return self.carteira

        except ValueError:
            print('O valor para pagamento não pode ser menor ou igual a zero')

        except ArithmeticError:
            print('Você não tem saldo para pagar pelo serviço')

        except SystemError:
            print('Erro de sistema. Não atribuiu uma loja')

def alugaBike(self, estoqueBikes, loja):
    self.carteira += loja.receberPedido(estoqueBikes)

    print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike feito. A pagar: {self.conta}. Carteira: R${self.carteira} ')
    return self.carteira

    except ValueError:
        print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike não efetuado devido a quantidade inválida. A pagar: R${self.conta}. Carteira R${self.carteira}')
        return -1

    except SystemError:
        print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike não efetuado devido a loja inválida. A pagar: R${self.conta}. Carteira: R${self.carteira}')
        return -1

    except:
        print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike não efetuado. A pagar: R${self.conta}. Carteira: R${self.carteira}')
        return -1

import calendar
import re
from datetime import datetime

def validaData(m):
    if (re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', m)):
        m = datetime.strptime(m, "%d/%m/%Y")
        d = datetime.strptime(dataHoje(), "%d/%m/%Y")
        if m > d:
            return True
        else:
            return False
    else:
        return False

def diferenca_Dias(data):
    data2 = datetime.now().date()
    data = datetime.strptime(data, "%d/%m/%Y").date()
    dif = data - data2
    dif = dif.days
    return int(dif)

def diferenca_Dias2(data):
    data2 = datetime.now().date()
    data = datetime.strptime(data, "%d/%m/%Y").date()
    dif = data2 - data
    dif = dif.days
    return int(dif)

def dataHoje():
    now = datetime.now()
    return ("%s/%s/%s" % (now.day, now.month, now.year))

def mostraCalendario():
    now = datetime.now()
    cal = calendar.month(now.year, now.month)
    print("Aqui está o calendário:")
    print(cal)

import re
import time

# Validando

def validaCpf(cpf):
    while cpfExistente(cpf) is True:
        cpf = input("CPF já utilizado!\nDigite outro:")
    if len(cpf) != 11:
        return False
    else:
        if not re.match("[0-9]", cpf):
            return False
        cpf = list(cpf)
        for a in range(len(cpf)):
            cpf[a] = int(cpf[a])
        mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        mult2 = [11] + mult
        soma = 0
        soma2 = 0
        for a in range(len(mult)):
            soma += cpf[a] * mult[a]
        d1 = 11 - (soma % 11)
        if d1 == 10 or d1 == 11:
            d1 = 0
        cpf.append(d1)
        for a in range(len(mult2)):
            soma2 += cpf[a] * mult2[a]
        d2 = 11 - (soma2 % 11)
        if d2 == 10 or d2 == 11:
            d2 = 0
        cpf.append(d2)
        return bool(d1 == cpf[9] and d2 == cpf[10])


def valOthers(variavel, qtd_letras):
    return bool(re.match("[0-9]{" + str(qtd_letras) + "}", variavel))


def validaEndereco(m):
    while bool(re.match('[A-Za-z0-9ãõẽíóáç .,º' ']{5,25}', m)) is False:
        m = input('Endereço Inválido!\nDigite um novo endereço, no formato (Rua, Número, Cidade-Estado): ')


def validaTelefone(m):
    while bool(re.match('^\([1-9]{2}\)[2-9]{2,3}[0-9]{2}\-[0-9]{4}$', m)) is False:
        m = input('Número errado!\nDigite outro número: ')


def validaNome(m, n):
    while bool(re.match('[^0-9][a-zA-Zãõçóúáéí ]{2,}', m)) is False:
        m = input(n + ' Inválido!\nDigite outro ' + n + ': ')


def validaData(m):
    try:
        date = time.strptime(m, '%d/%m/%Y')
        return bool(date.tm_year <= (int(time.strftime("%Y")) - 18))
    except:
        return False


def melhoresClientes():
    melhoresCli = {}
    for i in dataUser:
        if dataUser[i][10] != 0:
            melhoresCli[len(melhoresCli)] = dataUser[i][0], dataUser[i][10]
    melhoresCli = sorted(melhoresCli.values(), reverse=True)[:]

    print("///Nome do cliente/Quantidade de alugueis:")
    for i in melhoresCli:
        print("\t", i[0], " | ", i[1])

print('______________________________________')
print('         Projeto 3 Lets Code          ')
print('        DATA ESKIN RENT A BIKE        ')
print('--------------------------------------')
print(' Created by Daniel, Maurício e Luiz   ')
print('______________________________________')

