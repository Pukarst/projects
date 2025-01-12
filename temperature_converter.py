def temp_converter():
    print("-----WELCOME TO THE TEMPERATURE CONVERSION-----")
    print("Select the conversion type :-")
    print("1. Celsius(°C) --->Fahrenheit(°F)")
    print("2. Fahrenheit(°F)--->Celsius(°C)")
    print("3. Celsius(°C)--->Kelvin(K)")
    print("4. Kelvin(K)--->Celsius(°C)")
    print("5. Fahrenheit(°F)--->Kelvin(K)")
    print("6. Kelvin(K)--->Fahrenheit(°F)")

    choice = input("Enter your choice :: (1/2/3/4/5/6): ")

    temp = float(input("Enter the temperature of your choice: "))

    if choice == '1':
        result = (temp * 9/5) + 32
        print(f"The entered temperature {temp}°C is converted into {result}°F.")
    elif choice == '2':
        result = (temp - 32) * 5/9
        print(f"The entered temperature {temp}°F is converted into {result}°C.")
    elif choice == '3':
        result = temp + 273.15
        print(f"The entered temperature {temp}°C is converted into {result}K.")
    elif choice == '4':
        result = temp - 273.15
        print(f"The entered temperature {temp}K is converted into {result}°C.")
    elif choice=='5':
        result=5/9*(temp-32)+273.15
        print(f"The entered temperature {temp}°F is converted into {result}K.")
    elif choice=='6':
        result=9/5*(temp-273.15)+32
        print(f"The entered temperature {temp}K is converted into {result}°F.")
    else:
        print("Invalid choice!!!! Enter the correct choice.")

temp_converter()
