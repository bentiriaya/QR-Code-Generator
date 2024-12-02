from tkinter import *
import qrcode

root=Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#d8d8ff")
root.resizable(False,False)
def generateQRCode():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save()
    

Label(root,text="Title",fg="black",bg="#d8d8ff",font=15).place(x=50,y=150)
title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=250)


Button(root,text="Generate",width=20,height=2,bg="black",fg="white",command=generateQRCode).place(x=50,y=300)
root.mainloop()
