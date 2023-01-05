"""
Created on Tue Dec 27 12:06:02 2022

@author: Cleopatra
"""
import datetime
import time
import os
import random

class Movimentos:
    def __init__(self):
        self.data_movimento = datetime.datetime.today().date()
        self.tipo_movimento = []
        
    def imprime(self):
        print("Movimentos: ")
        for m in self.tipo_movimento:
            print("->",m)

if __name__ == '__main__':
    cliente = '';
    cl = []
    cont = []
    escolha = '-1'
    mov = []
    
    def movimentos(ct, tp):
        data_movimento = datetime.datetime.today().date()
        tp_movimento = [ct, tp, data_movimento]
        if os.path.exists('Movimentos.txt'):
            arquivoMovimentos = open('Movimentos.txt','a')
        else:
            arquivoMovimentos = open('Contas.txt','w')
        arquivoMovimentos.write('{}\n'.format(ct))
        arquivoMovimentos.write('{}\n'.format(tp))
        arquivoMovimentos.write('{}\n'.format(data_movimento))
        # arquivoMovimentos.write('{}\n'.format(limite))
        # arquivoMovimentos.write('{}\n'.format(tipoConta))
        arquivoMovimentos.close()
        mov.append(tp_movimento)
    
    def criar_conta(numero, titular, saldo, limite, tipoConta):
        histo_trans = []
        conta = [numero, titular, saldo, limite, tipoConta, histo_trans, datetime.datetime.today().date().isoformat()]
        if os.path.exists('Contas.txt'):
            arquivoConta = open('Contas.txt','a')
        else:
            arquivoConta = open('Contas.txt','w')
        arquivoConta.write('{}\n'.format(numero))
        arquivoConta.write('{}\n'.format(titular))
        arquivoConta.write('{}\n'.format(saldo))
        arquivoConta.write('{}\n'.format(limite))
        arquivoConta.write('{}\n'.format(tipoConta))
        arquivoConta.close()
        return conta
    
    def alterar_conta(numero_conta):
        vv = 0
        for c in cont:
            if (int(c[0]) == numero_conta):
                vv = 1
                print('1 << Alterar Tipo')
                print('2 << Alterar Titular')
                print('3 << Alterar Saldo')
                alt = int(input('>> '))
                if (alt == 1):
                    tp = input('Tipo de conta: ')
                    c[4] = tp
                if (alt == 2):
                    tit = input('Titular: ')
                    c[1] = tit
                if (alt == 3):
                    sld = int(input('Saldo: '))
                    c[2] = sld
        if (vv == 0):
            print('Não foi encongtrada nenhuma conta com este numero.')
            
    def eliminar_conta(numero):
        vv = 0
        for c in cont:
            if (c[0] == numero):
                vv = 1
                conf = input('Tem certeza que quer eliminar a conta?[S/N]: ')
                if (conf.upper() == 'S'):
                    c.clear()
                    print('\nConta Eliminada!\n')
        if (vv == 0):
            print('Não foi encongtrada nenhuma conta com este numero.')
    
    def cad_clientes(nome, sobrenome, bi):
        nome = nome
        sobrenome = sobrenome
        bi = bi
        id_titular = random.randrange(41) + 5
        if os.path.exists('titulares.txt'):
            arquivoTitular = open('titulares.txt','a')
        else:
            arquivoTitular = open('titulares.txt','w')
        arquivoTitular.write('{}\n{}\n{}\n{}\n'.format(id_titular, nome, sobrenome, bi))
        arquivoTitular.close()
        clt = [id_titular, nome, sobrenome, bi]
        return clt
    
    def lista_titulares():
        print('\n\n -- TITULARES --- \n\nID\t NOME\t\t SOBRENOME\t\t BI')
        for lst in cl:
            print('{}\t {}\t\t {}\t\t {}'.format(lst[0], lst[1], lst[2], lst[3]))
    
    def depositar(conta, valor):
        for c in cont:
            if (int(c[0]) == conta):
                c[2] = int(c[2]) + valor
                dc = {"Tipo":"Deposito", "Valor":valor, "Categoria":"-", "Data":datetime.datetime.today().date().isoformat()}
                c[5].append(dc)
    
    historico_trans = []
    def levantamento(conta, valor, categoria):
        for c in cont:
            if (int(c[0]) == conta):
                if (int(c[2]) < valor):
                    return False
                else:
                   if (categoria == "Transferencia"):
                       categoria = "-" 
                   c[2] = int(c[2]) - valor
                   dc = {"Tipo":"Levantamento", "Valor":valor, "Categoria":categoria, "Data":datetime.datetime.today().date().isoformat()}
                   c[5].append(dc)
                   if (c[2] < 0):
                       print("O saldo da conta {} esta negativo: {} AOA".format(conta, c[2]))
                   return True
        return False
        
    def extrato(conta_num):
        for c in cont:
            if (int(c[0]) == conta_num):
                print("Número: {}\nSaldo Dispnivel: {} AOA".format(conta_num, c[2]))
                dc = {"Tipo":"Extrato", "Categoria":"-", "Data":datetime.datetime.today().date().isoformat()}
                c[5].append(dc)
                movimentos(conta_num, "Tirou extrato")
        
    def transfer_para(conta, destino, valor):
        
        for c in cont:
            if (int(c[0]) == conta):
                retirou = levantamento(conta, valor, "Transferencia")
                if (retirou == False):
                    return False
                else:
                    for d in cont:
                        if (int(d[0]) == destino):
                            dest = d
                    depositar(destino, valor)
                    dc = {"Tipo":"Transferencia", "Valor":valor, "Categoria":"-", "Destino":dest[0], "Data":datetime.datetime.today().date().isoformat()}
                    c[5].append(dc)
                    movimentos(conta,"transferencia de {} para conta {}\n".format(valor, dest[0]))
                    return True
        
    def categoria_gasto(cat):
        categoria = ""
        if (cat == 0):
            categoria = "Casa"
        elif (cat == 1):
            categoria = "Seguros"
        elif (cat == 2):
            categoria = "Medicina"
        elif (cat == 3):
            categoria = "Salario"
        elif (cat == 4):
            categoria = "Telefone"
        elif (cat == 5):
            categoria = "Prendas"
        elif (cat == 6):
            categoria = "Alimentacao"
        else:
            categoria = "Outro"
            
        return categoria
            
    def imprime_historico(conta):
        for c in cont:
            print("data abertura: {}".format(c[6]))
            print("Tipo Conta: {}".format(c[4]))
            print("Número deConta: {}".format(c[0]))
            print("Movimentos: ")
            for t in c[5]:
                print("-", t)

    # def menu():
    while escolha != '-2':
        print("0 - INSERIR TITULAR {}".format(datetime.datetime.today().date()))
        print("1 - INSERIR CONTA")
        print("2 - ALTERAR CONTA")
        print("3 - ELIMINAR CONTA/MOVIMENTOS")
        print("4 - TRANSFERÊNCIA")
        print("5 - CONSULTAR SALDO")
        print("6 - CONSULTAR MOVIMENTOS ENTRE DATAS")
        print("7 - CONSULTAR MOVIMENTOS POR CATEGORIA")
        print("8 - LISTAR CONTAS")
        print("-2 - FECHAR PROGRAMA")
        print()
        escolha = input("OPÇÃO: ")
        
    # menu()
        if (escolha == '0'):
            nome = input("Primeiro Nome: ")
            sobrenome = input("Sobrenome: ")
            bi = input("BI: ")
            cliente = cad_clientes(nome, sobrenome, bi)
            cl.append(cliente)
            
            print('\t\t\t *** TITULAR CADASTRADO COM SUCESSO ***\n')
            
        elif (escolha == '1'):
            if (cliente == ''):
                print('Deverá cadastrar um titular antes.')
            else:
                lista_titulares()
                titular = int(input('Titular: '))
                numero = input('Número da Conta: ')
                tipo = input('Tipo de Conta: ')
                banco = input('Banco: ')
                saldo_abertura = input('Saldo: ')
                limite = 1000
                conta = criar_conta(numero, titular, saldo_abertura, limite, tipo)
                cont.append(conta)
                print('\t\t\t *** CONTA CRIADA COM SUCESSO ***')
                print('\t\t\t-------------- DADOS -------------')
                print('NUMERO\t\t TITULAR\t\t TIPO\t\t SALDO')
                for contass in cont:
                    for tt in cl:
                        if (int(tt[0]) == titular):
                            print('{}\t\t {}\t\t {}\t\t {}'.format(contass[0], tt[1], contass[4], contass[2]))
        elif (escolha == '2'):
            print('\tALTERAÇÃO DE DADOS DE CONTA\n')
            numC = int(input('Conta> '))
            alterar_conta(numC)
            
        elif (escolha == 3):
            print('\n\tELIMINAR CONTA\n')
            numero = input('Numero Conta> ')
            eliminar_conta(numero)
            
        elif (escolha == '4'):
            n = 0
            while n == 0:
                vf = 0
                conta_retirar = int(input("\tInsira o numero conta para retirar\n -> "))
                i = 0
                for i in cont:
                    if (int(i[0]) == conta_retirar):
                        nn = 0
                        vf = 0
                        while nn == 0:
                            vff = 1
                            ii = 0
                            conta_destino = int(input("\tinsira o numero conta destino\n -> "))
                            valor_transfere = int(input("\tinsira o valor de transferencia\n -> "))
                            
                            for ii in cont:
                                if (int(ii[0]) == conta_destino):
                                    transfer_para(conta_retirar, conta_destino, int(valor_transfere))
                                    print("Transferência feita com sucesso!")
                                    print("\n\t\t\t\t ======= HISTÓRICO =======")
                                    imprime_historico(conta_retirar)
                                    n = 1
                                    nn = 1
                                    vff = 0
                                    break
                            if (vff == 1):
                                resp = input("A conta de destino nao existe. Tentar novamente?[Y/N]: ")
                                if (resp == "Y" or resp == "y"):
                                    nn = 0
                                else:
                                    nn = 1
                    else:
                        vf = 1
                if (vf == 1):
                    resp = input("A conta não existe. Tentar novamente?[Y/N]: ")
                    if (resp == "Y" or resp == "y"):
                        n = 0
                    else:
                        n = 1
                    
        elif (escolha == '5'):
            i = 0
            while i == 0:
                conta = int(input("\tInsira o numero da conta\n -> "))
                ii = 0
                vf = 0
                for ii in cont:
                    if (int(ii[0]) == conta):
                        extrato(conta)
                        vf = 1
                        i = 1
                        break
                if (vf != 1):
                    print("\tConta nao encontrada. Tente novamente.")
                    
        
        elif (escolha == '6'):
            dtini = input("primeira data: ")
            dtfim = input("segunda data: ")
            
            dti = time.strptime(dtini,"%Y-%m-%d")
            dtf = time.strptime(dtfim, "%Y-%m-%d")
            
            print("\t============ MOVIMENTOS ENTRE {} E {} =============".format(dtini, dtfim))
            for i in cont:
                vf = 0
                for ii in i[5]:
                    dtcont = time.strptime(ii['Data'], "%Y-%m-%d")
                    if (dtcont >= dti and dtcont <= dtf):
                        print("\t{}".format(ii))
                        vf += 1
                
            if (vf == 0):
                print("\tNao existe nenhum movimento neste intervalo de datas.")
                    
        elif (escolha == '7'):
            print("\t============ MOVIMENTOS POR CATEGORIA =============")
            print("0 -- Casa")
            print("1 -- Seguros")
            print("2 -- Medicina")
            print("3 -- Salario")
            print("4 -- Telefone")
            print("5 -- Prendas")
            print("6 -- Alimentacao")
            print("7 -- Outro")
            
            cat = int(input("Categoria: "))
            for i in cont:
                ii = 0
                vf = 0
                for ii in i[5]:
                    if (ii['Categoria'] == categoria_gasto(cat)):
                        print(ii)
                        vf += 1
                
            if (vf == 0):
                print("\tNao existe nenhum movimento nesta categoria.")
                
        elif (escolha == '8'):
            print("\t\t\t\t ======= LISTA DE CONTAS =======")
            i = 0
            if (len(cont) > 0):
                print("+----------+--------------------+-------------------+-----------------+")
                print("+    ID    +\t    TITULAR1\t\t+\tTIPO DE CONTA\t+\tSALDO\t\t  +")
                print("+----------+--------------------+-------------------+-----------------+")
                for i in cont:
                    print("+\t{}\t   +\t  {}    \t\t+\t\t{}\t\t+\t\t{}\t  +".format(i[0],i[1], i[4], i[2]))
                    print("+----------+--------------------+-------------------+-----------------+")
            else:
                print("\t\tNao existe nenhuma conta")
                
        elif (escolha == '-2'):
            print("\t\t\t++++ OBRIGADO POR USAR OS NOSSOS SERVIÇOS ++++")
        else:
            print("Opção não existe. Tente novamente")
        print()