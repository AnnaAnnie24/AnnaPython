answer = input("What measure unit do you use: Fahrenheit or Celsius?  ")
if answer == "Celsius":
    c = input("How many degrees is it in celsius? ")
    c = int(c)
    f = c * 1.8 + 32
    f = round(f, 2)
    f = str(f)
    print(f + " degrees in fahrenheit")
elif answer == "Fahrenheit":
    f = input("How many degrees is it in Fahrenheit? ")
    f = int(f)
    c = (f - 32) * 5/9
    c = round(c, 2)
    c = str(c)
    print(c + " degrees in celsius")
