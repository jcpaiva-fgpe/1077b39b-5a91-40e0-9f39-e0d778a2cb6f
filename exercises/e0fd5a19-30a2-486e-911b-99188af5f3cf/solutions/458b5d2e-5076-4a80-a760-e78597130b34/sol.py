d = input("Date (DD.MM.YYYY)?\n").split('.')
day = d[0]
month = d[1]

if ((int(month)==12 and int(day) >= 22) or (int(month)==1 and int(day)<= 19)):
    zodiac_sign = ("Capricorn")
elif ((int(month)==1 and int(day) >= 20) or (int(month)==2 and int(day)<= 17)):
    zodiac_sign = ("Aquaris")
elif ((int(month)==2 and int(day) >= 18) or (int(month)==3 and int(day)<= 19)):
    zodiac_sign = ("Pisces")
elif ((int(month)==3 and int(day) >= 20) or (int(month)==4 and int(day)<= 19)):
    zodiac_sign = ("Aries")
elif ((int(month)==4 and int(day) >= 20) or (int(month)==5 and int(day)<= 20)):
    zodiac_sign = ("Taurus")
elif ((int(month)==5 and int(day) >= 21) or (int(month)==6 and int(day)<= 20)):
    zodiac_sign = ("Gemini")
elif ((int(month)==6 and int(day) >= 21) or (int(month)==7 and int(day)<= 22)):
    zodiac_sign = ("Cancer")
elif ((int(month)==7 and int(day) >= 23) or (int(month)==8 and int(day)<= 22)): 
    zodiac_sign = ("Leo")
elif ((int(month)==8 and int(day) >= 23) or (int(month)==9 and int(day)<= 22)): 
    zodiac_sign = ("Virgo")
elif ((int(month)==9 and int(day) >= 23) or (int(month)==10 and int(day)<= 22)):
    zodiac_sign = ("Libra")
elif ((int(month)==10 and int(day) >= 23) or (int(month)==11 and int(day)<= 21)): 
    zodiac_sign = ("Scorpio")
elif ((int(month)==11 and int(day) >= 22) or (int(month)==12 and int(day)<= 21)):
    zodiac_sign = ("Sagittarius")

print(zodiac_sign)