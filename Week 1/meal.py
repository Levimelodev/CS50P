

def convert(time):

   hour, minutes = time.split(":")
   hour = int(hour)
   minutes = int(minutes)
   minutes = minutes/60
   time = (hour)+(minutes)
   return time


def main():
    time = input("What time is it: ")
    time = convert(time)

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
