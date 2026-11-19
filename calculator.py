import os

password = os.environ.get("APP_PASSWORD")


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return sum(numbers) / len(numbers)


def get_user(users, name):
    for u in users:
        if u["name"] == name:
            return u["email"]
    return None


if __name__ == "__main__":
    print(divide(10, 2))
    print(average([1, 2, 3]))
