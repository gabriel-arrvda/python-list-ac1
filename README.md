## AC1 - LIST

Exercises from college about python, recursion and binary search made with Google Colab

## Files
- [Jupyter File](./AC1.ipynb)
- [Python File](./AC1.py)

## Exercises

### Exercício 1
Crie uma classe chamada **CalcCientifica** que tenha o seguinte atributo: 
 - numero -> guarda um número 
 
O método construtor da classe deverá receber como argumento de entrada o atributo indicado acima. 

A classe também deve ter is seguintes métodos: 

 - potencia -> retorna o atributo **numero** da classe elevado a um expoente.

     - esse método deve receber um parâmetro chamado **expoente** que deve ser opcional e possui valor **default** igual a 2.  Esse parâmetro receberá o expoente da potenciação. No Python, para você fazer b elevado a c, você pode usar ```b**c```. 
     
 - raiz -> retorna a raiz do atributo **numero** da classe. 

     - esse método deve receber um parâmetro chamado **indice** que deve ser opcional e possui valor **default** igual a 2.  Esse parâmetro receberá o índice da raiz. Lembre-se que para fazer o cálculo da raiz, você pode usar potenciação: $\sqrt[b]{a}$ é o mesmo que $a^{\frac{1}{b}}$.  

 - fatorial -> retorna o fatorial do atributo **numero** da classe. O código de método pode ser igual ao código mostrados na aula de recursividade da disciplina. 
 
 ### Exercício 2 

Crie uma função **recursiva** com o seguinte nome: **retornaImpares**. Essa função deve receber um número digitado como parâmetro e retornar uma **string** com todos os números ímpares de 0 até o número digitado separados por um espaço em branco. Por exemplo, ser for passado o número 8 como entrada, deve retornar: "1 3 5 7".

### Exercício 3

Faça uma função chamada **contaPalavras**. Essa função deve receber uma lista como entrada. 

Cada elemento da lista recebida pela função é uma outra lista de palavras. 

A função deve retornar a palavra que mais se repetiu, a palavra que menos repetiu e o total de palavras sem contar as repetições. 

### Exercício 4

Crie uma função **recursiva** com o seguinte nome: **retornaMenor**. Essa função deve receber uma lista como parâmetro e retornar o menor número. 

## Exercício 5

A empresa “Organizações Tabajaras” precisa de um sistema que faça o controle da folha de pagamento de seus funcionários. 

Para isso, você deve criar uma classe chamada **Funcionario** que tenha os seguintes atributos: 
 - nomeFuncionario -> guarda o nome do funcionário
 - departamento -> guarda o departamento
 - salarioBruto -> guarda o salário bruto
 - anoEntrada -> guarda o ano de entrada na empresa
 - anoSaida -> guarda o ano atual ou o ano em que o funcionário saiu da empresa 
 - rg -> guarda o RG
 - statusEmprego -> valor booleano que indica se o funcionário ainda está trabalhando na empresa ou se já foi demitido
 - dependentes -> quantos dependentes o funcionário possui.
 
O método construtor da classe deverá receber como argumento de entrada todos os atributos indicados acima. Todos eles deverão ser recebidos como atributo obrigatório, exceto os atributos **statusEmprego** e **anoSaida**. O parâmetro associado ao atributo **statusEmprego** deve ser opcional e ter valor *default* igual a **True**. O parâmetro associado ao atributo **anoDemissao** deve ser opcional e ter valor *default* igual a **0**. Na função construtora, caso o parâmetro associado ao atributo **anoDemissao** seja diferente de 0, o atributo **anoDemissao** deve receber o valor informado; senão, deve receber o ano atual.  Para obter o ano atual, você pode usar a biblioteca **datetime** do Python. Veja um exemplo onde a biblioteca **datetime** é usada para calcular o ano em que estamos:

```
import datetime

date = datetime.date.today()
year = date.strftime("%Y")
year = int(year)

print("Ano atual: ", year)
```

A classe também deve ter is seguintes métodos: 

 - calcSalarioLiquido -> cálcula o salário líquido do funcionário (recebe R\\$ 20,00 por dependente; depois, é descontado um imposto de 3\% para funcionários que ganham até R$ 1000,00 e 5% acima deste valor);

 - calcTempoServico -> cálcula o tempo de serviço do funcionário na empresa com base no ano de entrada na empresa e ano atual.

 - calcAumento -> calcula o aumento de salário. O cálculo de aumento de salário (com base no salário bruto) é realizado de acordo com os seguintes dados:
 
   - Tempo de Serviço menor que 5 anos – o percentual equivale a 5%
    
   - Tempo de Serviço maior que 5 anos – o percentual equivale a 8%
   
 - retornaInfo -> retorna uma string com os valores de todos dos atributos da classe. Essa string deve conter também o tempo de serviço, salário líquido e aumento de salário obtidos por meio da chamada das respectivas funções. 

### Exercício 6 

Cria uma função chamada **buscaBinaria**. Essa função deve modificar o algoritmo de busca binária para que retorne o índice da primeira e da última ocorrência de um número em uma lista. Por exemplo, se você informar a lista [1,2,3,3,3,4,5,6] e pedir para buscar o número 3, ele deverá retornar como resultado os valores 2 e 4, que correspondem respectivamente a posição da primeira e última posição onde o número 3 ocorreu. Se o número buscado não for encontrado, o algoritmo deverá retornar -1 e -1.
Teste o novo algoritmo com a lista [1,2,3,4,5,5,5,5,5,6,7,8,8,8,9,10]. 

Teste o novo algoritmo tentando encontrar as posições inicial e final do número 5. Depois, do número 8. Por fim, do número 50. Para cada tentativa, imprima as posições encontradas pelo algoritmo. 
