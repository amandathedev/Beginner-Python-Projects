dollar = input("How many dollars do you have? ")

euro = float(dollar) * 0.88
euro = round(euro, 2)

baht = float(dollar) * 31.76
baht = round(baht, 2)

dong = float(dollar) * 23190
dong = round(dong, 2)

kip = float(dollar) * 8582
kip = round(kip, 2)

forint = float(dollar) * 278.1
forint = round(forint, 2)

print(f"You have:\n {euro} Euros\n {baht} Baht\n {dong} Dong\n {kip} Kip\n {forint} Forint")