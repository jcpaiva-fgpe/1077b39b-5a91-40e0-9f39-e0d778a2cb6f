st = input()
lif = st.replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('!', '').replace('?', '').lower().split()
res = {i : lif.count(i) for i in set(lif) if lif.count(i)>1}
print (True if len (res)!= 0 else False)