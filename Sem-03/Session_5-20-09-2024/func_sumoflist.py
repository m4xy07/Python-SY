def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def calculate_total_cost(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total

print_details(name="Aman", age=20, occupation="Injinia")
total_cost = calculate_total_cost(apples=3.5, bananas=2.8, oranges=4.1)
print(f"Total Cost: ${total_cost}")
