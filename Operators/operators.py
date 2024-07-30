# temperature = 25
# if temperature == 25:
#     print('It is summer and the temperature is too hot today')
#     print('Drink plenty of water')
# else:
#     print('The temperature is in normal condition')


weight = float(input("weight"))
unit = input("Type K for kg And P for pound")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Pounds ", converted)
else:
    converted = weight * 0.45
    print("Weight in kg", converted)
