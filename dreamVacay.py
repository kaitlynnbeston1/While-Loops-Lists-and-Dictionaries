results = {}


polling = True
while polling:
    name = input("What is your name? ").title()
    place = input("If you could travel anywhere, where would it be? ").title()
    results[name] = place
    again = input("Would you like to let another person respond? \n Type y or n: ")
    if again == "n":
        polling = False


print("Here are the results of the pole:")
for name, place in results.items():
    print(f"{name} would like to go to {place}.")