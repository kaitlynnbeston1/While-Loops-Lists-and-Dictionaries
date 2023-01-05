import random

sandwichOrders = ["pastrami", "tuna", "pastrami", "toasted tomato", "pastrami", "ham and cheese", "pastrami", "turkey and swis", "salmon", "pastrami", "roast beef", "pastrami", "egg salad", "pb & j", "chicken salad", "pulled pork"]
finishedSandwiches = []
print("NOTICE: \n Unfortunately, we have run out of pastrami. \n All customers who have chosen this sandwich must select a new one.")


while "pastrami" in sandwichOrders:
    sandwichOrders.remove("pastrami")


while sandwichOrders:
    order = sandwichOrders.pop()
    finishedSandwiches.append(order)
    num = random.randint(10, 99)
    print(f"Finished making your {order} sandwich. \n Pick up at front desk with order number {num}.")
print("Completed orders are as follows: ")
for order in finishedSandwiches:
    print(order)