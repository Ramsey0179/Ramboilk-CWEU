sayi = int(input('bir sayı giriniz'))
asal_list = []

if sayi > 2:
    for x in range(3,sayi+1):
        a = 0
        for i in range(2, x):
            if x % i == 0:
                a +=1
                break
        if a == 0:
            asal_list.append(x)
    print(asal_list)
elif sayi == 2:
    asal_list.append(2)
    print(asal_list)
else:
    print('Asal sayı listesi bulanmamaktadır')