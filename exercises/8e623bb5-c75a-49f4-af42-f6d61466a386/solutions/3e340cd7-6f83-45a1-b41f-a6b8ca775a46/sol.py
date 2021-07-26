d = {}
while True:
    print('Enter the result:')
    res = input().split()
    try:
        if res[0] != 'end':
            d[res[0]] = float(res[1])
            maxv = max(d.values())
            maxk = [k for k, v in d.items() if v == maxv] 
            print('Leader:', *maxk, maxv)
        else: break
    except:
        break