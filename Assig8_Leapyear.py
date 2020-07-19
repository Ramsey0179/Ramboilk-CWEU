year = int(input("Sene kaç, girin lütfen :"))
leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
result = (leap_year == True)*'artık yıldır.' + (leap_year == False)*'artık yıl değildir.'
print(f"Girdiğiniz *{year:^10}* senesi {result:^20}!")
