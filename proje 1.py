# Hesap makinesi

# Toplama fonksiyonu
def toplama(x, y):
    return x + y


# Çıkarma fonksiyonu
def cikarma(x, y):
    return x - y


# Çarpma fonksiyonu
def carpma(x, y):
    return x * y


# Bölme fonksiyonu
def bolme(x, y):
    return x / y


print("Select operation.")
print("1.toplama")
print("2.cikarma")
print("3.carpma")
print("4.bolme")

while True:
    # kullancıdan istediği işlemi seçmesini isteriz
    islem = input("yapmak istediğiniz işlemi seçiniz (1/2/3/4): ")

    # kullancıdan hesaplamak istediği sayıları girmesini isteriz
    if islem in ('1', '2', '3', '4'):
        sayi1 = float(input("1. sayıyı giriniz: "))
        sayi2 = float(input("2. sayıyı giriniz: "))

        if islem == '1':
            print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))

        elif islem == '2':
            print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))

        elif islem == '3':
            print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))

        elif islem == '4':
            print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))

        # if kullanarak kullancının yeni bir işlem yapmak istediğini test ederiz
        # kullancı hayır derse işlemi bitiriz
        yeni_islem = input("yeni bir işlem yapmak ister misiniz? (evet/hayır): ")
        if yeni_islem == "hayır":
            break

    else:
        print("Hatalı Giriş")