print("-SULE CAKE-")
print("Dapatkan penawaran terbaik dari toko kami")
print("1.Jika anda membeli 5 hingga 20 kue coklat anda akan mendapatkan diskon sebesar 7%")
print("2.Jika anda membeli 21 hingga 35 kue coklat anda akan mendapatkan diskon sebesar 12%")
print("3.Jika anda membeli 4  hingga 15 kue keju anda akan mendapatkan diskon sebesar 10%")
print("4.Jika anda membeli 16 hingga 25 kue keju anda akan mendapatkan diskon sebesar 15%")
def Start():
    print('--------------MENU--------------\n1. kue keju\n2. kue coklat\n3.keluar')
    a = int(input("pilihan anda = "))
    if a == 1 :
        hargakuekeju1()
        loop1()
    if a == 2 :
        hargakuecoklat1()    
        loop1()
    if a == 3 :
        End()

def hargakuekeju1():
    jumlahpesanankeju = int(input("Masukan Jumlah Pesanan Anda = "))
    if jumlahpesanankeju >= 4 and jumlahpesanankeju <= 15:
        kuekeju1 = 6000
        diskonkeju1 = jumlahpesanankeju * kuekeju1 * 10/100 
        jumlah = jumlahpesanankeju * kuekeju1 - diskonkeju1
        print(jumlah)
    elif jumlahpesanankeju >= 16 and jumlahpesanankeju <= 25:
        kuekeju2 = 6000
        diskonkeju2 = jumlahpesanankeju * kuekeju2 * 15/100
        jumlah = jumlahpesanankeju * kuekeju2 - diskonkeju2
        print(jumlah)  

def hargakuecoklat1():
    jumlahpesanancoklat = int(input("Masukan Jumlah Pesanan Anda = "))
    if jumlahpesanancoklat >= 5 and jumlahpesanancoklat <= 20:
        kuecoklat1 = 3500
        diskoncoklat1 = jumlahpesanancoklat * kuecoklat1 * 7/100 
        jumlah = jumlahpesanancoklat * kuecoklat1 - diskoncoklat1
        print(jumlah)
    elif jumlahpesanancoklat >= 21 and jumlahpesanancoklat <= 35:
        kuecoklat2 = 3500
        diskoncoklat2 = jumlahpesanancoklat * kuecoklat2 * 12/100
        jumlah = jumlahpesanancoklat * kuecoklat2 - diskoncoklat2
        print(jumlah) 
    
def loop1() :
    answer = str(input("Apakah anda ingin kembali memesan ? = [Ya/Tidak] "))
    if answer == ("Ya") :
        Start()
    if answer == ("Tidak") :
        End()

def End() :
    print("Terima kasih telah memesan")

Start()



