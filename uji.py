import tkinter
from tkinter import ttk 
from tkinter import *
from tkinter.messagebox import showinfo

# inisialisasi
window = tkinter.Tk ()
window.configure(bg="red")
icon_img =PhotoImage (file='D:\\projek\\asset\\icons8-noodles-48.png')
window.iconphoto(False, icon_img)
window.geometry("400x350")
window.resizable(False,False)
window.title ("pendaftaran mukbang")

# Header
header_label = ttk.Label(window, text= "Pengisian Formulir", font=(16), background="teal", foreground="black" )
header_label.pack(pady=20)

# variabel & function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
MAKANAN_FAVORIT = tkinter.StringVar()
MINUMAN_FAVORIT= tkinter.StringVar()
TINGKAT_PEDAS = tkinter.StringVar()

# fungsi tombol
def tombol_click():
    if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not MAKANAN_FAVORIT.get() or not MINUMAN_FAVORIT.get() or not TINGKAT_PEDAS.get():
        showinfo(title="Error!", message="Mohon lengkapi semua data!")
    else:
        pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
        showinfo(title="Selamat",message=pesan)
# frame input
style = ttk.Style()
style.configure("Custom.TEntry", fieldbackground="blue")
input_frame = ttk.Frame(window)
#penempatan Grid, pack, place 
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen nama lengkap
nama_depan_Label= ttk.Label (input_frame,text="NAMA_LENGKAP:")
nama_depan_Label.pack (padx=10,fill="x",expand=True)
nama_depan_entry=ttk.Entry (input_frame,textvariable=NAMA_LENGKAP)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# komponen alamat rumah
alamat_rumah_Label= ttk.Label (input_frame,text="ALAMAT:")
alamat_rumah_Label.pack (padx=10,fill="x",expand=True)
alamat_rumah_entry=ttk.Entry (input_frame,textvariable=ALAMAT_RUMAH )
alamat_rumah_entry.pack(padx=10,fill="x",expand=True)

# komponen makanan favorit
makanan_favorit_Label= ttk.Label (input_frame,text="MAKANAN:")
makanan_favorit_Label.pack(padx=10,fill="x",expand=True)
makanan_favorit_entry=ttk.Entry(input_frame,textvariable=MAKANAN_FAVORIT )
makanan_favorit_entry.pack(padx=10,fill="x",expand=True)

# komponen minuman favorit
minuman_favorit_Label= ttk.Label (input_frame,text="MINUMAN:")
minuman_favorit_Label.pack(padx=10,fill="x",expand=True)
minuman_favorit_entry=ttk.Entry (input_frame,textvariable=MINUMAN_FAVORIT)
minuman_favorit_entry.pack(padx=10,fill="x",expand=True)

# komponen level pedas
tingkat_pedas_Label= ttk.Label (input_frame,text="Level:")
tingkat_pedas_Label.pack(padx=10,fill="x",expand=True)
tingkat_pedas_entry=ttk.Entry (input_frame,textvariable=TINGKAT_PEDAS)
tingkat_pedas_entry.pack(padx=10,fill="x",expand=True)

# tombol
Daftar = ttk.Button (input_frame, text="Daftar",command=tombol_click)
Daftar.pack(fill="x",expand=True,padx=10,pady=10)

window.mainloop()