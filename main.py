#criação de funçõellipsis

preco = 1999,90

#Caucular apenas 5% de imposto, guardar na variavel imposto e exibir na tela 
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que caucular um imposto de 5% e retornar a quem pediu... 
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto 
  print(imposto)

#Aqui é o imposto... aqui é imposto a calcular.. e exibir na tela 
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é como a função (7%): {imposto}"

print(preco) 
preco_procuto = 100
print(preco_produto)


#agora calcular impostos a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]
#se eu calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de...é..."(1o. preço, 2o. imposto)
for valor in valores: 
  print(f"O imposto de {valo} é {calcular_imposto(valorr)}")


  #Declarar um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto 
  for valor in valores:
    print(f"O imposto de {valo} é {calcular_imposto_aliquota(valor)}")
    for valor in valores:
     print(f"O imposto de {valo} é {calcular_imposto_aliquota(valor,7)}")
      for valor in valores:
        print(f"O imposto de {valo} é {calcular_imposto_aliquota(valorr,10)}")


