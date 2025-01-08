# # 1. Klammern nochmal erklären
# ## Listen werden immer mit [] initialisiert
# name_list = ["Christof", "Mete", "Joshua", "Nassima", "Sebastian"]
# # Element in einer Liste können über Indizes abgerufen werden
# # In der Liste oben gibt es index 0 --> "Christof" name_list[0]
# # index 1 --> "Mete"
# # index 2 --> "Joshua"
# print(f"Das erste Element ist: {name_list[0]}")
# print(f"Das zweite Element ist: {name_list[1]}")
# print(f"Das dritte Element ist: {name_list[2]}")
# print(f"Das 4. Element ist: {name_list[3]}")
# print(f"Das 5. Element ist: {name_list[-1]}")
# print(f"Die geamte Liste sieht so aus: {name_list}")
# for i in range(len(name_list)):
#     print(f"Das {i}. Element ist aus dem Loop: {name_list[i]}")
# for n in name_list:
#     print(f"Element ist aus neuen dem For-Loop ist: {n}")

# ------------------------------------------------------------------------


class Vehicles:
    def __init__(
        self,
        vehicle_brand_name,
        vehicle_model_name,
        average_consumption_in_l,
        tank_volume,
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.volume = tank_volume

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven

    def get_total_tank_volume(self):
        one_fill = self.consumption * self.volume
        return self.km_driven / one_fill


my_vehicle = Vehicles("VW", "Golf", 10, 100)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")
print(
    f"Der Golf muss bei 1000km, {my_vehicle.get_total_tank_volume()}x nachgetankt werden"
)
