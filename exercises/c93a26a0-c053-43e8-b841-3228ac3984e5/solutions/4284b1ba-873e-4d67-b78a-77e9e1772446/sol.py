while True:
    try:
        rollers = int(input("Enter the number of rollers:\n"))
        brushes = int(input("Enter the number of brushes:\n"))

        if rollers == brushes == 0: break
        total_mass = rollers * 75 + brushes * 112
        masa_kg = total_mass/1000
        print(f"Total mass: {total_mass}g ~ {round(masa_kg, 1)}kg")
        
        if masa_kg > 20:
            pack_amount = int(masa_kg/20) + 1
            lightest = round(masa_kg - 20 * (pack_amount - 1), 1)
            
        else:
            pack_amount = 1
            lightest = masa_kg

        parcels_id = ['small parcel', 'large parcel']
        if lightest < 10: type = parcels_id [0]
        else: type = parcels_id [1]

        print (f"Number of packages: {pack_amount}, lightest: {type}, weight: {lightest}kg")
        tn = input ("Next package?\n")
        if tn.lower() == "no": break

    except:
        break
