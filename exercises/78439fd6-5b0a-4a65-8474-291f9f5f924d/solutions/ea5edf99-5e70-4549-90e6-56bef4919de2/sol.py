letter = 'A'
while True:
    print(f"Enter a word beginning with {letter}:")
    word = input().upper()
    if word[0] == letter:
        letter = word[-1]
     else:
        print("You lost.")
        break