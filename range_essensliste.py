weekdays = ["Montag", "Dienstag", "Mittwoch"]
food = []
for w in weekdays:
    for _ in range(2):
        food_input = input(f"Was möchtest du am {w} essen?")
        food.append(food_input)
print(f"Der Essensplan für die gesamte Woche sieht wie folgt aus: {food}")
