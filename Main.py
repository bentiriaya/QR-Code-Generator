from tkinter import *
import qrcode
from PIL import Image
import os

root = Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#d8d8ff")
root.resizable(False, False)

def generateQRCode():
    name = title.get()
    text = entry.get()

    if not name or not text:
        result_label.config(text="Error: Title and Text are required!", fg="red")
        return

    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))

        folder = os.path.join(current_dir, "qrcodes")
        if not os.path.exists(folder):
            os.makedirs(folder)
        

        qr = qrcode.make(text)
        
        filepath = os.path.join(folder, f"{name}.png")
        qr.save(filepath)
        
        result_label.config(text=f"QR Code saved in: {filepath}", fg="green")
        print(f"QR Code saved in: {filepath}")
    except Exception as e:
        result_label.config(text=f"Error saving QR Code: {e}", fg="red")
        print(f"Error: {e}")

# Interface utilisateur
Label(root, text="Title", fg="black", bg="#d8d8ff", font=("Arial", 15)).place(x=50, y=150)
title = Entry(root, width=20, font=("Arial", 15))
title.place(x=50, y=200)

Label(root, text="Text", fg="black", bg="#d8d8ff", font=("Arial", 15)).place(x=50, y=250)
entry = Entry(root, width=30, font=("Arial", 15))
entry.place(x=50, y=300)

Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generateQRCode).place(x=50, y=350)

result_label = Label(root, text="", fg="black", bg="#d8d8ff", font=("Arial", 12))
result_label.place(x=50, y=400)

root.mainloop()
