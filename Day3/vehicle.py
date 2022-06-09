class Vehicle:
    def __init__(self, max_speed, mileage, seating_capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity = 50):
        super().__init__(max_speed, mileage, seating_capacity)
    def fare(self):
        return (self.seating_capacity * 100) * 1.1

vehicle1 = Vehicle(80, 2500, 4)
bus1 = Bus(65, 234)

print(vehicle1.fare())
print(bus1.fare())