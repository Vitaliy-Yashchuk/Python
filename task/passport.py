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


# error with creating Figure with abstract methods
# figure = Figure("Figure")