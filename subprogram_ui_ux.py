# LIBRARY subprogram_tambahan

import os

# Fungsi is_terminate
def is_terminate() -> bool:
    '''Mengakhiri program'''

    # KAMUS LOKAL
    # terminate = bool apakah exit?

    # ALGORITMA
    terminate = False
    if input("Do you want to exit? (y/n): ") == "y": terminate = True
    os.system('cls')
    
    # RETURN
    return terminate


# Fungsi menu
def menu(*item:str) -> str:
    '''Menampilkan menu'''

    # KAMUS LOKAL
    # item  = str pilihan 'button' pada menu
    # jwb   = str jawaban user

    # ALGORITMA
    
    print("Pilih Menu: ")
    
    # Menampilkan pilihan menu
    for i in range(len(item)):
        print(f"{i+1}. {item[i]}")
    
    # Slot memilih menu
    jwb = input("\n>> Jawaban: ")

    # RETURN
    return jwb


# Prosedur starter
def starter(*teks):
    '''Default Tampilan Program'''

    # KAMUS LOKAL
    # teks = tampilan yang akan di masukkan sebagai starter

    # ALGORITMA
    os.system('cls')
    print("\n===== PROGRAM GARDU TOL OTOMATIS =====\n")
    # Menulis kalimat pada starter
    for i in teks:
        print(i)
    
    # return 0