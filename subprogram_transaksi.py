# SUBPROGRAM transaksi
# proses transaksi

from subprogram_ui_ux import starter, menu
import os

# Fungsi Transaksi
def transaksi(gol:str, rfid:bool, tgl:str, database:list, mode:str) -> dict:
    '''Proses Transaksi'''
    
    # KAMUS LOKAL
    # gol           = str golongan kendaraan
    # rfid          = bool apakah pakai rfid
    # tgl           = str tanggal
    # databse       = array database
    # akun          = str akun rekening
    # uang          = int saldo rekening
    # jarak         = int jarak tempuh toll
    # harga         = int tarif toll
    # saldoakhir    = int sisa saldo rekening
    # data          = dict data yang akan diupdate ke database
    # tabel         = array 2D matriks tabel tarif gardu tol
    # asal          = str gardu tol masuk
    # tujuan        = str gardu tol keluar
                    
    # Apabila tidak menggunakan RFID, input secara manual
    if not rfid:
        starter("Silakan tempel kartu\n")
        akun        =     input(" >> Akun e-toll: ")
        uang        = int(input(" >> Saldo rek  : "))
        if mode == "1":
            jarak   = int(input(" >> Jarak (km) : "))
    
    # Apabila menggunakan RFID, input berdasarkan data
    else:
        input("\n>> Mengecek Saldo rekening")
        akun        = database[-1]["Nama"]
        uang        = database[-1]["Saldo"]
        if mode == "1":
            jarak   = database[-1]["Tarif"]

    # Apabila simulasi berdasarkan jarak tempuh 
    if mode == "1":
        # Menentukan harga per golongan
        if gol == "Golongan I":
            harga = int(5000 * (jarak / 10))
        elif gol == "Golongan II":
            harga = int(10000 * (jarak / 10))
        elif gol == "Golongan III":
            harga = int(15000 * (jarak / 10))
        elif gol == "Golongan IV":
            harga = int(20000 * (jarak / 10))
        elif gol == "Golongan V":
            harga = int(25000 * (jarak / 10))
        elif gol == "Golongan VI":
            harga = int(2000 * (jarak / 10))

    # Apabila Simulasi berdasarkan gerbang toll
    elif mode == "2":
        starter()
        tabel = [   ["Asal Perjalanan   ", "Tujuan Perjalanan   ",               "Gol I",        "Gol II",       "Gol III",      "Gol IV",       "Gol V",        "Gol VI"        ],
                    ["Gempol IC.        ", "Gempol JC.          ",               3000,           5000,           5000,           6000,           6000,           999999          ],
                    ["Gempol IC.        ", "Pandaan IC.         ",               11500,          19000,          19000,          24000,          24000,          999999          ],
                    ["Gempol IC.        ", "Pandaan.            ",               13000,          21500,          21500,          27000,          27000,          999999          ],
                    ["Gempol JC.        ", "Gempol IC.          ",	             3000,           5000,	         5000,	         6000,	         6000,           999999          ],
                    ["Gempol JC.        ", "Pandaan IC.         ",               3000,           14000,          14000,          18000,          18000,          999999          ],
                    ["Gempol JC.        ", "Pandaan.            ",               10000,          16500,          16500,          21000,          21000,          999999          ],
                    ["Pandaan IC.       ", "Gempol IC.          ",               11500,          19000,          19000,          24000,          24000,          999999          ],
                    ["Pandaan IC.       ", "Gempol JC.          ",               8500,           14000,          14000,          18000,          18000,          999999          ],
                    ["Pandaan IC.       ", "Pandaan.            ",               1500,           2500,           2500,           3000,           3000,           999999          ],
                    ["Pandaan.          ", "Gempol IC.          ",               13000,          21500,          21500,          27000,          27000,          999999          ],
                    ["Pandaan.          ", "Gempol JC.          ",	             10000,	         16500,	         16500,	         21000,          21000,          999999          ],
                    ["Pandaan.          ", "Pandaan IC.         ",	             1500,	         2500,	         2500,	         3000,	         3000,           999999          ]   ]  

        # Menampilkan daftar harga
        for i in range(len(tabel)):
            print(f"{tabel[i][0]}{tabel[i][1]}", end=": ")
            for j in range(2, len(tabel[i])-1):
                print(tabel[i][j], end="\t")
            print()
    
        # Meminta gerbang tol awal
        print("\nGerbang Tol Awal, ketikkan nama gerbang dengan benar!")
        asal = menu("Gempol IC", "Gempol JC", "Pandaan IC", "Pandaan")+"."

        # Meminta gerbang tol akhir
        print("\nGerbang Tol Akhir, ketikkan nama gerbang dengan benar!")
        tujuan = menu("Gempol IC", "Gempol JC", "Pandaan IC", "Pandaan")+"."

        # Mencari harga berdasarkan matriks
        for i in range(len(tabel)):
            if asal in tabel[i][0] and tujuan in tabel[i][1]:
                if gol == "Golongan I":
                    harga = tabel[i][2]
                elif gol == "Golongan II":
                    harga = tabel[i][3]
                elif gol == "Golongan III":
                    harga = tabel[i][4]
                elif gol == "Golongan IV":
                    harga = tabel[i][5]
                elif gol == "Golongan V":
                    harga = tabel[i][6]
                elif gol == "Golongan VI":
                    harga = tabel[i][7]

    # Variabel saldo akhir
    saldoakhir = uang - harga

    # User Interface
    starter("Terima kasih telah menggunakan layanan kami\n")
    print(f"Tanggal   : {tgl}")
    print(f"Atas Nama : {akun}")
    print(f"GOL       : {gol}")
    print(f"TARIF     : {harga}")
    
    if saldoakhir >= 0:
        print(f"SALDO     : {saldoakhir}")
        print("\nSelamat Jalan\n")
    
    elif saldoakhir < 0:
        saldoakhir = "TIDAK MENCUKUPI"
        print(f"Saldo tidak mencukupi")
        print("\nSilakah lakukan pembayaran secara tunai\n")

    data = {"Tanggal":tgl , "Nama":akun , "Golongan":gol , "Tarif":harga , "Saldo":saldoakhir}      

    # Memasukkan data ke database
    return data
