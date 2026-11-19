password = "admin123"

def divide(a, b):
    return a / b

def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

def get_user(users, name):
    for u in users:
        if u["name"] == name:
            return u["email"]

print(divide(10, 0))
print(average([]))
