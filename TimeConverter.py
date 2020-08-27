import math

def konversi(detik):  # function konversi dengan parameter detik
    if type(detik) == int and detik >= 0 and detik <= 359999:# kondisi dimana detik adalah tipe int dan lebih besar dari 0 (bermakna positif tidak boleh negatif), dan maksimal value 359999
        detik = math.floor(detik %(24 * 3600))  # variabel detik dimana di konversi kan terhadap detik per jam (24 jam dikali 3600 detik)
        jam = detik // 3600          # variabel detik di konversikan terhadap jam
        detik %= 3600                
        menit = math.floor(detik // 60 )         # variabel menit dimana konversi menit terhadap detik
        detik %= 60
        return "%d:%02d:%02d"% (jam, menit, detik)
    
    else:
        print("invalid input")

konversi(3600)  # memanggil fungsi dengan isi parameternya