#Space Travel Calulator
print("Welcome to the Space Travel Calculator!")

#Distance
distance = input("What is the distance to the celestial object?")
distance = int(distance)

#Speed
speed = input("What is the speed of the spacecraft?")
speed = int(speed)

#time
print("It will take you" + "" + str(distance / speed) + "" + "to reach your destination")