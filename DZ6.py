        # Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує

class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    def __str__(self):
        return f"{self.name} - {self.destination}"


# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали

class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        print(f"До місця {destination} їхали {distance // self.speed} годин.")


# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів (об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()

class Bus(Transport):
    def __init__(self, speed, capacity, passengers=None):
        super().__init__(speed)

        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

        self.capacity = capacity

    def __str__(self):
        return f"{self.name} - {self.destination}"


    def board_passenger(self, passenger):
        if self.capacity > len(self.passengers):
            self.passengers.append(passenger)
            print(f"Зайшов пасажир {passenger.name} - {passenger.destination}")
        else:
            print("Автобус заповнений.")

    def move(self, destination, distance):

        count = 0

        leav_pas = []
        rem_pas = []

        for passenger in self.passengers:
            if passenger.destination == destination:
                rem_pas.append(passenger)
                count += 1
            else:
                leav_pas.append(passenger)

        self.passengers = leav_pas

        print(f"На зупинці {destination} вийшло {count} пасажирів: .")  # не зміг вивести нормально список пасажирів,
                                                                    # які вийшли - як зробити чарівний метод для ліста

        super().move(destination,distance)


passenger1 = Passenger("Ivan", 'Rovno')
passenger2 = Passenger("Roman", 'Gitomir')
passenger3 = Passenger("Kate", 'lutsk')
passenger4 = Passenger("Svetlana", 'Rovno')
passenger5 = Passenger("Ivan", 'Lviv')

passengers = [passenger1, passenger2, passenger3]

bus_lviv = Bus(60, 4, passengers=passengers)

bus_lviv.move("Kykyivo", 100)
bus_lviv.board_passenger(passenger4)
bus_lviv.board_passenger(passenger5)

bus_lviv.move("Gitomir", 200)

bus_lviv.move("Rovno", 300)
