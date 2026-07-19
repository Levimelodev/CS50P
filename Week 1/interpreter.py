
expression = input("Expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
  print(f"{x + z}")

elif y == "*":
   print(f"{x * z}")

elif y == "-":
    print(f"{x - z}")

elif y == "/":
     print(f"{x / z}")
