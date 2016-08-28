colorDictionary = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb"}

for key, value in colorDictionary.items():
    print("this dictionary include color {}".format(key))

user_input = input("please enter a color name:")

print(colorDictionary[user_input])