
text = input("Input: ")
vogals = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

new_text = ""
for x in text:
      if x in vogals:
        x = ""
        new_text = new_text+(x)

      else:
        x = x
        new_text = new_text+(x)

print(f"Output: {new_text}")
