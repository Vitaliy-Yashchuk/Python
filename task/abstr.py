from abc import ABC, abstractmethod


# class Ship(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def powerGuns(self):
#         pass

#     def __str__(self) -> str:
#         return self.name


# # inheritamce: class Deriver(Base)
# class Frigate(Ship):
#     def __init__(self,speed,powerGun) -> None:
#         super().__init__("Frigate")
#         self.speed = speed
#         self.powerGun = powerGun

#     def __str__(self) -> str:
#         return f"{self.name}: {self.speed}km"

#     def powerGuns(self):
#         return self.powerGun

# class Destroyer(Ship):
#     def __init__(self, speed, size, personnel) -> None:
#         super().__init__("Destroyer")
#         self.speed = speed
#         self.size = size
#         self.personnel = personnel

#     def __str__(self) -> str:
#         return f"{self.name}: {self.speed}km \nSize: {self.size}\nPersonnel: {self.personnel}"

#     def powerGuns(self):
#         return  
    
# class Cruiser(Ship):
#     def __init__(self,speed,powerGun,CruisingRange) -> None:
#         super().__init__("Cruiser")
#         self.speed = speed
#         self.powerGun = powerGun
#         self.CruisingRange=CruisingRange

#     def __str__(self) -> str:
#         return f"{self.name}: {self.speed}km\nCruisingRange:{self.CruisingRange}"

#     def powerGuns(self):
#         return 
# f1 = Frigate(24, 6500)
# D1 = Destroyer(240, 2300, 124)
# print(f1)
# print(f"Power  : {f1.powerGuns()}cm^2")
# print(D1)


class Airplane:
    def __init__(self, model, passengers, max_passengers):
        self.model = model                   
        self.passengers = passengers         
        self.max_passengers = max_passengers 
        
    def __eq__(self, other):
        return self.model == other.model
    def __add__(self, value):
        new_count = self.passengers + value
        return Airplane(self.model, min(new_count, self.max_passengers), self.max_passengers)
    def __iadd__(self, value):
        self.passengers = min(self.passengers + value, self.max_passengers)
        return self
    def __sub__(self, value):
        new_count = self.passengers - value
        return Airplane(self.model, max(new_count, 0), self.max_passengers)
    def __isub__(self, value):
        self.passengers = max(self.passengers - value, 0)
        return self
    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers
    def __int__(self):
        return self.passengers
    def __str__(self):
        return f"Модель літака: {self.model}, Пасажири: {self.passengers}/{self.max_passengers}"

if __name__ == "__main__":
    plane1 = Airplane("Boeing 737", 50, 200)
    plane2 = Airplane("Airbus A320", 100, 180)
    plane3 = Airplane("Boeing 737", 75, 200)

    print(plane1)
    print(plane2)
    print("plane1 == plane3:", plane1 == plane3)
    plane1 += 30
    print(plane1)
    plane2 -= 50
    print(plane2)
    print("plane1 > plane2:", plane1 > plane2)
    print("Кількість пасажирів у plane1:", int(plane1))


