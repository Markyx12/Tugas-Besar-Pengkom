# LIBRARY klasifikasi

# Prosedur Menampilkan Tabel Dataset
def print_dataset(array:list) -> str:
    '''Menampilkan dataset model'''
    
    # KAMUS
    # array     = array 2D [float] dataset 'model_dimensi'
    # label_x   = array 1D [str] label kolom, atau horizontal, atau sumbu x
    # label_y   = array 1D [str] label baris, atau vertikal, atau sumbu y

    # ALGORITMA

    # Inisiasi label pada tabel data
    label_x = ['pjg', 'lbr', 'tgi']
    label_y = ['Bus', 'Gol I', 'Gol II', 'Gol III', 'Gol IV', 'Gol V', 'Gol VI']

    # Print label kolom, atau label yang ditulis secara horizontal
    print('\t', end='')
    for i in label_x:
        print(i, end='\t')
    print()

    # Print label baris, atau label yang ditulis secara vertikal
    for i in range(len(array)):
        print(label_y[i], end='\t')
        # Print item di setiap baris
        for j in array[i]:
            print(j, end=' ')
        print()
    
    # return 0


# Fungsi Kopi Array Secara Mengeluruh
def absolut_copy(array:list) -> list:
    '''Mengkopi setiap elemen pada array dengan dimensi yang tidak diketahui'''
    
    # KAMUS 
    # array = array [any]

    for i in array:
        # Mengecek tipe elemen pada array. Apabila list, lakukan rekursi sedemikian sehingga didapat elemen non list
        if type(i) == list:
            return [absolut_copy(i) for i in array] # Masukkan elemen list ke dalam array baru
        else:
            return array # Masukkan elemen non list ke dalam array baru


# Fungsi Rumus Euclidean Distance
def euclidean_distance(model:list, uji:list) -> float:
    '''Mencari Euclidean distance dari dua buah array dengan jumlah dimensi yang sama'''
    
    # KAMUS LOKAL
    # model = array [float] titik data model
    # uji   = array [float] titik data uji
    # sum   = float

    # ALGORITMA
    # R = sqrt((D1f-D1i)^2 + (D2f - D2i)^2 + (D3f - D3i)^2 + ... + (Dnf - Dni)^2) 
    # dengan R:= jarak, dan Dn:= posisi pada dimensi ke-n
    
    sum = 0
    for i in range(len(uji)):
        sum += (uji[i] - model[i]) ** 2
    
    return sum ** (1/2)


# Fungsi Klasifikasi
def klasifikasi(model:list, uji:list, plotting:bool) -> str:
    '''Mengidentifikasi golongan kendaraan berdimensi 'uji' dalam bentuk list
    berdasarkan tabel model dimensi kendraan yang golongannya telah terklasifikasi'''

    # KAMUS
    # model             = array 3D [float] tabel data model dimensi kendaraan
    # uji               = array 1D [float] list data uji dimensi hasil input 
    # plotting          = bool apakah akan melakukan testing dan upgrade model
    # tabel_distansi    = array 2D [float] tabel model yang setiap elemennya diubah menjadi jarak titik tersebut ke titik uji
    # distansi          = array 1D [float] 'tabel_distansi' yang setiap golongannya sudah diwakili oleh satu titik
    # indeks            = int indeks 'distansi' yang bernilai distansi terkecil
    # golongan          = str hasil identifikasi dan klasifikasi golongan kendaraan

    # Format data model dimensi kendaraan (dalam cm)
    #               |Panjang|Lebar  |Tinggi | data dimensi kendaraan 2, 3, dst.. >>>
    # Gol I Bus     |       |       |       |
    # Gol I non Bus |       |       |       |
    # Gol II        |       |       |       |
    # Gol III       |       |       |       |
    # Gol IV        |       |       |       |
    # Gol V         |       |       |       |
    # Gol VI        |       |       |       |


    # Mencari jarak antara titik uji ke setiap titik model 
    tabel_distansi = absolut_copy(model)
    # mengubah setiap elemen menjadi euclidean distance
    for i in range(len(model)):
        for j in range(len(model[i])):
            tabel_distansi[i][j] = euclidean_distance(model[i][j], uji)


    # Mencari jarak terdekat untuk mewakili titik dari setiap golongan
    distansi = absolut_copy(tabel_distansi)
    for item in distansi:       # Mengecek apabila dataset pada baris (golongan) memiliki lebih dari satu data,
        if type(item) == list:  # pencarian jarak terdekat dilakukan pada kluster golongan terlebih dahulu.
            item = min(item)
    # Sehingga diperoleh satu titik terdekat yang mewakili setiap golongan. 


    # Mencari jarak terdekat diantara perwakilan titik tiap golongan
    indeks = distansi.index(min(distansi)) # Memanggil indeks pada array 'distansi' yang memiliki nilai minimum (jarak terdekat)


    # Mengecek apakah akan menambahkan data uji ke dataset model
    if plotting == True:
        model[indeks].append(uji) # Mengaupdate dataset


    # Klasifikasi Golongan
    if indeks == 0 or indeks == 1:
        golongan = "Golongan I"
    elif indeks == 2:
        golongan = "Golongan II"
    elif indeks == 3:
        golongan = "Golongan III"
    elif indeks == 4:
        golongan = "Golongan IV"
    elif indeks == 5:
        golongan = "Golongan V"
    elif indeks == 6:
        golongan = "Golongan VI"
    

    # Output golongan kendaraan
    return golongan