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

#membuat kelas dengan nama rumah yang berkorelasi/terhubung dengan hunian
class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, gambar):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik        #nama pemilik
        self.luas_tanah = luas_tanah            #luas tanah
        self.gambar = gambar                    #gambar

    #get dokumen
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    #get nama pemilik
    def get_nama_pemilik(self):
        return self.nama_pemilik

    #get luas tanah
    def get_luas_tanah(self):
        return self.luas_tanah

    #get detail
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Tanah : " + self.luas_tanah + "\n"

    #get gambar
    def get_gambar(self):
        return self.gambar