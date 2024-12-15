from abc import ABC, abstractmethod


class Passport(ABC):
    def __init__(self, name, surname, city, country, id) -> None:
        self.name = name
        self.surname = surname
        self.city = city
        self.country = country
        self.id = id

    @abstractmethod
    def passport_info(self):
        pass

    def __str__(self) -> str:
        return f"Name: {self.name}, Surname: {self.surname}, City: {self.city}, Country: {self.country}, ID: {self.id}"


class ForeignPassport(Passport):
    def __init__(self, name, surname, city, country, id, pass_number, visa_list) -> None:
        super().__init__(name, surname, city, country, id)
        self.pass_number = pass_number
        self.visa_list = visa_list

    def passport_info(self):
        return f"Passport Number: {self.pass_number}, Visas: {', '.join(self.visa_list)}"
    def addVisa(self,newCountry):
        self.visa_list.append(newCountry)
    def removeVisa(self,oldCountry):
        self.visa_list.remove(oldCountry)

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, Passport Number: {self.pass_number}, Visas: {', '.join(self.visa_list)}"
        )


f1 = ForeignPassport(
    name="Ivan",
    surname="Petrenko",
    city="Kyiv",
    country="Ukraine",
    id="AB123456",
    pass_number=12345678,
    visa_list=["Poland", "Germany", "Italy", "Japan"],
)
f1.addVisa("France")
print(f1)
f1.removeVisa("Poland")
print(f1.passport_info())


class TemperatureConverter:
    # Статична змінна для підрахунку кількості конвертацій
    _conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Конвертує температуру з Цельсія у Фаренгейт.
        Формула: (°C × 9/5) + 32 = °F
        """
        TemperatureConverter._conversion_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """
        Конвертує температуру з Фаренгейта у Цельсій.
        Формула: (°F − 32) × 5/9 = °C
        """
        TemperatureConverter._conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        """
        Повертає кількість виконаних конвертацій.
        """
        return TemperatureConverter._conversion_count

# Приклад використання
if __name__ == "__main__":
    print("25°C у Фаренгейтах:", TemperatureConverter.celsius_to_fahrenheit(25))  # 77.0
    print("77°F у Цельсіях:", TemperatureConverter.fahrenheit_to_celsius(77))    # 25.0

    print("Кількість виконаних конвертацій:", TemperatureConverter.get_conversion_count()) 