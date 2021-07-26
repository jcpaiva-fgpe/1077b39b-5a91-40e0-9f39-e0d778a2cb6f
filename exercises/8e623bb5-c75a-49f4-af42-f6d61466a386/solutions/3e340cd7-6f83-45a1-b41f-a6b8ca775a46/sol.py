d = {}
while True:
    print('Result?')
    try:
        res = str(input()).split()
        d[res[0]] = float(res[1])
        maxv = max(d.values())
        maxk = [k for k, v in d.items() if v == maxv] 
        print('Leader:', *maxk, maxv)
    except:
        break
