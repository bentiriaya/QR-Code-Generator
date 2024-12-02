from tkinter import *
import qrcode
from PIL import Image, ImageTk  # Correct import from Pillow
import os

root = Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#d8d8ff")
root.resizable(False, False)

# Icon image
image_icon = PhotoImage(file="icone.png")
root.iconphoto(False, image_icon)

def generateQRCode():
    name = title.get()
    text = entry.get()

    if not name or not text:
        result_label.config(text="Error: Title and Text are required!", fg="red")
        return

    try:
        # Create a directory for QR codes
        current_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(current_dir, "qrcodes")
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Generate and save the QR code
        qr = qrcode.make(text)
        filepath = os.path.join(folder, f"{name}.png")
        qr.save(filepath)

        result_label.config(text=f"QR Code saved in: {filepath}", fg="green")
        print(f"QR Code saved in: {filepath}")

        # Load and resize the image before displaying it
        pil_image = Image.open(filepath)
        pil_image = pil_image.resize((200, 200))  # Resize to 200x200 pixels
        tk_image = ImageTk.PhotoImage(pil_image)

        # Update the displayed image
        global Image_display
        Image_display = tk_image
        Image_view.config(image=Image_display)

    except Exception as e:
        result_label.config(text=f"Error saving QR Code: {e}", fg="red")
        print(f"Error: {e}")

# User interface
Image_view = Label(root, bg="#d8d8ff")
Image_view.pack(padx=50, pady=10, side=RIGHT)

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
