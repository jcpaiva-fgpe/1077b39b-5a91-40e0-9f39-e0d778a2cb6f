silkroad = "Beijing - Xian - Lanzhou - Xiahe - Wuwei - Zhangye - Jiayuguan Pass - Dunhuang - Turpan - Urumqi - Kashgar - Shanghai"
przystanki = silkroad.split(' - ')
print('In?')
i = input()
print('Out?')
j = input()
if i in przystanki and j in przystanki:
    if przystanki.index(i) < przystanki.index(j):
        print("Route:", *przystanki[przystanki.index(i)+1:przystanki.index(j)])
    else: 
        print("Route:", *przystanki[przystanki.index(j)+1:przystanki.index(i)][::-1])
else: 
    print(False)
