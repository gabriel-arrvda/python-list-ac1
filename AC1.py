# -*- coding: utf-8 -*-
class CalcCientifica:


  def __init__(self, numero):

    self.numero = numero

  def potencia(self, expoente=2):

    return self.numero**expoente

  def raiz(self, indice=2):

    return self.numero**(1/indice)
  
  def fatorial(self, n = 0):
    if (self.numero - 1) == n:
      self.numero = n

    if self.numero < 2:
      return 1

    else:
      return self.numero * self.fatorial(self.numero - 1)
##########################################################################

# testando a classe criada
num1 = 9
num2 = 8

# cria dois objetos - um para cada numero
calc1 = CalcCientifica(num1)
calc2 = CalcCientifica(num2)

# calcula a raiz quadra 
raiz1 = calc1.raiz()
raiz2 = calc2.raiz(indice=3)

# calcula a raiz quadra 
potencia1 = calc1.potencia()
potencia2 = calc2.potencia(expoente=4)

# calcula o fatorial
fact1 = calc1.fatorial()
fact2 = calc2.fatorial()

print('Resultado esperado: ')
print('\tRaiz quadrada de 9: 3')
print('\t9 elevado a 2: 81')
print('\tFatorial de 9: 362880')

print('\n\n\tRaiz cubica de 8: 2')
print('\t8 elevado a 4: 4096')
print('\tFatorial de 8: 40320')

print('\n' + 20*'-')
print('Resultado retornado: ' )
print('\tRaiz quadrada de %d: %d' %(num1,raiz1))
print('\t%d elevado a 2: %d' %(num1,potencia1))
print('\tFatorial de %d: %d' %(num1,fact1))

print('\n\tRaiz cubica de %d: %d' %(num2,raiz2))
print('\t%d elevado a 4: %d' %(num2,potencia2))
print('\tFatorial de %d: %d' %(num2,fact2))

################# ESCREVA SEU CÓDIGO AQUI  ###############################
def retornaImpares(numero, helper = []):

  if numero == 1:
    helper.append(''+str(numero))
    helper.reverse()
    array_str = ''.join([str(item) for item in helper])
    return array_str

  elif (numero%2 != 0):
    helper.append(' '+str(numero))

  return retornaImpares(numero-1 , helper)

##########################################################################

# testando a função criada
impares = retornaImpares(8)

print('Resultado esperado:')
print('\t1 3 5 7')

print('\n' + 20*'-')
print('Resultado retornado:')
print('\t'+impares)

if impares != '1 3 5 7' and impares != '1 3 5 7 ':
    print('\nAtenção! Seu resultado foi diferente do que era esperado')


################# ESCREVA SEU CÓDIGO AQUI  ###############################
def contaPalavras(lista):
  dicionario = {}
  total = 0
  maisRepetida = 'teste'
  menosRepetida = 'teste'

  for lst in lista:
    for arr in lst:
      if arr in dicionario:
        dicionario[arr] = dicionario[arr] + 1
      else:
        dicionario[arr] = 1
  
  total = len(dicionario.keys())
  menosRepetida = min(dicionario, key = dicionario.get)
  maisRepetida = max(dicionario, key = dicionario.get)

  return total, maisRepetida, menosRepetida

##########################################################################

# testando a função criada
lista = [
    ['Angola','Chade','Gana'],
    ['Chade','Angola','Gana','Togo'],
    ['Togo','Gana','Chade','Eritreia'],
    ['Chade','Togo','Angola']
]

total, maisRepetida, menosRepetida = contaPalavras(lista)

print('Resultado esperado:')
print('\tTotal: 5') 
print('\tPalavra que mais repetiu: Chade') 
print('\tPalavra que menos repetiu: Eritreia') 

print('\n' + 20*'-')
print('Resultado retornado:')
print('\tTotal: %d' %(total)) 
print('\tPalavra que mais repetiu: %s' %(maisRepetida)) 
print('\tPalavra que menos repetiu: %s' %(menosRepetida))

################# ESCREVA SEU CÓDIGO AQUI  ###############################
def retornaMenor(lista):

  menorValor = 0
  i = 0

  for i in range(len(lista)):
    if(menorValor == 0):
      menorValor = lista[i]

    if lista[i] < menorValor:
      menorValor = lista[i]

    else:
      i+=1
  
  return menorValor
##########################################################################

# testando a função criada
lista = [10,6,2,9,8,23,5]
menor = retornaMenor(lista)

print('Resultado esperado: 2')

print('\n' + 20*'-')
print('Resultado retornado: %d' %(menor) )

################# ESCREVA SEU CÓDIGO AQUI  ###############################
import datetime

class Funcionario:
  def __init__ (self, nome, departamento, salarioBruto, 
    anoEntrada, rg, dependentes, defineEmprego= True, defineAno= 0):
    
    self.nomeFuncionario = nome
    self.departamento  =  departamento
    self.salarioBruto = salarioBruto
    self.anoEntrada = anoEntrada
    self.anoSaida = defineAno
    self.rg = rg
    self.statusEmprego = defineEmprego
    self.dependentes = dependentes
    self.aux=0

  def calcSalarioLiquido(self):
    baseCalculo = self.salarioBruto + (self.dependentes*20)

    if baseCalculo <= 1000:
      salarioLiquido = baseCalculo - (baseCalculo*0.03)
    
    else:
      salarioLiquido = baseCalculo - (baseCalculo*0.05)

    return salarioLiquido
    
  def calcTempoServico(self):
    date = datetime.date.today()
    ano = date.strftime("%Y")
    ano = int(ano)
    self.aux = ano - self.anoEntrada
    return ano - self.anoEntrada
    
  def calcAumento(self):
    aumento = 0.0
    if self.aux < 5 :
      aumento = self.salarioBruto*0.05
    elif self.aux > 5 :
      aumento += self.salarioBruto*0.08
    return aumento

  def retornaInfo (self):
    srtg = "Nome: {}. Departamento {}. Salario líquido {}. Aumento {}.".format(self.nomeFuncionario,self.departamento,self.calcSalarioLiquido(),self.calcAumento())
    return srtg

##########################################################################

# testando a classe criada
nome = "Pedro Cardoso"
departamento = "TI"
salarioBruto = 5000
anoEntrada = 2000
rg = '192528'
dependentes = 5

func1 = Funcionario(
    nome, departamento, salarioBruto, 
    anoEntrada, rg, dependentes 
    )

salario = func1.calcSalarioLiquido()
tempo = func1.calcTempoServico()
aumento = func1.calcAumento()
info = func1.retornaInfo()
statusFunc = func1.statusEmprego

print('Resultado esperado: ')
print('\t O funcionário está empregado?: True')
print('\t Salario Liquido: 4845.00')
print('\t Tempo de serviço: 22 anos')
print('\t Aumento: 400.00')

print('\n\tString retornada pelo método imprimir(): ')

print('\n' + 20*'-')
print('Resultado retornado: ')
print('\t O funcionário está empregado?: %s' %(statusFunc))
print('\t Salario Liquido: %1.2f' %(salario))
print('\t Tempo de serviço: %d anos' %(tempo))
print('\t Aumento: %1.2f' %(aumento))
print('\t Bruto %1.2f' %(func1.salarioBruto))

print('\nInformacoes da classe retornadas pela método retornaInfo: \n%s' %(info))

if not isinstance(info, str):
    print('\nAtenção. O valor retornado pelo método retornaInfo()')
    print('da classe Funcionário deveria ser uma string')

################# ESCREVA SEU CÓDIGO AQUI  ###############################
def buscaBinaria(lista, n):
  start = 0
  end = len(lista) - 1

  menor = -1
  maior = -1

  idxFound = -1

  while start <= end:
    idx = (start + end) // 2

    if lista[idx] == n:
      idxFound = idx
      break
    elif lista[idx] > n:
      end = idx - 1
    else:
      start = idx + 1

  if idxFound != -1:
    menor = idxFound
    maior = idxFound

    idx = idxFound

    search_left = True

    while lista[idx] == n:
      if search_left and idx != 0:
        if lista[idx-1] == n:
          idx = idx - 1
          menor = idx
        else: 
          search_left = False
          idx = idxFound
      else:
        if idx == len(lista) - 1:
          break

        if lista[idx+1] == n:
          idx = idx + 1
          maior = idx
        else: 
          break  

  return menor, maior
##########################################################################

# testando a função criada
lista = [1,2,3,4,5,5,5,5,5,6,7,8,8,8,9,10]

print('\n' + 30*'=' + '\nPrimeiro teste')
numBuscado = 5
firstIndex, lastIndex = buscaBinaria(lista, numBuscado)

print('\nResultado esperado:')
print('\tPrimeiro índice: 4')
print('\tÚltimo índice: 8')

print('\n' + 20*'-')
print('Resultado retornado:' )
print('\tPrimeiro índice: %d' %(firstIndex))
print('\tÚltimo índice: %d' %(lastIndex))

print('\n' + 30*'=' + '\nSegundo teste')
numBuscado = 50
firstIndex, lastIndex = buscaBinaria(lista, numBuscado)

print('\nResultado esperado:')
print('\tPrimeiro índice: -1')
print('\tÚltimo índice: -1')

print('\n' + 20*'-')
print('Resultado retornado:' )
print('\tPrimeiro índice: %d' %(firstIndex))
print('\tÚltimo índice: %d' %(lastIndex))