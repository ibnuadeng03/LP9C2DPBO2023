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

#import
from tkinter import *

#landing page
root = Tk()
root.title("Landing Page - PUTR")

def open_residen_page():
    from data_residen import details
    root.destroy()

frame = Frame(root, padx=100, pady=100)
frame.pack()

#halaman awal 
title_label = Label(frame, text="Selamat Datang di Dinas PUTR Kab. Bandung", font=("Arial", 16))
title_label.pack(pady=20)

#halaman untuk selengkapnya
button = Button(frame, text="Lihat Data Residen tahun 2023", command=open_residen_page)
button.pack(pady=10)

root.mainloop()
