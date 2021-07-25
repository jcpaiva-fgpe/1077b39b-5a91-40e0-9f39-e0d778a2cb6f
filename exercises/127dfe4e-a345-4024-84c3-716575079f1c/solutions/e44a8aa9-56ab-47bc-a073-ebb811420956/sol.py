while True:
    try:
        print(sum(list(map(int, input()))))
        
    except ValueError:
        break