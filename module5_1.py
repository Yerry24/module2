class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if i <= self.number_of_floors:
                print(i)
            else:
                print("Такого этажа не существует")
                break


h0 = House('ЖК Эльбрус', 30)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h0.go_to(5)
h1.go_to(5)
h2.go_to(10)