print("small letter", "\n")
temp = float(input("temp in c"))
unit = input("unit you want(f k r)")

## only 1
print("\n", "only 1")
result = 0
if(unit == "f"):
    result = ((9 / 5) * temp) + 32
elif(unit == "k"):
    result = temp + 273.15
elif(unit == "r"):
    result = (temp * 0.8)
print(result, unit)

## display all
print("\n", "all")
faren = ((9 / 5) * temp) + 32
kelvin = temp + 273.15
romer = (temp * 0.8)
print(temp, "c", faren, "f", kelvin, "k", romer, "r")