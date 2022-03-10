'''
*args
Antes de mais nada, ele não precisa se chamar args, mas precisa ter o *! poderia muito bem ser *some_list ou *xyz. O nome “args” é uma convenção.
Imagine uma função em que você precise imprimir o nome de um país e quantas copas do mundo ele ganhou: A Espanha tem 1 título, o Brasil tem 5… Como faríamos?
def world_cup_titles(country, *args):
    print('Country: ', country))
    for title in args:
        print('year: ', title)
Observe que na função, iteramos sobre args, exibindo cada título passado e que o fato de ser possível iterar sobre uma lista de argumentos nos dá a flexibilidade que precisamos para o nosso caso.
1- Chamada com 5 itens no *args:
>>> world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')
Country:  Brasil
Year:  1958
Year:  1962
Year:  1970
Year:  1994
Year:  2002
2- Chamada com 1 item no *args:
>>> world_cup_titles('Espanha', '2010')
Country:  Espanha
Year:  2010
**kwargs
Antes de mais nada, ele não precisa se chamar kwargs, mas precisa ter os **! poderia muito bem ser **some_dict ou **xyz. O nome “kwargs” é uma convenção.
Agora imagine uma situação em que você precise passar diferentes argumentos, talvez para diferentes propósitos. Como ficaria?
Usaremos uma função de cálculo de preço como exemplo. Nela, teremos dois argumentos opcionais, discount e tax_percentage:
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value
Já que os argumentos são opcionais, podemos calcular o preço final de um produto sem desconto ou impostos:
>>> final_price = calculate_price(100.0)
>>> print(final_price)
100.0
Mas também podemos aplicar um desconto a ele:
>>> final_price = calculate_price(100.0, discount=5.0)
>>> print(final_price)
95.0
Ou adicionar um imposto:
>>> final_price = calculate_price(100.0, tax_percentage=7)
>>> print(final_price)
107.0
Ou ainda, aplicar um desconto e adicionar um imposto:
>>> final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
>>> print(final_price)
102.0
Mas por que usei **kwargs e não *args?
Observe no exemplo acima que o nome dos argumentos variáveis é extremamente importante, já que por ele é possível saber se o valor se trata de um imposto ou um desconto a ser aplicado! Não se trata de uma lista de argumentos a serem iterados, e sim de argumentos opcionais com finalidades completamente diferentes, identificados por seus nomes!
Também é possível combinar *args e **kwargs, mas por hora vamos apenas entender a diferença entre os dois.
'''

def world_cup_titles(country, *args):
  print('Country: ', country)
  for title in args:
    print('year: ', title)

world_cup_titles('Brasil', 1983,1998)

def calculate_price(value, **kwargs):
  tax_percentage = kwargs.get('tax_percentage')
  discount = kwargs.get('discount')
  if tax_percentage:
      value += value * (tax_percentage / 100)
  if discount:
      value -= discount
  return value

final_price = calculate_price(100.0)
print(f"just final price {final_price}")

final_price = calculate_price(100.0, discount=5.0)
print(f"price with discount {final_price}")

final_price = calculate_price(100.0, tax_percentage=7)
print(f"price with tax percentage {final_price}")

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(f"price with both {final_price}")