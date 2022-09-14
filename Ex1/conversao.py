def conversor(escolha, valor):
  if escolha == 1:
    resultado1 = (valor * 3.281)
    return print(round(resultado1, 4))
  elif escolha == 2:
    resultado2 = (valor * 0.3048)
    return print(round(resultado2, 4))