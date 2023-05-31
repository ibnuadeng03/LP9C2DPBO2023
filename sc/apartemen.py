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

# membuat kelas dengan nama apartemen yang berkorelasi dengan hunian
class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, fasilitas, gambar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik        #nama pemilik
        self.fasilitas = fasilitas              #fasilitas
        self.gambar = gambar                    #gambar/foto

    #get dokumen
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a.n " + self.nama_pemilik + "."

    #get nama pemilik
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    #get fasilitas
    def get_fasilitas(self):
        return self.fasilitas
    
    #get detail
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nFasilitas : " + self.fasilitas + "\n"
    
    #get gambar
    def get_gambar(self):
        return self.gambar