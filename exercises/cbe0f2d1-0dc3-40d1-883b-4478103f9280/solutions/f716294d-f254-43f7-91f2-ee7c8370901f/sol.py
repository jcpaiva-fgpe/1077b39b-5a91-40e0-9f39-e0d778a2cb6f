while True:
    options = [['1', 'Kelvin', 'Kelvin-Celsius'], ['2', 'Celsius', 'Celsius-Kelvin']]
    print("Kelvin-Celsius [1] / Celsius-Kelvin [2]")
    try:
        option = input().strip()
        if option in options[0]:
            temp = float(input(f'Enter {options[0][1]}:\n'))
            print(f"{round(temp - 273.15, 2)}°C")
        elif option in options[1]:
            temp = float(input(f'Enter {options[1][1]}:\n'))
            print(f"{round(temp + 273.15, 2)}°K")
        else:
            print('False')
            break
    except ValueError:
        print('False')
        break