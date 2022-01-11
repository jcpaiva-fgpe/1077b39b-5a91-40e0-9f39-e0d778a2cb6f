while True:
    try:
        option = int(input("Kelvin-Celsius [1] / Celsius-Kelvin [2]?\n"))
        temp = float(input())
        if option == 1:
            print(f"{round(temp - 273.15, 2)}°C")
        elif option == 2:
            print(f"{round(temp + 273.15, 2)}°K")
        else:
            break
        
    except ValueError:
        break