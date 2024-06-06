class Building:
    def __init__(self):
        self.numberOfFloors = int
        self.buildingType = str

    def __eq__(self, other):
        return self.numberOfFloors == other.buildingType

floors_1 = Building()
floors_2 = Building()
print(floors_1 == floors_2)