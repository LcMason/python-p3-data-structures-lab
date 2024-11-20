spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    # return a list of strings with the names of each spicy food.
    return [food ["name"] for food in spicy_foods]
    

def get_spiciest_foods(spicy_foods):
    pass
    # returns a list of dictionaries where the heat level of the food is greater than 5.
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    # returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
    result = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return result[0] if result else None

def print_spiciest_foods(spicy_foods):
    pass
  
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]

            print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

def get_average_heat_level(spicy_foods):
    pass
    # and returns an integer representing the average heat level of all the spicy foods in the array
    total_heat = sum(food['heat_level'] for food in spicy_foods)

    num_of_food = len(spicy_foods)

    return total_heat // num_of_food

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)

    return spicy_foods
