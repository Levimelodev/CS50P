
import sys
from pyfiglet import Figlet
figlet = Figlet()

count = len(sys.argv) #count
fonts = figlet.getFonts()

if count == 1:
   print("Without any fonts...")

elif count == 3 and sys.argv[1] == '-f':
   u_font = sys.argv[2]
   figlet.setFont(font=u_font)
# se a fonte nao for encontrada retorne para 'else:'

   user_type = input(f"Input: ")
   print(f'\n{user_type}') #teste falho em mudar a fonte
   print(figlet.renderText(user_type))

else:
   sys.exit("Invalid usage")
