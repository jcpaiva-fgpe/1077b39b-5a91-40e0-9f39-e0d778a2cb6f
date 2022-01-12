while True:

    options = [['1', 'Kelvin', 'Kelvin-Celsius', 'K'], ['2', 'Celsius', 'Celsius-Kelvin', 'C']]
    for i in range (2): print(f'{options[i][2]} [{options[i][0]}]' + ' | '*((i+1)%2), end="") 
    print()

    try:
        option = input().strip().upper()
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
            