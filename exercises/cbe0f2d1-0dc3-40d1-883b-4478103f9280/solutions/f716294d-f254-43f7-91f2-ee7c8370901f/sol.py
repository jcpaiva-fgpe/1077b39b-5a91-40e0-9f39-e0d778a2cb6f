while True:
    try:
        temp = float(input("Kelvin?\n"))
        print(f"{round(temp + 273.15, 2)}°C")
    except ValueError:
        break