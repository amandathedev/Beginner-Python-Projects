cups = input("How many cups do you need? ")

cups = int(cups)

tablespoons = cups * 16.66
teaspoons = cups * 50
pints = cups * 0.44
quarts = cups * 0.264
liters = cups * 0.25
gallons = cups * 0.066
fluid_ounces = cups * 8.333

print(f"That's {tablespoons} tablespoons, {teaspoons} teaspoons, {pints} pints, {quarts} quarts, {liters} liters, {gallons} gallons, {fluid_ounces} fluid ounces")
