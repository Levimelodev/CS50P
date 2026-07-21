
camel = input("camelCase: ")

num = 0
for y in camel:
  num = num + 1

resul = ""

for x in camel:
  while camel != num+1:
   if x.isupper():
     x = "_"+(x.lower())
     resul = resul+(x)

   elif x.lower():
     x = x.lower()
     resul = resul+(x)

   break
print(f"snake_case: {resul}")
