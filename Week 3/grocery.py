
dicionario = {} #dic

while True:
    try:

      oque_usuario_digitou = input("") #text
      oque_usuario_digitou = oque_usuario_digitou.upper()

      if oque_usuario_digitou in dicionario:
            dicionario[oque_usuario_digitou] += 1

      else:
           dicionario[oque_usuario_digitou] = 1

    except EOFError:
      print("")
      break


for cada_item in dicionario:
   print(dicionario[cada_item], cada_item)
