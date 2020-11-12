print("-SELAMAT DATANG DI OPANG CELL-")
print("         SALE UP TO 50%      ")
def Start():
    str(print('Merk Handphone\n1. Iphone\n2. Vivo\n3. Samsung\n4. Redmi\n5 Realme\n6. Keluar'))
    a = int(input("Pilihan anda = "))

    if a == 1:
        hargaiphone()
        loop1()
    elif a == 2:
        hargavivo()
        loop1()
    elif a == 3:
        hargasamsung()
        loop1()
    elif a == 4 :
        hargaredmi()
        loop1()
    elif a == 5:
        hargarealme()
        loop1  
    elif a == 6 :
        End()


def hargaiphone():
    iphone = print('IPHONE DISCON 20%')
    aa  = print("1. Iphone 7\t= Rp.3.000.000\n2. Iphone 8\t= Rp.5.000.000\n3. Iphone X\t= Rp.7.000.000\n4. Iphone 11\t= Rp.13.000.000")
    pil = float(input('Masukan Pilihan Anda! = '))
    if pil == 1:
        harga_iphone = 3000000
        diskon = int(harga_iphone) * 20/100 #20%
        bayar = int(harga_iphone) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 2:
        harga = 5000000
        diskon = harga * 20/100 #20%
        bayar = int(harga) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 3:
        harga = 7000000
        diskon = harga * 20/100 #20%
        bayar = int(harga) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 4:
        harga = 13000000
        diskon = harga * 20/100 #20%
        bayar = int(harga) - diskon
        print('Total Harga = Rp.{}'.format(bayar))

def hargavivo():
    vivo = print('VIVO DISCON 30%')
    aa  = print("1. Vivo y12\t= Rp.1.999.000\n2. Vivo y91c\t= Rp.1.599.000\n3. Vivo y20s\t= Rp.3.299.000\n4. Vivo y12i\t= Rp.1.899.000")
    pil = float(input('Masukan Pilihan Anda! = '))
    if pil == 1:
        harga_vivo = 1999000
        diskon = int(harga_vivo) * 30/100 #30%
        bayar = int(harga_vivo) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 2:
        harga_vivo = 1599000
        diskon = int(harga_vivo) * 30/100 #30%
        bayar = int(harga_vivo) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 3:
        harga_vivo = 3299000
        diskon = int(harga_vivo) * 30/100 #30%
        bayar = int(harga_vivo) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 4:
        harga_vivo = 1899000
        diskon = int(harga_vivo) * 30/100 #30%
        bayar = int(harga_vivo) - diskon
        print('Total Harga = Rp.{}'.format(bayar))

def hargasamsung():
    samsung = print('SAMSUNG DISCON 25%')
    aa  = print("1. samsung A01\t= Rp.1.250.000\n2. samsung A10S\t= Rp.1.550.000\n3. samsung A11\t= Rp.1.899.000\n4. samsung A30\t= Rp.2.500.000")
    pil = float(input('Masukan Pilihan Anda! = '))
    if pil == 1:
        harga_samsung = 1250000
        diskon = int(harga_samsung) * 25/100 #25%
        bayar = int(harga_samsung) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 2:
        harga_samsung = 1550000
        diskon = int(harga_samsung) * 25/100 #25%
        bayar = int(harga_samsung) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 3:
        harga_samsung = 1899000
        diskon = int(harga_samsung) * 25/100 #25%
        bayar = int(harga_samsung) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 4:
        harga_samsung = 2500000
        diskon = int(harga_samsung) * 25/100 #25%
        bayar = int(harga_samsung) - diskon
        print('Total Harga = Rp.{}'.format(bayar))

def hargaredmi():
    redmi = print('REDMI DISCON 25%')
    aa  = print("1. redmi 8A Pro\t= Rp.1.550.000\n2. redmi 8\t= Rp.1.900.000\n3. redmi 9A\t= Rp.1.299.000\n4. redmi Note 8\t= Rp.2.100.000")
    pil = float(input('Masukan Pilihan Anda! = '))
    if pil == 1:
        harga_redmi = 1550000
        diskon = int(harga_redmi) * 25/100 #25%
        bayar = int(harga_redmi) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 2:
        harga_redmi = 1900000
        diskon = int(harga_redmi) * 25/100 #25%
        bayar = int(harga_redmi) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 3:
        harga_redmi = 1299000
        diskon = int(harga_redmi) * 25/100 #25%
        bayar = int(harga_redmi) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 4:
        harga_redmi = 2100000
        diskon = int(harga_redmi) * 25/100 #25%
        bayar = int(harga_redmi) - diskon
        print('Total Harga = Rp.{}'.format(bayar))

def hargarealme():
    Realme = print('REALME DISCON 15%')
    aa  = print("1. realme c11\t= Rp.1.599.000\n2. realme c12\t= Rp.1.899.000\n3. realme c15\t= Rp.2.199.000\n4. realme c17\t= Rp.2.499.000")
    pil = float(input('Masukan Pilihan Anda! = '))
    if pil == 1:
        harga_realme = 1599000
        diskon = int(harga_realme) * 15/100 #15%
        bayar = int(harga_realme) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 2:
        harga_realme = 1899000
        diskon = int(harga_realme) * 15/100 #15%
        bayar = int(harga_realme) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 3:
        harga_realme = 2199000
        diskon = int(harga_realme) * 15/100 #15%
        bayar = int(harga_realme) - diskon
        print('Total Harga = Rp.{}'.format(bayar))
    elif pil == 4:
        harga_realme  = 2499000
        diskon = int(harga_realme) * 15/100 #15%
        bayar = int(harga_realme) - diskon
        print('Total Harga = Rp.{}'.format(bayar))

def loop1() :
    answer = str(input(" Apakah anda ingin kembali ke manu utama? [Ya/Tidak] "))
    if answer == ("Ya") :
        Start()
    elif answer == ("Tidak") :
        End()


def End():
    print("TERIMA KASIH SUDAH MEMBELI HANDPHONE DI COUNTER KAMI")
      




Start()
