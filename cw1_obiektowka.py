from random import randint

class Drone():
    """
    Klasa służąca do obsługi dronów. Przymuje wartość 'speed' jak prędkość.
    """
    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def __str__(self):
        return "Dron o mocy:" + str(self.speed) + ", na wysokości: " + str(self.altitude)

    def moveUp(self):
        """
        Ta metoda porusza dronem w górę o prędkość, jaką ma dany dron
        :return:
        """
        self.altitude += self.speed

    def moveDown(self):
        # if (self.altitude - self.speed) < 0:
        #     self.altitude = 0
        # else:
        #     self.altitude -= self.speed
        self.altitude = max(0, self.altitude - self.speed)

    def changeSpeed(self, new_speed):
        self.speed = new_speed

# lista do przechowania 10 dronów
drones = list()
#
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

# obniżenie losowego drona w góre
for i in range(1000):
    droneIndex = randint(0, 9)
    drones[droneIndex].moveDown()


# wyświetlnie dronów
for drone in drones:
    print(drone)


print("Przed zmianą:", drones[0])
drones[0].changeSpeed(20)
print("Po zmianie:", drones[0])
