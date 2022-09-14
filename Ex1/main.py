##título
print(" Olá, bom te ver por aqui! Seja bem-Vindo ao Conversor de pés para metros e metros para pés :P\n");

##Fazer um módulo que converte
##Pé -> Metros -> Pé: Entrada do usuário que define a ##conversão
##1 pé = 0,3048 metros
##1 metro = 3,281 pés
##Entregar 1 código por grupo de 2

##input dos dados do usuário
valor = float(input("Digite o valor a ser convertido: "))
escolha = int(input("Você quer converter para metro->pés[1] ou pés->metros[2]?: "))

##modulo
from conversao import conversor
c = conversor(escolha, valor)

##footer :)
print("\n\nby Fabiana Sayuri e Erick Aguiar :)")