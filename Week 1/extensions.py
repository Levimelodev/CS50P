filetype = input("File name: ").lower().strip()
_ = "image/"

if filetype.endswith(".zip"):
    print(f"application/zip")

elif filetype.endswith(".jpeg"):
    print(f"{_}jpeg")

elif filetype.endswith(".png"):
    print(f"{_}png")

elif filetype.endswith(".jpg"):
    print(f"{_}jpeg")

elif filetype.endswith(".gif"):
    print(f"{_}gif")

elif filetype.endswith(".txt"):
    print("text/plain")

elif filetype.endswith(".pdf"):
    print("application/pdf")

else:
    print("application/octet-stream")
