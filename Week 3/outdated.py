
lista = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
while True:

   #conversao do texto
   text = input("Date: ")
   text = text.lower().strip()
   text = text.capitalize()

   if "-" in text:
      space_text = text.split('-')

      try:
        int(space_text[1])
        int(space_text[2])


        space_text[2], space_text[1] = space_text[1], space_text[2] #conversão de formato [0]
        space_text[1], space_text[0] = space_text[0], space_text[1] #Conversão de formato [1]

        print(f"{space_text[0]}-{space_text[1]}-{space_text[2]}")
        break

      except:
        continue

   elif text.split()[0] in lista and "," in text:
           space_text = text.split()
           space_text[1] = space_text[1].strip(',')

           try:
              int(space_text[1])
              int(space_text[2])

              space_text[2], space_text[1] = space_text[1], space_text[2] #conversão de formato [0]
              space_text[1], space_text[0] = space_text[0], space_text[1] #conversão de formato [1]

              if int(space_text[2]) < 1 or int(space_text[2]) > 31:
                 continue


              if space_text[1] == "January":
                 space_text[1] = int(1)

              elif space_text[1] == "February":
                 space_text[1] = int(2)

              elif space_text[1] == "March":
                 space_text[1] = int(3)

              elif space_text[1] == "April":
                 space_text[1] = int(4)

              elif space_text[1] == "May":
                 space_text[1] = int(5)

              elif space_text[1] == "June":
                 space_text[1] = int(6)

              elif space_text[1] == "July":
                 space_text[1] = int(7)

              elif space_text[1] == "August":
                 space_text[1] = int(8)

              elif space_text[1] == "September":
                 space_text[1] = int(9)

              elif space_text[1] == "October":
                 space_text[1] = int(10)

              elif space_text[1] == "November":
                 space_text[1] = int(11)

              elif space_text[1] == "December":
                 space_text[1] = int(12)

              print(f"{space_text[0]}-{space_text[1]}-{space_text[2]}")
              break

           except:
              continue

   else:
      continue


