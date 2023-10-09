# Posttest_Python#mengimport pretty table
from prettytable import PrettyTable

# menamai table & mengisi field table
table = PrettyTable()
table.field_names = ["No","Layanan","Harga"]

#inisialisasi
struktur = [
    {'no': 1 , 'layanan': 'Suntik Rabies', 'harga': 'Rp.150.000'},
    {'no': 2 , 'layanan': 'Suntik Vaksin', 'harga': 'Rp.100.000'},
    {'no': 3 , 'layanan': 'Suntik Scabies', 'harga': 'Rp.150.000'},
    {'no': 4 , 'layanan': 'Tindakan Operasi', 'harga': 'Rp.450.000'},
    {'no': 5 , 'layanan': 'Cabut Gigi', 'harga': 'Rp.200.000'},
    {'no': 6 , 'layanan': 'Check Up', 'harga': 'Rp.100.000'}
]

#untuk menambahkan data kedalam row
for i in struktur:
    table.add_row([i['no'], i['layanan'], i['harga']])

#fungsi-fungsi
def menambahkan():
    no = int(input("Nomor: "))
    layanan = input("Layanan: ")
    harga = input("harga: ")

    #proses tambah data
    table.add_row([no, layanan ,harga])
    print(f"Layanan telah ditambahkan!")
    print()

def menampilkan():
    #proses menampilkan data
    print(table)
    print()

def update():
    no = int(input("Nomor: "))
    layanan = input("Layanan: ")
    harga = input("harga: ")

    #proses mengupdate data
    for row in table.rows:
        if  int(row[0]) == no:
            row[1] = layanan
            row[2] = harga
            print(f"Layanan telah diperbarui!")
            print()
            return

def delete():
        no = int(input("Nomor: "))

        #proses menghapus data
        for row in table.rows:
            if int(row[0]) == no:
                table._rows.remove(row)
                print(f"Layanan {no} telah dihapus!")
                print()
                return 
            
#fungsi tampilan data dan inputan visitor
def data():
    print()
    pemilik = input("Nama Pemilik: ")
    alamat  = input("Alamat Pemilik: ")
    wa      = int(input("No Handphone: "))
    peliharaan = input("Nama peliharaan: ")
    jenis = input("Jenis peliharaan: ")
    tanggal = input("Hari/tanggal: ")
    isi = input("Layanan Nomor: ")
    print()

    #tampilan
    print(f"Pemilik {pemilik}, Alamat {alamat}, nomor yang dapat dihubungi {wa}, {peliharaan} jenis {jenis}, layanan {isi} dengan drh.Nindya Pramudita")
    print()
    print(f"Hari/tanggal: {tanggal}")
    print(f"Terkonfirmasi")          
    print(f"Biaya sudah termasuk obat!")
    print()
    print("Terima kasih dan Cepat sembuh")
    print("Nomor anda akan dihubungi ketika masuk waktu pemeriksaan!")
    print("bertanda tangan: drh.Nindya Pramudita")
    print()

def keluar():
    print("Anda Keluar!")
    print()




print()
print("-----Welcome To The Animal Clinic-----")
print()

#Memilih akan pergi ke menu dokter/pengunjung
pilih = input("Please select as (visitor/doctor)?: ")

#jika dokter
if pilih == "doctor":
        email_1 = "nindya@gmail.com" #harus masuk menggunakan email ini
        password_1 = 250524 #harus masuk menggunakan password ini
        email = input("Masukkan Email anda   : ")
        password = int(input("Masukkan Password Anda: "))
        if email == email_1 and password == password_1: #proses apakah passwornya sudah benar atau belum
            print("Selamat Datang drh.Nindya Pramudita") #jika benar
            print()

            #tampilan menu dokter
            while True:
                print("========Doctor========")
                print("1. Menambahkan Data")
                print("2. Menampilkan Data")
                print("3. Update Data")
                print("4. Delete Data")
                print("======================")
                crud = int(input("Pilih 1/2/3/4: "))
                print()

                if crud == 1:
                    menambahkan() #fungsi yang sudah dibuat di atas, tinggal dipanggil saja
                elif crud == 2:
                    menampilkan() #fungsi yang sudah dibuat di atas, tinggal dipanggil saja
                elif crud == 3:
                    update()    #fungsi yang sudah dibuat di atas, tinggal dipanggil saja
                elif crud == 4:
                    delete()    #fungsi yang sudah dibuat di atas, tinggal dipanggil saja
                else:
                    print("Invalid!!!")
                    break
        else:
            print("Email atau password anda salah!!!") #jika salah

#jika pengunjung
elif pilih == "visitor":
    print(table)
    print()

    #menu pengunjung
    while True:
        print("========Visitor=========")
        print("1. Tampilkan Data")
        print("2. Janjian Dengan Dokter")
        print("3. Keluar")
        print("========================")
        crud = int(input("Pilih 1/2/3: "))
        print()

        if crud == 1:
            menampilkan() #fungsi yang sudah dibuat di atas, tinggal dipanggil saja
        elif crud == 2:
            data() #fungsi yang sudah dibuat di atas, tinggal dipanggil saja
        elif crud == 3:
            keluar()#fungsi yang sudah dibuat di atas, tinggal dipanggil saja
            break
        else:
            print("Invalid!!!")

else:
    print("Error")
