while True:
    try:
        name, pesel = map(str, input().split())
        sum_psl = sum([int(pesel[i])*j for i, j in enumerate([i for i in [1,3,7,9]*3][:-2])])
        plec, last = map(int, pesel[9:])
        r, m, d = map(str, [pesel[i:i+2] for i in range(0,5,2)])
    except ValueError: break
    
    status = 10 - int(str(sum_psl)[-1])
    if status == last:
       zwroty = 'Ms.' if plec % 2 == 0 else 'Mr.'
       r = f'19{r}' if int(m) < 20 else f'20{r}'
       m = int(m) if int(m) < 20 else int(m) - 20
       m = f'0{m}' if m < 10 else str(m) 
       data = f'{d}.{m}.{r}'
       from datetime import datetime
       tday = datetime.now()
       wiek = (tday.year - int(r)) - ((tday.month, tday.day) < (int(m), int(d)))
    else: break
    print(zwroty, f'{name.title()}({wiek}), {data}, PESEL: {pesel}.')