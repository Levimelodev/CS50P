alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = alphabet.split()

numbers = "0 1 2 3 4 5 6 7 8 9"
numbers = numbers.split()

ex_zero = "1 2 3 4 5 6 7 8 9"
ex_zero = ex_zero.split()

text = input("PLATE: ")

num = 0
for x in text:
    num = num + 1

def is_valid(text):
    #If it has 2 charcaters

    if num == 1 and (text[0] in alphabet or text[0] in numbers):
       print("Invalid")

    elif text[0] in alphabet and text[1] in alphabet and num == 2:
       print("Valid")



    #If it has 3 characters
    elif text[0] in alphabet and text[1] in alphabet and num == 3 and (text[2] in ex_zero or text[2] in alphabet):
       print("Valid")

    elif text[0] in alphabet and text[1] in alphabet and num == 4 and (text[2] in ex_zero and (text[3] in numbers) or text[2] in alphabet and (text[3] in ex_zero)):
       print("Valid")

    elif text[0] in alphabet and text[1] in alphabet and num == 5:
               #LL-LLL
               if text[2] in alphabet and text[3] in alphabet and text[4] in alphabet:
                  print("Valid")

               #LL-LLE
               elif text[2] in alphabet and text[3] in alphabet and text[4] in ex_zero:
                   print("Valid")

               #LL-LEN
               elif text[2] in alphabet and text[3] in ex_zero and text[4] in numbers:
                   print("Valid")
               else:
                   print("Invalid")


    elif text[0] in alphabet and text[1] in alphabet and num == 6:
                   #LL-LLLL
                   if text[2] in alphabet and text[3] in alphabet and text[4] in alphabet and text[5] in alphabet:
                      print("Valid")

                   #LL-LLLE
                   elif text[2] in alphabet and text[3] in alphabet and text[4] in alphabet and text[5] in ex_zero:
                       print("Valid")

                   #LL-LLEN
                   elif text[2] in alphabet and text[3] in alphabet and text[4] in ex_zero and text[5] in numbers:
                       print("Valid")

                   #LL-LENN
                   elif text[2] in alphabet and text[3] in ex_zero and text[4] in numbers and text[5] in numbers:
                        print("Valid")
                   else:
                        print("Invalid")



    else:
        print("Invalid")


is_valid(text)

