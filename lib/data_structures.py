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
    return [food["name"] for food in spicy_foods]
# => ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
   
    

def get_spiciest_foods(spicy_foods):
    pass
    # returns a list of dictionaries where the heat level of the food is greater than 5.
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    pass
    # output to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        print (f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")
  


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    # returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
    for food in spicy_foods:
      
        # print(f"Checking food: {food['name']} ({food['cuisine']})")
        print(f"Checking food: {food['name']} ({food['cuisine']})")
        print(f"Comparing {food['cuisine']} with {cuisine}")
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    pass
    # outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:
    # Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"] 
            heat_level = food["heat_level"]

            print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

def get_average_heat_level(spicy_foods):
    pass
    # and returns an integer representing the average heat level of all the spicy foods in the array
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_of_foods = len(spicy_foods)
    return total_heat // num_of_foods 



