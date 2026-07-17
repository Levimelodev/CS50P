dollars = int("0")
greeting = input("Greeting: ").strip().lower()

if "hello" in greeting:
    print(f"${dollars}")

elif greeting[0] == "h" or greeting[0]== "H":
    print(f"${dollars+20}")

else:
    print(f"${dollars+100}")
