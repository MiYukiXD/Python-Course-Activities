flavors = ["boots", "chocolate", "strawberry", "cookies n' cream", "Bubblegum"]
toppings = ["almonds", "banna slices", "chocolate syrup", "caramel syrup", "white chips"]
ice_cream = dict(zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)