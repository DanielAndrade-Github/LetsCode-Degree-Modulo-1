import calendar
import re
from datetime import datetime

# Criação da Classe/Objeto "LOJA":
class Loja(object):
    def __init__(self, estoque = 0):
        """
        Construtor da classe, instancia a Loja de Bicicletas.
        """
        self.estoque = estoque

    # Métodos:
    
    ## Mostrar o estoque de bicicletas:
    def mostrarEstoque(self):
        """
        Mostra o estoque de bicicletas disponíveis para locação.
        """
        print(f"No momento, temos {self.estoque} bicicletas disponíveis para locação.")
        return self.estoque
    
    
    ## Receber pedidos de aluguéis por hora, diários ou semanais validando
    ## a possibilidade com o estoque: 
    
    ### Locação por hora:
    def locacaoHora(self, qtBikes):
        """
        Locação de bicicleta(s) por hora ao Cliente.
        """
        ### Caso seja informado um número negativo de bicicletas:
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        ### Verificação de bicicletas solicitadas versus estoque atual:
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos \
                apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        ### Havendo estoque, exibe as informações da locação para o Cliente na tela e
        ### retorna a hora atual para posterior cálculo do valor a ser pago:
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às \
                {horaLocacao} de hoje.\n O valor para locação por hora é de R$ 5,00 \
                por hora, por bicicleta.\nAgradecemos a preferência e volte sempre!")
            self.estoque -= qtBikes
            return horaLocacao
    
    ### Locação por dia:
    def locacaoDia(self, qtBikes):
        """
        Locação de bicicleta(s) por dia ao Cliente.
        """
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos \
                apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às \
                {horaLocacao} de hoje.\n O valor para locação diária é de R$ 25,00 \
                por dia, por bicicleta.\nAgradecemos a preferência e volte sempre!")
            self.estoque -= qtBikes
            return horaLocacao
    
    ### Locação por semana:
    def locacaoSemanal(self, qtBikes):
        """
        Locação de bicicleta(s) por semana ao Cliente.
        """
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos \
                apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às \
                {horaLocacao} de hoje.\n O valor para locação semanal é de R$ 100,00 \
                por semana, por bicicleta.\nAgradecemos a preferência e volte sempre!")
            self.estoque -= qtBikes
            return horaLocacao
    
    ### Locação familiar:
    def locacaoFamilia(self, qtBikes):
        """
        Locação de bicicleta(s) sob a Promoção Família ao Cliente. Aplica um desconto de
        30% ao valor total da locação para 3 a 5 empréstimos de qualquer tipo.
        """
        ### Verifica se é possível aplicar a Promoção Família:
        if not(3 <= qtBikes <= 5):
            print(f"Desconto da 'Promoção Família' não aplicável.")
            return False
        ### Caso positivo, informa a aplicação do desconto e retorna um booleano para
        ### verificação posterior no momento do pagamento:
        else:
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} e receberá o desconto da \
                'Promoção Família'!\nVocê terá 30% (trinta por cento) de desconto sobre \
                o valor total final da locação.\nAproveite!")
            return True    
    
    ## Calcular a conta quando o cliente decide devolver a bicicleta:
    def calcularConta(self, alugaBike, locacaoFamilia):
        """
        Método para calcular a conta a ser paga pelo cliente e atualizar o estoque. Deverá
        ser alimentada a partir de argumentos do método 'alugaBike' do objeto Cliente.
        Deverá retornar o valor da conta.
        """
        horaLocacao, tipoLocacao, qtBikes = alugaBike
        conta = 0

        ### Caso esteja tudo de acordo com os valores recebidos do método alugaBike:
        if horaLocacao and tipoLocacao and qtBikes:
            self.estoque += qtBikes
            horaAtual = datetime.datetime.now()
            tempoLocacao = horaAtual - horaLocacao
            ### Locação por hora:
            if tipoLocacao == 1:
                conta = round(tempoLocacao.seconds / 3600) * 5 * qtBikes
            ### Locação por dia:
            elif tipoLocacao == 2:
                conta = round(tempoLocacao.days) * 25 * qtBikes
            ### Locação por semana:
            else: # tipoLocacao == 3:
                conta = round(tempoLocacao.days / 7) * 100 * qtBikes
            ### Verificação do desconto família:
            if locacaoFamilia == True:
                conta = conta * (0.7)
            ### Imprime uma mensagem de agradecimento ao Cliente e retorna o valor total
            ### devido (conta):
            print(f"Obrigado por devolver a(s) bicicleta(s)! \n \
                O valor total da sua locação é de: R$ {conta}.")
            return conta
       ### Caso haja algum problema com os valores recebidos do método alugaBike:
        else:
            print("Locação não encontrada no sistema.")
            return None

class Cliente(object):

    def __init__(self, qtBikes, tipoLocacao, horaLocacao, conta):
        self.qtBikes = 0
        self.tipoLocacao = 0
        self.horaLocacao = 0
        self.conta = 0
    
    def alugaBike(self, qtBikes, tipoLocacao):
        qtBikes = input("Quantas bicicletas gostaria de alugar?")
        tipoLocacao = input("Qual o tipo de locação que deseja?\n (Digite o número)\n \
            1 - Locação por hora (R$ 5,00/hora); \n \
            2 - Locação por dia (R$ 25,00/dia); \n \
            3 - Locação por semana (R$ 100,00/semana).")

        try:
            qtBikes = int(qtBikes)
        except ValueError:
            print("Num. deve ser um inteiro positivo!")
            return -1

        if qtBikes < 1:
            print("Entrada inválida. Qtbikes deve ser > zero!")
            return -1
        else:
            self.qtBikes = qtBikes
        
        try:
            tipoLocacao = int(tipoLocacao)
        except ValueError:
            print("Num. deve ser um int positivo!")
            return -1
        
        try:
            tipoLocacao in [1, 2, 3]
        except ValueError:
            print("Escolher 1, 2 ou 3.")
        
        if tipoLocacao == 1:
            return self.horaLocacao == 

        
        elif tipoLocacao == 2:

        else: # tipoLocacao == 3:


        

        return self.qtBikes, self.tipoLocacao, self.horaLocacao


        
    




# class Cliente(object):
#     def __init__(self, nome, cpf, carteira):
#         self.nome = nome
#         self.cpf = cpf
#         self.carteira = carteira
#         self.conta = 0

#     # verifica o estoque disponível de bicicletas
#     def ver_Estoque(self, estoque, objectLoja):
#         self.estoque = estoque
#         print(f'A Loja {objectLoja} tem em estoque {self.estoque}')
    

#     # calcula o valor da locação horária
#     def locacaoHora(self, valor, quantidade):
#         self.custohorario *= valor * quantidade

#     def pagaConta(self, valorPagto, objectLoja):
#         try:
#             if valorPagto <= 0:
#                 raise ValueError('Valor não pode ser zero ou negativo')

#             if valorPagto > self.carteira:
#                 raise ArithmeticError(
#                     'Pagamento maior que o dinheiro disponível')

#             if not isinstance(objectLoja, Loja):
#                 raise SystemError(
#                     'Não recebeu uma loja')

#             self.carteira -= valorPagto
#             aPagar = objectLoja.receberPagto(self.conta, valorPagto)
            
#             print(
#                 f'Cliente {self.nome} - Pagamento de R${valorPagto} da conta de R${self.conta} feito. Conta R${self.conta}. Carteira: R${self.carteira}')
            
#             if aPagar == 0:
#                 self.conta = 0
#             elif aPagar > 0:
#                 self.conta = aPagar
#             else:
#                 self.carteira -= aPagar
#                 self.conta = 0

#             return self.carteira

#         except ValueError:
#             print('O valor para pagamento não pode ser menor ou igual a zero')

#         except ArithmeticError:
#             print('Você não tem saldo para pagar pelo serviço')

#         except SystemError:
#             print('Erro de sistema. Não atribuiu uma loja')

# def alugaBike(self, estoqueBikes, loja):
#     self.carteira += loja.receberPedido(estoqueBikes)

#     print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike feito. A pagar: {self.conta}. Carteira: R${self.carteira} ')
#     return self.carteira

#     except ValueError:
#         print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike não efetuado devido a quantidade inválida. A pagar: R${self.conta}. Carteira R${self.carteira}')
#         return -1

#     except SystemError:
#         print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike não efetuado devido a loja inválida. A pagar: R${self.conta}. Carteira: R${self.carteira}')
#         return -1

#     except:
#         print(f'Cliente {self.nome} inscrito no CPF {self.cpf} - Pedido de {estoqueBikes} bike não efetuado. A pagar: R${self.conta}. Carteira: R${self.carteira}')
#         return -1

# def validaData(m):
#     if (re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', m)):
#         m = datetime.strptime(m, "%d/%m/%Y")
#         d = datetime.strptime(dataHoje(), "%d/%m/%Y")
#         if m > d:
#             return True
#         else:
#             return False
#     else:
#         return False

# def diferenca_Dias(data):
#     data2 = datetime.now().date()
#     data = datetime.strptime(data, "%d/%m/%Y").date()
#     dif = data - data2
#     dif = dif.days
#     return int(dif)

# def diferenca_Dias2(data):
#     data2 = datetime.now().date()
#     data = datetime.strptime(data, "%d/%m/%Y").date()
#     dif = data2 - data
#     dif = dif.days
#     return int(dif)

# def dataHoje():
#     now = datetime.now()
#     return ("%s/%s/%s" % (now.day, now.month, now.year))

# def mostraCalendario():
#     now = datetime.now()
#     cal = calendar.month(now.year, now.month)
#     print("Aqui está o calendário:")
#     print(cal)

# import re
# import time

# # Validando

# def validaCpf(cpf):
#     while cpfExistente(cpf) is True:
#         cpf = input("CPF já utilizado!\nDigite outro:")
#     if len(cpf) != 11:
#         return False
#     else:
#         if not re.match("[0-9]", cpf):
#             return False
#         cpf = list(cpf)
#         for a in range(len(cpf)):
#             cpf[a] = int(cpf[a])
#         mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
#         mult2 = [11] + mult
#         soma = 0
#         soma2 = 0
#         for a in range(len(mult)):
#             soma += cpf[a] * mult[a]
#         d1 = 11 - (soma % 11)
#         if d1 == 10 or d1 == 11:
#             d1 = 0
#         cpf.append(d1)
#         for a in range(len(mult2)):
#             soma2 += cpf[a] * mult2[a]
#         d2 = 11 - (soma2 % 11)
#         if d2 == 10 or d2 == 11:
#             d2 = 0
#         cpf.append(d2)
#         return bool(d1 == cpf[9] and d2 == cpf[10])


# def valOthers(variavel, qtd_letras):
#     return bool(re.match("[0-9]{" + str(qtd_letras) + "}", variavel))


# def validaEndereco(m):
#     while bool(re.match('[A-Za-z0-9ãõẽíóáç .,º' ']{5,25}', m)) is False:
#         m = input('Endereço Inválido!\nDigite um novo endereço, no formato (Rua, Número, Cidade-Estado): ')


# def validaTelefone(m):
#     while bool(re.match('^\([1-9]{2}\)[2-9]{2,3}[0-9]{2}\-[0-9]{4}$', m)) is False:
#         m = input('Número errado!\nDigite outro número: ')


# def validaNome(m, n):
#     while bool(re.match('[^0-9][a-zA-Zãõçóúáéí ]{2,}', m)) is False:
#         m = input(n + ' Inválido!\nDigite outro ' + n + ': ')


# def validaData(m):
#     try:
#         date = time.strptime(m, '%d/%m/%Y')
#         return bool(date.tm_year <= (int(time.strftime("%Y")) - 18))
#     except:
#         return False


# def melhoresClientes():
#     melhoresCli = {}
#     for i in dataUser:
#         if dataUser[i][10] != 0:
#             melhoresCli[len(melhoresCli)] = dataUser[i][0], dataUser[i][10]
#     melhoresCli = sorted(melhoresCli.values(), reverse=True)[:]

#     print("///Nome do cliente/Quantidade de alugueis:")
#     for i in melhoresCli:
#         print("\t", i[0], " | ", i[1])

# print('______________________________________')
# print('         Projeto 3 Lets Code          ')
# print('        DATA ESKIN RENT A BIKE        ')
# print('--------------------------------------')
# print(' Created by Daniel, Maurício e Luiz   ')
# print('______________________________________')

