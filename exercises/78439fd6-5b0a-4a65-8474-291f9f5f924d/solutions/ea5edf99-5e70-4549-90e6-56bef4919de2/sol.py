letter = 'A'
while True:
    print(f"Word - {letter}***?")
    word = input().upper()
    if word[0] == letter:
        letter = word[-1]
    else:
        print("Game over.")
        break