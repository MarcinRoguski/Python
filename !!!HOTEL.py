import time

class Room:
    def __init__(self, number, price, kitchen, number_of_beds, air_condition, floor):
        self.number = number
        self.price = price
        self.kitchen = kitchen
        self.number_of_beds = number_of_beds
        self.air_condition = air_condition
        self.floor = floor

with open("rooms.txt", "r", encoding = "UTF-8") as file_rooms:
    text = file_rooms.read().splitlines()

print(text[1])
#room_101 = Room(text[1])
room_102 = Room(102, 100, False, 1, False, 1)
#print(room_101)
print(room_102.price)