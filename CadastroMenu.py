from Cliente import Cliente
from Profissional import Profissional
from Pedido import Pedido
from Endereco import Endereco
from EsteticistaPreco import EsteticistaPreco
from ManicurePreco import ManicurePreco
from MaquiadoraPreco import MaquiadoraPreco
from MassagistaPreco import MassagistaPreco
from DesignerSobrancelha import DesignerSobrancelhaPreco
from Especialidades import especialidades
from CabeleiraPreco import CabelereiraPreco

print("--------Seja Bem vinda ao Aplicativo Dazzle-----")
print('\n '
      "Dazzle é um aplicativo de beleza, que atende a domicílio ")

print('\n'
      "1- Cadastrar Cliente")
print("2- Cadastrar Profissional")
print("3- Cadastrar Endereço Cliente")
print("4- Cadastrar Endereço Profissional")
print("5- Cadastrar Serviço")
print("6- Tabela de preços ")
print("7- Solicitar serviços")
print("8- Cancelar serviço ")
print("9- Especialidade ")
print("10- Marcar Horario")
print("11- Forma de pagamento")
print("12 - Avaliar")

c1 = Cliente('nome', 'cpf', 'email', 'genero')
p1 = Profissional('nome', 'cpf', 'email', 'genero', 'especialidade')
end1 = Endereco('rua', 'bairro', 'cidade', 'numero')
e1 = especialidades('nomeEspecialidade', 'preco')
M = ManicurePreco('ValorM')
Es = EsteticistaPreco('ValorE')
Cb = CabelereiraPreco('ValorC')
Mi = MaquiadoraPreco('ValorMi')
Ma = MassagistaPreco('ValorMa')
Ds = DesignerSobrancelhaPreco('ValorDs')
Pe = Pedido('horario', 'endereco', 'Tservico', 'Tpagamento')

opcao = int(input('\n'
                  "O que você deseja? "))
if opcao == 1:
  print('\n'
        '******CADASTRO CLIENTE*******')
  c1.cadastrarCliente()

if opcao == 2:
  print('\n'
        '******CADASTRO PROFISSIONAL*******')
  p1.Cadastrar_profissional()

if opcao == 3:
  print('\n--> Forneça seu endereço <--')
  end1.informar_Endereco()

if opcao == 4:
  print('\n --> Forneça seu endereço <--')
  end1.informar_Endereco()

if opcao == 5:
  print('\n ---------Cadastrar Serviço---------')
  p1.cadastrar_servico()

if opcao == 6:
  print('\n Preço da Manicure')
  M.FornecerPrecos()
  print('\n Preço da Esteticista')
  Es.FornecerPrecos()
  print('\n Preço de cabelereira')
  Cb.FornecerPrecos
  print('\n Preço de maquiadora')
  Mi.FornecerPrecos()
  print('\n Preço da Massagista')
  Ma.FornecerPrecos()
  print('\n Preço de Designer de Sobrancelha')
  Ds.FornecerPrecos()

if opcao == 7:
  print('\n -------Solicite o seu serviço ---------')
  c1.solicitar_servico()

if opcao == 8:
  print('\n ---------Pagina de cancelamento de serviço-------------')
  c1.cancelarservico()
if opcao == 9:
  print('\n ------------Qual especialidade você está procurando? ---------- ')
  e1.escolher_especialidade()
if opcao == 10:
  Pe.marcar_horario()
if opcao == 11:
  Pe.escolher_pagamentos()
if opcao == 12:
  c1.avaliar_servico()