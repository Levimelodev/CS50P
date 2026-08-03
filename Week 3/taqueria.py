
try:
 total = float(0)
 while True:
  try:
    text = input("Item: ")
    text = text.lower().strip()

    items = {"burrito": "7.50", "bowl": "8.50", "nachos": "11.00",
         "quesadilla": "8.50","super burrito": "8.50", "super quesadilla": "9.50",
         "taco": "3.00", "tortilla salad": "8.00"}

    for item in items:
      price = items[text]
      price = float(price)

    if text in items:
        total = price + total
        print(f"Total: ${total:.2f}")
  except KeyError:
       print("Item: ")
       break

except EOFError:
   print()
