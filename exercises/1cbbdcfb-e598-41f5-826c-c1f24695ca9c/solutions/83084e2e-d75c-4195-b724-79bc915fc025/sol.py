print('String:')
napis = input().split()
res = [napis[i] for i in range(len(napis)) if napis[i][-1] == '.']
print(*res)
