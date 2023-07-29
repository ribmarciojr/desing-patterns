# many wheels 
class Vehicle:
    def __init__(self, name, brand) -> None:
        self.name = name
        self.brand = brand


class Car(Vehicle):
    def __init__(self, name, brand) -> None:
        super().__init__(name, brand)

    def getWheels(self) -> int:
        return 4

    def __str__(self) -> str:
        return f'Car: {self.name} {self.brand}'


class Moto(Vehicle):
    def __init__(self, name, brand) -> None:
        super().__init__(name, brand)

    def getWheels(self) -> int:
        return 2

    def __str__(self) -> str:
        return f'Moto: {self.name} {self.brand}'

class Ship(Vehicle):
    def __init__(self, name, brand) -> None:
        super().__init__(name, brand)

    def getWheels(self) -> None:
        return None

    def __str__(self) -> str:
        return f'Ship: {self.name} {self.brand}'

class VehicleFactory():
    @classmethod
    def create(self,type:str, name :str, brand: str) -> Vehicle:
        match type:
            case 'car':
                return Car(name, brand)
            case 'moto':
                return Moto(name, brand)
            case 'ship':
                return Ship(name, brand)
            case other:
                return 'We do not have this type of vehicle'



test = VehicleFactory.create('moto', 'ninja','kawazaki')

test2 = VehicleFactory.create('car', 'Cross','Corolla')

test3 = VehicleFactory.create('ship', 'Big ship','Bmw')

print(f"{type(test)} {test.getWheels()}")
print(f"{type(test2)} {test2.getWheels()}")
print(f"{type(test3)} {test3.getWheels()}")
print(VehicleFactory.create('caminhão', 'big caminhão', 'mercedes'))

