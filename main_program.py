# ===== PROGRAM Gardu Tol Otomatis =====
# Mensimulasikan sistem kerja gardu tol otomatis dengan menggunakan program python

# ===== IMPORT FUNCTION=====
from subprogram_klasifikasi import *
from subprogram_rfid import *
from subprogram_transaksi import *
from subprogram_report import *
from subprogram_ui_ux import *
from datetime import *

# ===== KAMUS LOKAL =====
# antrian_kendaraan     = array kendaraan yang mengantri memasuki gardu tol. Ada yang berisi data (pakai RFID), ada yang tidak.
# kendaraan_masuk       = array kendaraan yang memasuki gardu tol. Dapat memiliki data (pakai RFID), dapat pula tidak. 
# database              = array [dict] data kendaraan yang memasuki gardu tol
# dataset               = array data model dimensi kendaraan untuk machine learning subprogram klasifikasi. 
# plotting              = bool apakah data uji akan ditambahkan ke data model pada machine learning subprogram klasifikasi. 
# urutan                = int antrian kendaraan ke-
# kalender              = str tanggal
# user                  = str jawaban pilihan menu user
# menu_user             = str jawaban pilihan menu user as staff
# menu_dataset          = str jawaban pilihan menu user as staff to check dataset
# is_rfid               = bool apakah menggunakan rfid
# dimensi_kendaraan     = array [p, l, t] int dimensi kendaraan terukur oleh AVC
# nomor_polisi          = str nomor polisi terbaca oleh AVC
# golongan_kendaraan    = str golongan kendaraan
# data                  = dict data kendaraan yang memasuki gardu tol, yang akan dimasukkan ke database

# ===== SIMULASI =====
# format data RFID = [Nama, nomor polisi, golonagn, saldo rekening, jarak tempuh]
antrian_kendaraan = [ [], ["Udin", "B 1945 AG", "Golongan I", 500500, 350], [], [], ["Asep", "D 2371 HS", "Golongan V", 2000000000, 890], ["Made", "DK 2489 ST", "Golongan II", 7000000, 500], [], [] ]
kendaraan_masuk = []

# ===== DATABASE DAN DATASET =====
database = []

dataset = [[[  1500.0,   255.0,    390.0]],
           [[  470.0,    180.0,    145.0]],
           [[  800.0,    235.0,    300.0]],
           [[  1300.0,   260.0,    350.0]],
           [[  1100.0,   270.0,    375.0]],
           [[  1800.0,   275.0,    415.0]],
           [[  200.0,    75.0,     125.0]]]

# ===== ALGORITMA =====

# Inisiasi nilai awal
plotting = False
urutan = 0
kalender = datetime.now().strftime("%x")

starter("Mau simulasi pakai apa?\n")
cara_simulasi = menu("Jarak", "Gerbang Tol")

# Program diulang terus menerus sampai di-exit oleh user atau antrian habis
while urutan < len(antrian_kendaraan):
    
    # Inisiasi kendaraan masuk
    kendaraan_masuk = antrian_kendaraan[urutan]

    # User Interface
    starter("Memulai Program\n")
    user = menu("Staff", "Driver")

    # User sebagai Staff
    if user == "1":
        starter("Silakan pilih akses\n")
        menu_user = menu("Dataset", "Database")

        # Menu dataset
        if menu_user == "1":
            starter("Mengakses Dataset\n")
            menu_dataset = menu("Lihat dataset", "Atur plotting")
            
            # Lihat dataset
            if menu_dataset == "1":
                starter("Dataset Automatic Vehicle Classifier\n")
                print_dataset(dataset)                

            # Atur plotting
            elif menu_dataset == "2":
                starter("Silakan atur konfigurasi\n")
                plotting = bool(menu("True (fill anything)", "False (press 'Enter')"))

            # Terminasi
            print()
            if is_terminate(): break
            else: continue

        # Report database
        elif menu_user == "2":
            # Menampilkan database
            starter("Mengakses Database\n")
            report(database=database)
            
            # Terminasi
            if is_terminate(): break
            else: continue       

    # User sebagai Driver
    elif user == "2": # kendaraan masuk area gardu tol
        
        # Menambah data baru di database
        database.append({})

        starter()
        input(">> Kendaraan Memasuki Area Gardu Tol")
        input("\n>> Mencoba mendeteksi RFID")

        # Menjalankan RFID apabila terdeteksi
        is_rfid = RFID(kendaraan=kendaraan_masuk, tgl=kalender, data=database[-1])
        
        if is_rfid:
            golongan_kendaraan = database[-1]["Golongan"]

        # Tap cash apabila tidak pakai RFID
        if not is_rfid:
            input("\n>> Mengaktifkan AVC")

            # AVC dijalankan dan mulai menginput data ke sistem gardu tol
            starter("Memulai Identifikasi kendaraan\n")
            dimensi_kendaraan = [0, 0, 0]
            nomor_polisi            =         input(" >> Nomor Polisi terbaca  : ")
            dimensi_kendaraan[0]    =   float(input(" >> Panjang terbaca (cm)  : "))
            dimensi_kendaraan[1]    =   float(input(" >> Lebar terbaca (cm)    : "))
            dimensi_kendaraan[2]    =   float(input(" >> Tinggi terbaca (cm)   : "))
            
            # Update database
            database[-1].update({"Nomor Polisi":nomor_polisi})
            
            # Proses klasifikasi dengan metode K-Nearest Neigbor
            golongan_kendaraan = klasifikasi(model=dataset, uji=dimensi_kendaraan, plotting=plotting)
            
            input("\nIdentifikasi kendaraan berhasil")
        
        # Proses Transaksi
        starter()
        input(">> Memulai proses transaksi")
        data = transaksi(gol=golongan_kendaraan, rfid=is_rfid, tgl=kalender, database=database, mode=cara_simulasi)
        
        # Antrian kendaraan berlanjut
        urutan += 1

        # Update database
        database[-1].update(data)

        # Terminasi
        if is_terminate(): break
        else: continue 

# Program berakhir
input("\nSimulasi Berakhir")