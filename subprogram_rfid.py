# SUBPROGRAM RFID
# Mengakses data kendaraan menggunakan RFID

# Fungsi RFID
def RFID(kendaraan:list, tgl:str, data:dict) -> bool:
    '''Mengakses data pada kendaraan menggunakan RFID'''

    # KAMUS LOKAL
    # kendaraan = list data pada kendaraan RFID 
    # tgl       = str tanggal
    # data      = dict data yang akan diupdate untuk database
    # acc       = str nama akun rekening
    # plat      = str nomor polisi
    # gol       = str golongan kendaraan
    # rek       = int saldo rekening
    # dis       = int jarak tempuh toll
    
    # ALGORITMA

    # RFID berhasil terdeteksi apabila jumlah data pada alat RFID lengkap
    if len(kendaraan) == 5:

        input("\n>> RFID Terdeteksi")

        # Mengambil data dari alat yang terpasang di kendaraan
        acc     = kendaraan[0]
        plat    = kendaraan[1]
        gol     = kendaraan[2]
        rek     = kendaraan[3]
        dis     = kendaraan[4]
    
        data.update({"Tanggal":tgl , "Nama":acc , "Golongan":gol , "Tarif":dis , "Saldo":rek, "Nomor Polisi":plat})    

        return True 
    
    # RFID tidak terdeteksi
    else:
        input("\n>> RFID tidak terdeteksi")

        return False
