while True:
    try:
        rollers = int(input("A?\n"))
        brushes = int(input("B?\n"))

        if rollers == brushes == 0: break
        total_mass = rollers * 75 + brushes * 112
        masa_kg = total_mass/1000
        print(f"{total_mass}g ~ {round(masa_kg, 1)}kg")
        
        if masa_kg > 20:
            pack_amount = int(masa_kg/20) + 1
            lightest = round(masa_kg - 20 * (pack_amount - 1), 1)
            
        else:
            pack_amount = 1
            lightest = masa_kg

        p_id = ['S', 'L']
        if lightest < 10: type = p_id [0]
        else: type = p_id [1]

        print (f"#{pack_amount}, weight: {lightest}kg [{type}]")
        tn = input ("Next package?\n")
        if tn.lower() == "true": continue
        else: break

    except:
        break
