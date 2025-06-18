# Database Dummy

dataBuku = {
    "Judul": [
        "Matematika", "Informatika", "Analisis", "Kesenian", "5 Cara Diet Paling Ampuh", "Pengolahan Citra Digital", "Kecerdasan Tiruan", "Laskar Pelangi", "Sistem Basis Data" , "Logika Matematika", "Pemodelan Matematika"# Tidak ada aturan pada penulisan judul selain tidak boleh berupa karakter kosong
    ],
    "Penulis": [
        "Andre", "Budi", "Ahmad", "James", "Sulthan", "Dwi Ratna S.", "Prof. Isa Irawan, MT.", "Andrea Hirata", "Budi Setiyono", "Gifary Divandra N.", "Prof. Choirul Imron, M.Si"# Tidak boleh ada angka dalam penulis, boleh menggunakan titik dan koma
    ],
    "Tahun Terbit": [
        '2005', '2014', '2009', '2018', '2011', '2011' , '2018', '2005', '2009', '2018', '2023'# Tahun terbit harus berada di antara tahun 1800 hingga tahun 2025 
    ],
    "ISBN": [
        '9789793062797', '9786021408450', '9789794335005', '9780735211292', '9780062316097', '9783458792592', '9738245926038', '9738573583752', '9783482746432', '9747263847632', '9794837264212' # ISBN harus terdiri dari 13 digit dan lebih dari nol
    ],
    "Kategori": [
        "Sains", "Sains", "Sains", "Sastra", "Kesehatan", "Sains", "Sains", "Novel", "Sains", "Sains", "Sains" # Kategori harus ada di dalam list kategori yang tersedia
    ],
    "Stock Buku": [
        '0','9','8','1','4','5','6','4','2','1', '2' # Harus digit positif
    ]
}
listKategori = ["Fiksi", "Sejarah", "Puisi", "Novel", "Biografi", "Agama", "Drama", "Horror", "Komik", "Fantasi", "Resep", "Bisnis", "Sastra", "Sains"] # Harus alphabet


# Fungsi Untuk Menampilkan Dashboard
def menuutama():
    print("\n\n==========Data Peminjaman Buku Di Perpustakaan==========\n")
    print("1. Lapran Data Buku Perpustakaan")
    print("2. Menambahkan Koleksi Buku")
    print("3. Mengubah Data Koleksi Buku")
    print("4. Menghapus Koleksi Buku")
    print("5. Exit\n")
    print("Silahkan Pilih Menu [1-5] ")

def menu1(): #SubMenu1
    print("\n\n==========Data Record Peminjaman Buku Di Perpustakaan==========\n")
    print("1. Laporan Seluruh Data Buku")
    print("2. Cari Buku Berdasarkan ISBN")
    print("3. Cari Buku Berdasarkan Kategori Tertentu")
    print("4. Cari Buku Berdasarkan Tahun Terbit Tertentu")
    print("5. Kembali Ke Menu Utama\n")
    print("Silahkan Pilih Menu [1-5] ")


def menu2(): #SubMenu2
    print("\n\n==========Menambahkan Data Peminjaman Buku Di Perpustakaan==========\n")
    print("1. Tambahkan Koleksi Buku")
    print("2. Kembali Ke Menu Utama\n")
    print("Silahkan Pilih Menu [1-2] ")

def menu3(): #SubMenu3
    print("\n\n==========Memperbarui Data Peminjaman Buku Di Perpustakaan==========\n")
    print("1. Perbarui Data Koleksi Buku")
    print("2. Kembali Ke Menu Utama\n")
    print("Silahkan Pilih Menu [1-2] ")

def menu4(): #SubMenu4
    print("\n\n==========Menghapus Data Peminjaman Buku Di Perpustakaan==========\n")
    print("1. Hapus Koleksi Buku")
    print("2. Kembali Ke Menu Utama\n")
    print("Silahkan Pilih Menu [1-2] ")


# Fungsi yang sering digunakan berkali-kali
def input_menu():
    menu_pilihan = input("Masukkan menu yang ingin dipilih : ")
    print(f"Menu yang dipilih : {menu_pilihan}")
    return menu_pilihan


def tidakValid():
    print("Pilihan Tidak Valid. Silahkan Pilih Lagi")
    

def header():
    print("=" * 147)
    print(f"||  {'No':<3}||  {'Judul':<30}||  {'Penulis':<25}||  {'Tahun Terbit':<13}||  {'Kategori':<20}||  {'ISBN':<15}||  {'Stock Buku':<11}||")
    print("=" * 147)

def tampilkanData(i):
    print(f"||  {i+1 :<3}||  {dataBuku['Judul'][i] :<30}||  {dataBuku['Penulis'][i] :<25}||  {dataBuku['Tahun Terbit'][i] :<13}||  {dataBuku['Kategori'][i]:<20}||  {dataBuku['ISBN'][i]:<15}||  {dataBuku['Stock Buku'][i]:<11}||")


#Fungsi SubMenu1
def fitur1a():
    n = len(dataBuku['ISBN'])
    header()
    for i in range(n):
        tampilkanData(i)
    print("=" *147)

def fitur1b():
    while True:
        
        print(f"ISBN buku yang tersedia : {dataBuku['ISBN']}\n")
        cariBuku = input("Masukkan ISBN buku yang ingin dicari : ")
        
       
        if cariBuku in dataBuku['ISBN']:
            i = dataBuku['ISBN'].index(cariBuku)
            header()
            tampilkanData(i) 
            print("=" *147)
            break
        else:
            tidakValid()
            continue

def fitur1c():
    while True:
        print(f"Kategori Buku yang tersedia : {listKategori}")
        carikategori = input("Masukkan Kategori Buku Yang Ingin Dicari : ").title()

        if carikategori in dataBuku['Kategori']:
            header()
            for i in range(len(dataBuku['Kategori'])):
                if carikategori == dataBuku['Kategori'][i]:
                    tampilkanData(i)
                    print("=" *147)
            break
        else:
            tidakValid()
            continue


def fitur1d():
    while True:
        caritahun = input("Cari Buku Berdasarkan Tahun Terbit : ")

        if caritahun in dataBuku['Tahun Terbit']:
            header()
            for i in range(len(dataBuku['Tahun Terbit'])):
                if caritahun == dataBuku['Tahun Terbit'][i]:
                    tampilkanData(i)
                    print("=" *147)
            break
        else:
            tidakValid()
            continue



def fitur1():
    while True:
        menu1()
        menu_pilihan = input_menu()
        if menu_pilihan == '1':
            fitur1a()
            continue
        elif menu_pilihan == '2':
            fitur1b()
            continue
        elif menu_pilihan == '3':
            fitur1c()
            continue
        elif menu_pilihan == '4':
            fitur1d()
            continue
        elif menu_pilihan == '5':
            break

        else:
            tidakValid()
            continue
    

#Fungsi SubMenu2
def fitur2a(): 
    while True:
        
        isbnBaru = input(f"Masukkan ISBN Dari Buku tersebut.")
        
        if isbnBaru in dataBuku['ISBN']: # Memastikan ISBN baru tidak ada dalam ISBN yang sudah terdaftar
            judulterdaftar = dataBuku['ISBN'].index(isbnBaru)
            print(f"ISBN telah terdaftar dengan judul {dataBuku['Judul'][judulterdaftar]}.")
            continue
        elif isbnBaru.isdigit() and len(isbnBaru) == 13: # Memastikan ISBN yang ingin didaftarkan berupa 13 digit angka
            if int(isbnBaru) <= 0:
                tidakValid()
                continue
            dataBuku['ISBN'].append(isbnBaru)
            break
        else:
            tidakValid()
            continue

    while True:
        judulBaru = input("Masukkan Judul Buku Yang Ingin Ditambahkan : ")
        if not judulBaru.strip() : # Memastikan judul yang diinput bukan karakter kosong
            tidakValid()
            continue
        else: 
            dataBuku['Judul'].append(judulBaru.title())
            break
        

    while True:
        penulisBaru = input(f"Masukkan Nama Penulis Dari Buku {judulBaru} tersebut: ")
        if all(c.isalpha() or c.isspace() or (c in ',.')for c in penulisBaru) and penulisBaru.strip(): # Memastikan input yang diterima hanya alphabet, spasi, dan bukan karakter kosong.
            dataBuku['Penulis'].append(penulisBaru.title())
            break
        else:
            tidakValid()
            continue
            

    while True:
        tahunterbitBaru = input(f"Masukkan Tahun Terbit Dari Buku {judulBaru} tersebut")
        if tahunterbitBaru.isdigit():
            tahunterbitint = int(tahunterbitBaru)
            if 1800 <= tahunterbitint <= 2025:
                dataBuku['Tahun Terbit'].append(tahunterbitBaru)
                break
            else:
                tidakValid()
                continue  
        else:
            tidakValid()
            continue

    while True:
        print(f"Kategori Buku yang tersedia : {listKategori}")
        kategoribaru = input(f"Masukkan Kategori Dari Buku {judulBaru} tersebut.")
        if kategoribaru.title() in listKategori:
            dataBuku['Kategori'].append(kategoribaru.title())
            break
        else:
            tidakValid()
            continue
    
    while True:
        stockBaru = input(f"Masukkan Jumlah Stock Dari Buku {judulBaru}")
        if stockBaru.isdigit():
            dataBuku['Stock Buku'].append(stockBaru)
            break
        else:
            tidakValid()
            continue

    fitur1a()


def fitur2():
    while True:
        menu2()
        menu_pilihan = input_menu()

        if menu_pilihan == '1':
            fitur2a()
            continue
        elif menu_pilihan == '2' : #Exit
            break
        else:
            tidakValid()
            continue

#Fungsi SubMenu3
def fitur3a():
    while True:
        print(f"{dataBuku['ISBN']}")
        input_ISBN = input('Masukkan ISBN buku yang ingin diupdate : ')
        if input_ISBN not in dataBuku['ISBN']:
            tidakValid()
            continue
        else:
            i = dataBuku['ISBN'].index(input_ISBN)
            print(f"Buku yang ingin diupdate adalah {dataBuku['Judul'][i]}")
            break
    while True:
        konfirmasi = input(f"Apakah anda yakin ingin mengupdate data dari buku {dataBuku['Judul'][i]} [ya/tidak]").lower()
        if konfirmasi == 'tidak':
            break
        elif konfirmasi == 'ya':
    
            while True:
                input_update = input("Masukkan kolom yang ingin diupdate [Judul, Penulis, Tahun Terbit, Kategori, Stock Buku]").title()
                if input_update not in dataBuku:
                    tidakValid()
                    continue
                elif input_update.upper() == 'ISBN':
                    print("ISBN sebagai primary key tidak boleh diganti")
                    continue
                else:
                    
                    break
            
            
            if input_update == 'Judul':
                while True:
                    x = input(f"Masukkan value baru dari {input_update} dari {dataBuku['Judul'][i]}")
                    if x.strip():
                        
                        break
                    else:
                        tidakValid()
                        continue

            elif input_update.title() == 'Penulis':
                while True:
                    x = input(f"Masukkan value baru dari {input_update} dari {dataBuku['Judul'][i]}")
                    if all(c.isalpha() or c.isspace() or (c in ',.')for c in x) and x.strip():
                        
                        break
                    else:
                        tidakValid()
                        continue

            elif input_update.title() == 'Tahun Terbit':
                while True:
                    x = input(f"Masukkan value baru dari {input_update} dari {dataBuku['Judul'][i]}")
                    if x.isdigit():
                        tahunterbitint = int(x)
                        if 1800 <= tahunterbitint <= 2025:
                            break
                        else:
                            tidakValid()
                            continue
                        
                    else:
                        tidakValid()
                        continue

            elif input_update.title() == 'Kategori':
                while True:
                    print(f"Berikut adalah list kategori : {listKategori}")
                    x = input(f"Masukkan value baru dari {input_update} dari {dataBuku['Judul'][i]}")
                    if x in listKategori:
                        
                        break
                    else:
                        tidakValid()
                        continue

            elif input_update.title() == 'Stock Buku':
                while True:
                    x = input(f"Masukkan value baru dari {input_update} dari {dataBuku['Judul'][i]}")
                    if x.isdigit():
                        
                        break
                    else:
                        tidakValid()
                        continue

            while True:
                konfirmasi2 = input(f"Apakah anda yakin ingin mengupdate {input_update.title()} dari buku {dataBuku['Judul'][i]}? [ya/tidak]").lower()
                if konfirmasi2 == 'ya':
                    dataBuku[input_update][i] = x.title()
                    print(f"{input_update.title()} telah diperbarui menjadi {x}")
                    break
                elif konfirmasi2 == 'tidak':
                    print("Data tidak jadi diupdate")
                    break
                else:
                    tidakValid()
                    continue
            break
        else:
            tidakValid()
            continue
    
        
    fitur1a()



def fitur3():
    while True:
        menu3()
        menu_pilihan = input_menu()

        if menu_pilihan == '1':
            fitur3a()
            continue
        elif menu_pilihan == '2' :
            break
        else:
            tidakValid()
            continue


# Fungsi SubMenu4
def fitur4a():
    while True:
        input_ISBN = input("Masukkan ISBN buku yang ingin dihapus : ")
        if input_ISBN not in dataBuku['ISBN']:
            tidakValid()
            continue
        else:
            break
    
    i = dataBuku['ISBN'].index(input_ISBN)
    while True:
        validasi = input(f"Apakah anda yakin ingin menghapus data dari buku {dataBuku['Judul'][i]} teresebut? [ya/tidak]").lower()
        if validasi == 'ya':
            for j in dataBuku:
                del dataBuku[j][i]
            print("Data telah terhapus\n")
            break
        elif validasi == 'tidak':
            print("Data tidak terhapus")
            break
        else:
            tidakValid()
            continue
    fitur1a()
    


def fitur4():
    while True:
        menu4()
        menu_pilihan = input_menu()

        if menu_pilihan == '1':
            fitur4a()
            continue
        elif menu_pilihan == '2' :
            break
        else:
            tidakValid()
            continue

# Fungsi Menjalankan Program
def runProgram():
    while True:
        menuutama()
        menu_pilihan = input_menu()

        if menu_pilihan == '1':
            fitur1()
            continue

        elif menu_pilihan == '2':
            fitur2()
            continue

        elif menu_pilihan == '3':
            fitur3()
            continue

        elif menu_pilihan == '4':
            fitur4()
            continue

        elif menu_pilihan == '5':
            print("Terima Kasih, Adios Bella Ciao")
            break

        else:
            tidakValid()
            continue

#Menjalankan Program
runProgram()
    
