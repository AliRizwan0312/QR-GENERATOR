import qrcode
from tkinter import *

root = Tk()
root.title("QR Code Generator")
root.geometry("600x410")
root.config(background="#90be6d")
root.resizable(False, False)

def generate():
    name =a1.get()
    Text =a2.get()
    qr=qrcode.make(Text)
    #qr.save("qrcode1/"+str(name)+".png")
    fileDir=a4.get()+'\\'+a1.get() #Getting the  directoryhere the file has to be save
    qr.save(f'{fileDir}.png')
# Create title label
title_label = Label(root, text="Enter Name", fg="white", bg="#90be6d", font=("Arial", 25))
title_label.pack(pady=5, padx=10)
a1 = Entry(root, width=28, font=("Arial", 15))
a1.pack(padx=0, pady=10)


# Create input field
title_label1 = Label(root, text="Enter link", fg="white", bg="#90be6d", font=("Arial", 25))
title_label1.pack(pady=0, padx=10,)

a2 = Entry(root, width=28, font=("Arial", 15))
a2.pack(padx=10, pady=20)

title_label2 = Label(root, text="Enter the location to save", fg="white", bg="#90be6d", font=("Arial", 25))
title_label2.pack(pady=0, padx=15,)

a4 = Entry(root, width=28, font=("Arial", 15))
a4.pack(padx=20, pady=25)


a3 = Button(root,text="Generate",width=20,height=2,background="black",fg="white",command=generate)
a3.pack(padx=10,pady=10)



title_label2 = Label(root, text="Empower Edge Solution", fg="white", bg="#90be6d", font=("Arial", 10),anchor="e")
title_label2.pack(side="right")


root.mainloop()
