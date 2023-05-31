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
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import Image, ImageTk

#add data
hunians = []
hunians.append(Apartemen("Nelly Joy", 5, 4, "Ruang Musik, Ruang Olahraga, Rooftop", "sc/assets/apartemen.jpg"))
hunians.append(Rumah("Sekar MK", 3, 3, "8mx7m", "sc/assets/rumah.jpg"))
hunians.append(Apartemen("Haji Kohar", 1, 4, "Ruang Olahraga, Kolam Renang, Ruang Musik", "sc/assets/apartemen2.jpg"))
hunians.append(Rumah("Satria", 3, 4, "6mx8m", "sc/assets/rumah2.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", 756200, "sc/assets/indekos.jpg"))
hunians.append(Apartemen("Hj. Tonah", 3, 4, "Ruang Rapat, Kolam Renang, Taman Cinta", "sc/assets/apartemen3.jpg"))
hunians.append(Indekos("Haji Zapar", "Neng Kokom", 455000, "sc/assets/indekos2.jpg"))
hunians.append(Rumah("Yayah Rokayah", 13, 20, "167mx114m", "sc/assets/rumah3.jpg"))
hunians.append(Indekos("Yana Trian", "Jang Eho", 375500, "sc/assets/indekos3.jpg"))

#judul
root = Tk()
root.title("Praktikum 9 DPBO Python - IAK 2023")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    #frame data residen
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # Tampilkan gambar menggunakan Label
    image = Image.open(hunians[index].get_gambar())
    image = image.resize((400, 200))
    photo = ImageTk.PhotoImage(image)
    img_label = Label(d_frame, image=photo)
    img_label.image = photo
    img_label.pack()
    img_label.grid(row=1, column=0)

    #summary
    d_summary = Label(d_frame, text="SUMMARY\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" +
                                     hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0,
                                                                                                    sticky="w")

    #button
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Tutup", command=top.destroy)
    b_close.grid(row=0, column=0)
    
#frame data seluruh residen
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

#button tambah data
b_add = Button(opts, text="Tambahkan Data", state="disabled")
b_add.grid(row=0, column=0)

#button keluar
b_exit = Button(opts, text="Keluar", command=root.quit)
b_exit.grid(row=0, column=1)

#daftar-daftar bangunan beserta info untuk selengkapnya/detailnya
for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index + 1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type_label = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type_label.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Selengkapnya ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()