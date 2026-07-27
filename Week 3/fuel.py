
while True:
  try:
    text = input("Fraction: ")
    text = text.split("/")

    value1 = text[0]
    value2 = text[1]

    value1 = int(value1)
    value2 = int(value2)

    math = value1/value2
    math = (math)*100
    math = round(math)
    math = int(math)

  except ZeroDivisionError:
    text = input("Fraction: ")
    text = text.split("/")

    value1 = text[0]
    value2 = text[1]

    value1 = int(value1)
    value2 = int(value2)

    math = value1/value2
    math = (math)*100
    math = round(math)
    math = int(math)

  except ValueError:
   while True:
    text = input("Fraction: ")
    text = text.split("/")

    value1 = text[0]
    value2 = text[1]

    value1 = int(value1)
    value2 = int(value2)

    math = value1/value2
    math = (math)*100
    math = round(math)
    math = int(math)
  except IndexError:
   while True:
    text = input("Fraction: ")
    text = text.split("/")

    value1 = text[0]
    value2 = text[1]

    value1 = int(value1)
    value2 = int(value2)

    math = value1/value2
    math = (math)*100
    math = round(math)
    math = int(math)

  if math <= 1:
    print("E")
    break

  elif value1 > value2:
    text = input("Fraction: ")
    text = text.split("/")

    value1 = text[0]
    value2 = text[1]

    value1 = int(value1)
    value2 = int(value2)

    math = value1/value2
    math = (math)*100
    math = round(math)
    math = int(math)

  elif math >= 99:
    print("F")
    break


  else:
    math = str(math)
    print((math)+"%")
    break

