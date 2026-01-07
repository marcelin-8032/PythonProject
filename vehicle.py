from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f"Vehicle(brand '{self.brand}', model= '{self.model}')"

    @property
    @abstractmethod
    def km_range(self):
        pass

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def charge(self):
        pass


class ElectricVehicle(Vehicle):

    def __init__(self, brand, model, battery_level, km_range):
        super().__init__(brand, model)
        self.battery_level = battery_level
        self._km_range = km_range

    def km_range(self):
        return self._km_range * (self.battery_level / 100)

    def drive(self, distance):
        if distance > self.km_range():
            return "Battery low"

        used_battery = (distance / self._km_range) * 100
        self.battery_level -= used_battery
        return f"Drove {distance} km"

    def charge(self):
        self.battery_level = 100
        return "Battery full"
