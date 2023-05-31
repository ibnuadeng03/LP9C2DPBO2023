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

# membuat class dengan nama hunian
class Hunian:
    def __init__(self, jenis, jml_penghuni=1, jml_kamar=1):
        self.jenis = jenis                      #jenis
        self.jml_penghuni = jml_penghuni        #jml penghuni
        self.jml_kamar = jml_kamar              #jml kamar

    #get jenis
    def get_jenis(self):
        return self.jenis

    #get jumlah penghuni
    def get_jml_penghuni(self):
        return self.jml_penghuni

    #get jumlah kamar
    def get_jml_kamar(self):
        return self.jml_kamar

    #get dokumen
    def get_dokumen(self):
        pass

    #get summary
    def get_summary(self):
        return "Hunian " + self.jenis + ", ditempati oleh " + str(self.jml_penghuni) + " orang."

    #get detail
    def get_detail(self):
        pass

    #get gambar
    def get_gambar(self):
        return ""