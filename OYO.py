def car_cost(days):
  if days<3:
    return 5000*days
  elif 3<=days<7:
    return 5000*days-200
  elif days>=7:
    return 5000*days-500
days = int(input("How many days: "))
print("Your car rent for ",days,"days is",car_cost(days))


def hotel_cost(nights):
    return nights*5000
#cost: 5000/night
nights = int(input("How Many Nights You Want To Stay:: \n"))
print("Your Hotel cost is",hotel_cost(nights))


def hotel_room_cost(room):
  if room=="Single":
    return 1500
  if room=="Double":
    return 2500
  if room=="Triple":
    return 3500
  if room=="Quad":
    return 4500
  if room=="Queen":
    return 7500
  if room=="King":
    return 8500
  if room=="Twin":
    return 10000
  if room=="Double-Double":
    return 10500
  if room=="Studio":
    return 12500
  if room=="Master Suite":
    return 15500
  if room=="Mini-Suite or Junior Suite":
    return 13500
  if room=="Connecting Rooms":
    return 14500
  if room=="Adjoining Rooms":
    return 12500
  if room=="Adjacent Rooms":
    return 16500
  else:
    print("Sorry we Dont Have Data For:: \n",room)   
    return 0
room= input("Enter room type: ")
print("Your Room cost is",hotel_room_cost(room))
