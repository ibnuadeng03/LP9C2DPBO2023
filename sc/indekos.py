''' 
	Saya Ibnu Adeng Kurnia NIM 2101769 mengerjakan latihan ke-9 
	dalam mata kuliah desain dan pemrograman berorientasi objek C2 2023
	untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. 
	Aamiin.
'''

'''  
    Design ini disusun dan/atau digunakan hanya untuk lingkungan sendiri.
	Tidak untuk menjadi konsumsi/kepentingan umum.
	Hanya untuk melengkapi tugas DPBO 2023.
'''

#import file
from hunian import Hunian

#membuat kelas dengan nama indekos yg terhubung dengan/berkorelasi dengan hunia
class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, harga_per_bulan, gambar):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik            #nama pemilik
        self.nama_penghuni = nama_penghuni          #nama penghuni
        self.harga_per_bulan = harga_per_bulan      #harga sewa tiap bulan
        self.gambar = gambar                        #gambar

    #get dokumen
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    #get nama kepemilikan
    def get_nama_pemilik(self):
        return self.nama_pemilik

    #get nama yg menghuni
    def get_nama_penghuni(self):
        return self.nama_penghuni

    #get harga sewa tiap bulan
    def get_harga_per_bulan(self):
        return self.harga_per_bulan

    #get detail 
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nPenghuni : " + self.nama_penghuni + "\nHarga per Bulan : " + str(self.harga_per_bulan) + "\n"

    #get gambar
    def get_gambar(self):
        return self.gambar