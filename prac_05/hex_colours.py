# Constant dictionary of color names and their hexadecimal codes
COLOR_TO_HEX = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF"
}

print("Color Hexadecimal Lookup")
print(COLOR_TO_HEX.keys())

color_name = input("Enter color name: ").strip().title()


while color_name:
    if color_name in COLOR_TO_HEX:
        print(f"{color_name} hex code is {COLOR_TO_HEX[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ").strip().title()