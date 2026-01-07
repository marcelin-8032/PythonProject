from vehicle import ElectricVehicle


def test_electric_vehicle():

    ev = ElectricVehicle("Tesla", "Model 3", 50, 200)
    print(ev.brand, ev.model)
    print("Range:", ev.km_range(), "km")

    print(ev.drive(450))
    print("Battery:", ev.battery_level, "%")

    print(ev.charge())
    print("Battery:", ev.battery_level, "%")
