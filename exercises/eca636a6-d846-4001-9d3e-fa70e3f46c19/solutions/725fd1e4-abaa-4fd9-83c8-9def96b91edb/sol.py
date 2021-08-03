rome_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

while True:
    print('Rome?')
    rome_in = input().upper()

    a = b = res = 0

    for i in rome_in:
        prev = a
        if i in rome_dict:
            a = rome_dict[i]
            
        if a > prev:
            b = -2*prev
        res += b + a
    
    print("Arabic:", res)
