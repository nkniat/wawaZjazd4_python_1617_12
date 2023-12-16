from random import randint

class Drone():
    """
    Klasa służąca do obsługi dronów. Przymuje wartość 'speed' jak prędkość.
    """
    def __init__(self, speed, max_altitude, battery_life, manufacturer):
        self.altitude = 0
        self.max_altitude = max_altitude
        self.speed = speed
        self.battery_life = battery_life
        self.remaining_battery = battery_life
        self.manufacturer = manufacturer
        self.flying = False

    def __str__(self):
        return "Dron " + str(self.manufacturer) + " o mocy:" + str(self.speed) + ", na wysokości: " + str(self.altitude)

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

    def check_battery(self):
        print("Stan baterii: ", self.remaining_battery)

    def recharge(self):
        self.remaining_battery = self.battery_life
        print("Dron zostal naładowany")

    def fly(self):
        if self.remaining_battery > 0 and not self.flying:
            self.flying = True
            self.altitude += self.speed
            print("Dron wystartował")
        else:
            # albo mam za mało baterii albo już latam
            print("Nie mogę wystartować!")

    def land(self):
        if self.flying:
            self.flying = False
            self.altitude = 0
            print("Dron wylądował")
        else:
            print("Jestem już na ziemi")

    def calculate_flight_time(self):
        return self.remaining_battery / self.speed


"""
- Opracuj klasę DroneFleet, aby zarządzać wieloma dronami.
- Dodaj funkcjonalność dodawania nowych dronów do floty, usuwania dronów i wyświetlania statusu floty
(poziom naładowania baterii, aktualna wysokość, itp.).
- Przetestuj różne scenariusze z udziałem wielu dronów wykonujących loty, lądowania, sprawdzanie stanu baterii
oraz aktualizacje statusu floty
"""
class DroneFleet:
    def __init__(self):
        self.drones = list()

    def add_drone(self, drone):
        self.drones.append(drone)

    def remove_drone(self, drone):
        if drone in self.drones:
            self.drones.remove(drone)
            print("Dron usunięty z floty")
        else:
            print("Nie ma takiego drona we flocie")

    def display_status(self):
        # wyświetlnie dronów
        for drone in self.drones:
            print(drone)

# wykorzystane wyrazenie listowne do stworzenia 10 dronów
drones = [Drone(randint(1,10), 1000, 100, "Nokia") for _ in range(10)]

# podniesienie losowego drona w góre
for i in range(1000):
    droneIndex = randint(0, 9)
    drones[droneIndex].moveUp()

# obniżenie losowego drona w góre
for i in range(1000):
    droneIndex = randint(0, 9)
    drones[droneIndex].moveDown()


drones[1].fly()
print(drones[1].altitude)