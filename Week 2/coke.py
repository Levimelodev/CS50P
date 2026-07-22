
num = 1
amount = int(50)
print("Amount Due: 50")

while num != 0:
  insert = int(input("Insert Coin: "))

  if insert == 10 or insert == 25 or insert == 5:
    amount = (amount)-insert

    if amount >0:
      print(f"Amount Due: {amount}")

    else:
      owed = abs(amount)
      print(f"Change Owed: {owed}")
      num = 0

  else:
   print(f"Amount Due: {amount}")

