# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana:Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = 'Banana'
color = "Green"

if color != "Green" or color != "Yellow" or color != "Brown":
    print("Recheck fruit color")
    exit()


if fruit == 'Banana':
    if color == 'Green':
        fruit_status = "Unripe"
    elif color == "Yellow":
        fruit_status = "Ripe"
    else:
        fruit_status = "Overripe"

print("Your {} is {} .".format(fruit,fruit_status))