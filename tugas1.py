class fisika:
    def menu(self):
        menu = """
>>>MENU fisika<<<
Hi, saya adalah Doni, akan membantumu mengerjakan soal Fisika. Silakan pilih salah satu (dengan angka):
[1] menghitung kecepatan
[2] menghitung energi kinetik
[3] menghitung energi potensial
[4] keluar
        """
        return menu
    def menghitung_kecepatan(self, jarak, waktu):
        hasil = float(jarak)/float(waktu)
        return hasil
    def menghitung_ek(self, massa, kecepatan):
        hasil = 0.5 * float(massa) * float(kecepatan)**2
        return hasil 
    def menghitung_ep(self, massa, gravitasi, tinggi):
        hasil = float(massa) * float(gravitasi) * float(tinggi)
        return hasil
 
while True:
    print(fisika().menu())
    pilih = input("Saya pilih nomor :")
    if pilih == "1":
        print("Oke Bos, Doni akan menghitung kecepatan")
        while True:
            benda = input("masukkan nama benda :")
            jarak = input("masukkan jarak (dalam meter) :")
            waktu = input("masukkan waktu (dalam sekon) :")
            hasil_kecepatan = f"besar kecepatan yang diperlukan {benda} untuk menempuh jarak {jarak} meter selama {waktu} sekon adalah {fisika().menghitung_kecepatan(jarak, waktu)} m/s"
            print(hasil_kecepatan)
            print("[1] Lagi \n[2] Kembali")
            pilih2 = input("Saya pilih :")
            if pilih2 == "1": continue
            else: break
 
    elif pilih == "2":
        print("Oke Bos, Doni akan menghitung energi kinetik")
        while True:
            benda = input("masukkan nama benda :")
            massa = input("masukkan massa (dalam Kg) :")
            kecepatan = input("masukkan kecepatan (dalam m/s) :")
            hasil_ek = f"energi kinetik {benda} dengan {massa} Kg dengan kecepatan {kecepatan} m/s adalah {fisika().menghitung_ek(massa=massa, kecepatan=kecepatan)} joule"
            print(hasil_ek)
            print("[1] Lagi \n[2] Kembali")
            pilih2 = input("Saya pilih :")
            if pilih2 == "1": continue
            else: break
 
    elif pilih == "3":
        print("Oke Bos, Doni akan menghitung energi potensial")
        while True:
            benda = input("masukkan nama benda :")
            massa = input("masukkan massa (dalam Kg) :")
            gravitasi = input("masukkan gravitasi (dalam m/s^2) :")
            tinggi = input("masukkan tinggi (dalam meter) :")
            hasil_ep = f"energi potensial {benda} dengan {massa} Kg dan ketinggian {tinggi} meter adalah {fisika().menghitung_ep(massa=massa, gravitasi=gravitasi, tinggi=tinggi)} joule"
            print(hasil_ep)
            print("[1] Lagi \n[2] Kembali")
            pilih2 = input("Saya pilih :")
            if pilih2 == "1": continue
            else: break
    else: break
