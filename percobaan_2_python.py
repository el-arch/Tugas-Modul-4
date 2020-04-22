<<<<<<< HEAD
import class1

def error():
    print("\n!!Anda telah memilih inputan yang salah!!")
    return 0

=======
  #Identitas
>>>>>>> a20cc4f5b961071649c3be6148c5ba2643b20343
def non_return_func(praktikan1, praktikan2):
    print(f"{praktikan1} - 21120119140120 dan {praktikan2} - 21120119140145")
    print('Shift 2 - Kelompok 53\n\n')

   #Pemanggilan identitas
non_return_func("Abimanyu Putro Yulianto", "Elmar Leonard")

    #Judul
print('---------E&A Jacket---------\n\n')

<<<<<<< HEAD
hoodie = ["Jeans", "Hoodie", "Kulit"]
harga = [350000, 250000, 450000]
print("Daftar jenis jaket yang kami jual :")
i = 0
while i < 3:
    print("{}. Jaket".format(i+1), hoodie[i], " - Rp.", harga[i])
    i += 1
pil = int(input("Pilih jenis jaket yang anda inginkan = "))
if (pil < 4):
    x = 1
    p1 = class1.kelas(x, hoodie, harga, pil)
    ukuran = ["M", "L", "XL", "XXL"]
    print("\nDaftar ukuran jaket yang tersedia :")
    for i in range(4):
        print("{}.".format(i+1), ukuran[i])
    pil1 = int(input("Pilih ukuran jaket yang anda inginkan = "))
    if (pil1 < 5):
        y = 2
        p1.hasil(y, hoodie, ukuran, harga, pil1, pil)
    elif (pil1 <= 0):
        error()
    else :
       error()
elif(pil <= 0):
    error()
else :
    error()
j = int(input("\nMasukan jumlah yang anda inginkan : "))
h = j*harga[pil-1]
print("\nTerima kasih telah membeli", j, "pakaian")
print("Dengan total harga Rp.", h)
=======
    #pilihan jenis
def non_return_func(jenis1, jenis2, jenis3):
    print(f" Daftar jenis jaket yang kami jual: \n 1. {jenis1} - Rp.350000 \n 2. {jenis2} - Rp.250000 \n 3. {jenis3} - Rp.450000")

    #Pemanggilan pilihan jenis
non_return_func("Jaket Jeans", "Jaket Hoodie", "Jaket Kulit")


    #memilih jenis
x = float(input('Pilih jenis jaket apa yang anda inginkan = '))

if x ==1:
    print('------------------------------------------------------')
    print('Anda telah memilih Jaket Jeans dengan harga Rp.350000')
    print('------------------------------------------------------')
    print('Daftar ukuran jaket yang tersedia')
    print('1. M')
    print('2. L')
    print('3. XL')
    print('4. XXL')
    a = float(input('Pilih ukuran jaket apa yang anda inginkan ='))
    if a ==1:
        print('------------------------------------------------------')
        print('Anda memilih ukuran M')
        print('------------------------------------------------------')

        j = int(input("Masukkan jumlah yang anda inginkan:"))
        h = j*350000
        print('------------------------------------------------------')
        print("Anda telah membeli Jaket Jeans dengan ukuran M berjumlah",j, "\nAnda harus membayar sebesar: Rp.",h)
        print('------------------------------------------------------')
    elif a ==2:
        print('------------------------------------------------------')
        print('Maaf stok ukuran yang anda pilih sudah habis')
        print('------------------------------------------------------')     
    elif a ==3:
        print('------------------------------------------------------')
        print('Anda memilih ukuran XL')
        print('------------------------------------------------------')

        j = int(input("Masukkan jumlah yang anda inginkan:"))
        h = j*350000
        print('------------------------------------------------------')
        print("Anda telah membeli Jaket Jeans dengan ukuran XL berjumlah",j, "\nAnda harus membayar sebesar: Rp.",h)
        print('------------------------------------------------------')
    elif a==4:
        print('------------------------------------------------------')
        print('Anda memilih ukuran XXL')
        print('------------------------------------------------------')

        j = int(input("Masukkan jumlah yang anda inginkan:"))
        h = j*350000
        print('------------------------------------------------------')
        print("Anda telah membeli Jaket Jeans dengan ukuran XXL berjumlah",j, "\nAnda harus membayar sebesar: Rp.",h)
        print('------------------------------------------------------')
    else:
        item = ['\n','!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3','4']
        for ukuran in item:
            print(ukuran)   
               
elif x ==2:
    print('------------------------------------------------------')
    print('Anda telah memilih Jaket Hoodie dengan harga Rp.250000')
    print('------------------------------------------------------')
    print('Daftar ukuran jaket yang tersedia')
    print('1. M')
    print('2. L')
    print('3. XL')
    print('4. XXL')
    b = float(input('Pilih ukuran jaket apa yang anda inginkan ='))
    if b ==1:
        print('-----------------------------------------------------')
        print('Anda memilih ukuran M')
        print('-----------------------------------------------------')

        j = int(input("Masukkan jumlah yang anda inginkan:"))
        h = j*250000
        print('------------------------------------------------------')
        print("Anda telah membeli Jaket Hoodie dengan ukuran M berjumlah",j, "\nAnda harus membayar sebesar: Rp.",h)
        print('------------------------------------------------------')
    elif b ==2:
        print('------------------------------------------------------')
        print('Maaf stok ukuran yang anda pilih sudah habis')
        print('------------------------------------------------------')
    elif b ==3:
        print('------------------------------------------------------')
        print('Anda memilih ukuran XL')
        print('------------------------------------------------------')

        j = int(input("Masukkan jumlah yang anda inginkan:"))
        h = j*250000
        print('------------------------------------------------------')
        print("Anda telah membeli Jaket Hoodie dengan ukuran XL berjumlah",j, "\nAnda harus membayar sebesar: Rp.",h)
        print('------------------------------------------------------')
    elif b ==4:
        print('------------------------------------------------------')
        print('Anda memilih ukuran XXL')
        print('------------------------------------------------------')

        j = int(input("Masukkan jumlah yang anda inginkan:"))
        h = j*250000
        print('------------------------------------------------------')
        print("Anda telah membeli Jaket Hoodie dengan ukuran XXL berjumlah",j, "\nAnda harus membayar sebesar: Rp.",h)
        print('------------------------------------------------------')
    else:
        item = ['\n','!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3','4']
        for ukuran in item:
            print(ukuran)

elif x ==3:
    print('-----------------------------------------------------')
    print('Anda telah memilih Jaket Kulit dengan harga Rp.450000')
    print('-----------------------------------------------------')
    print('Daftar ukuran jaket yang tersedia')
    print('1. M')
    print('2. L')
    print('3. XL')
    c = float(input('Pilih ukuran jaket apa yang anda inginkan ='))
    if c ==1:
        print('------------------------------------------------------')
        print('Maaf stok ukuran yang anda pilih sudah habis')
        print('------------------------------------------------------')
    elif c ==2:
        print('------------------------------------------------------')
        print('Maaf stok ukuran yang anda pilih sudah habis')
        print('------------------------------------------------------')
    elif c ==3:
        print('------------------------------------------------------')
        print('Anda memilih ukuran XL')
        print('------------------------------------------------------')

        j = int(input("Masukkan jumlah yang anda inginkan:"))
        h = j*450000
        print('------------------------------------------------------')
        print("Anda telah membeli Jaket Kulit dengan ukuran XL berjumlah",j, "\nAnda harus membayar sebesar: Rp.",h)
        print('------------------------------------------------------')
    else:
        item = ['\n','!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3']
        for ukuran in item:
            print(ukuran)

else:
    item = ['\n''!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3']
    for jenis in item:
        print(jenis)
        
   

print("\n--TERIMAKASIH SUDAH MENGUNJUNGI/MEMBELI DI TOKO KAMI--\n")




>>>>>>> a20cc4f5b961071649c3be6148c5ba2643b20343



