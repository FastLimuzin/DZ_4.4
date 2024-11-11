# Пример с *args:
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)

# Пример с **kwargs:
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Евгений", age=35, city="Москва")

# Комбинированный пример:

def user_profile(greeting, *args, **kwargs):
    print(greeting)
    print("Interests:")
    for interest in args:
        print(f"- {interest}")
    print("Additional info:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


user_profile("Hello!", "Reading", "Traveling", name="Евгений", age=35, city="Москва")


