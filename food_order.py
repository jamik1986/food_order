italian_food = ["pasta bolognese", "pepperoni pizza",
                "margherita pizza", "lasagna"]

indian_food = ["curry", "chutney", "samosa", "naan"]


def find_meal(name, menu):
    if name in menu:
        return name
    else:
        return None


def select_meal(name, food_type):
    if food_type == "italian":
        return find_meal(name, italian_food)
    elif food_type == "indian":
        return find_meal(name, indian_food)
    else:
        return None


def display_available_meals(food_type):
    if food_type == "italian":
        print("Available Italian Meals")
        for meal in italian_food:
            print(meal)
    elif food_type == "indian":
        print("Available Indian meals")
        for meal in indian_food:
            print(meal)
    else:
        print("Sorry, but we don't have it")


def create_summary(name, amount):
    order = select_meal(name, food_type)
    if order:
        return f"You ordered {amount} {name}"
    else:
        return "Meal was not found"


print("Welcome to the Food Order System! We have Italian and Indian Food in the menu. ")

if __name__ == "__main__":
    food_type = input("What type of food you want today? ").strip().lower()
    display_available_meals(food_type)
    name_input = input("Enter the name of the meal you want to order: ").strip().lower()
    amount_input = int(input("Enter the quantity you want to order: "))
    result = create_summary(name_input, amount_input)
    print(result)
