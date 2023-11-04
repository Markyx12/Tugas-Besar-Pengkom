# SUBPROGRAM REPORT
# Menampilkan Database ke Layar

from subprogram_ui_ux import starter

# Prosedur report
def report(database:list) -> None:
    '''Menampilkan database ke layar'''

    # KAMUS LOKAL
    # database      = list database
    # akun          = str pemilik kendaraan
    # tanggal       = str tanggal
    # golongan      = str golongan kendaraan
    # harga         = int tarif toll
    # saldo_akhir   = int sisa saldo rekening
    # nomor_polisi  = str nomor polisi

    # ALGORITMA

    starter("Laporan Kendaraan Masuk Gardu Tol\n")
    for i in range(len(database)):
        
        # Mengakses database
        akun            = database[i]["Nama"]
        tanggal         = database[i]["Tanggal"]
        golongan        = database[i]["Golongan"]
        harga           = database[i]["Tarif"]
        saldo_akhir     = database[i]["Saldo"]
        nomor_polisi    = database[i]["Nomor Polisi"]

        # Menampilkan database
        print(f"Tanggal     : {tanggal}")
        print(f"Nomor polisi: {nomor_polisi}")
        print(f"Atas nama   : {akun}")
        print(f"Golongan    : {golongan}")
        print(f"Tarif       : {harga}")
        print(f"Saldo       : {saldo_akhir}")
            
        print()

        # return 0