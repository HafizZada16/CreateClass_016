class persegipanjang:
    def __init__(self, panjang, lebar): # Membuat Konstruktor Persegi Panjang
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self): # Menghitung Panjang
        return 2 *(self.panjang + self.lebar)
    
    def luas(self): # Menghitung Luas
        return self.panjang * self.lebar
    
    def __str__(self): # Untuk menampilkan string object Persegi Panjang yg diinput
        return f"persegi panjang, panjang {self.panjang} cm, lebar {self.lebar} cm"
    
def main():
    try:
        # Input Panjang & Lebar
        panjang = int(input("Masukkan panjang : "))
        lebar = int(input("Masukkan lebar : "))
        
        # Membuat objek persegi panjang
        pp = persegipanjang(panjang, lebar)

        # Validasi nilai panjang dan lebar
        if panjang <= 0 or lebar <= 0:
            print("Nilai jangan negatif!") # Jika yg diinput negatif
            return
    
    except:
        print("Input tidak valid!, Masukkan Angka!") # Jika yg diinput bukan angka
        return

    print(pp)  # Output Hasil persegi panjang
    print("Keliling:", pp.keliling(), "cm")
    print("Luas:", pp.luas(), "cm²")

main()

#self untuk tiap objek punya nilai berbeda & akses parameter