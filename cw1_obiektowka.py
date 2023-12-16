from random import randint

class Drone():
    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def __str__(self):
        return "Dron o mocy:" + str(self.speed) + ", na wysokości: " + str(self.altitude)

    def moveUp(self):
        self.altitude += self.speed


# lista do przechowania 10 dronów
drones = list()

# wykorzystana petla do stworzenia 10 elementów
# for _ in range(10):
#     # tworze nowego drona wykorzystujac forme Drone()
#     newDrone = Drone()
#     drones.append(newDrone)


# wykorzystane wyrazenie listowne do stworzenia 10 dronów
drones = [Drone(randint(1,10)) for _ in range(10)]

# podniesienie losowego drona w góre
for i in range(1000):
    droneIndex = randint(0, 9)
    drones[droneIndex].moveUp()

# wyświetlnie dronów
for drone in drones:
    print(drone)