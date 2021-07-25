import re
print("E-mail strings:")
while True:
    txt = input()
    a = re.findall("[A-z0-9]+[.][\w-]?[a-z]\w+[@]\w+[.]\w+", txt)
    if not a: break
    for i,j in enumerate(a):
        name_email = j.split('@')[0]
        l = [i for i in name_email if i.isdigit()]
        print(f"{i+1})", name_email, *sorted(set(l), reverse=True))
print("end.")
