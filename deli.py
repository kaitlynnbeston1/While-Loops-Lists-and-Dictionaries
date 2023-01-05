import random

sandwichOrders = ["tuna", "toasted tomato", "ham and cheese", "roast beef"]
finishedSandwiches = []
while sandwichOrders:
    order = sandwichOrders.pop()
    finishedSandwiches.append(order)
    num = random.randint(10, 99)
    print(f"Finished making your {order} sandwich. \n Pick up at front desk with order number {num}.")
print("Completed orders are as follows: ")
for order in finishedSandwiches:
    print(order)