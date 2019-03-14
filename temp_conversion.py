fahrenheit = input("What is the temperature in Fahrenheit today? ")

celsius = (int(fahrenheit) - 32) / 1.8

if celsius <= 0:
    print("That's " + str(celsius) + " degrees Celsius! It's freezing outside! Wear your coat.")
elif celsius > 0 and <= 10:
    print("That's " + str(celsius) + " degrees Celsius! It's pretty chilly. Bring a jacket.")

# print(str(celsius))