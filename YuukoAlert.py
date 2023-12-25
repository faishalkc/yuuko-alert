import pygame
import tkinter as tk
from PIL import Image,ImageTk

pygame.init()
root = tk.Tk()
root.resizable(False,False)
root.geometry("250x150")
root.eval('tk::PlaceWindow . center')
root.iconbitmap("files/icon.ico")
root.title("Yuuko Alert")

canvas= tk.Canvas(root, width= 250, height= 80)
canvas.pack(padx=5, pady=5)

img= (Image.open("files/face.png"))
resized_image= img.resize((80,72), Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(10,10, anchor="nw", image=new_image)
canvas.create_text(170, 50, text="Selamat Pagi !", fill="black", font=('Segoe UI', '11'))

close = tk.Button(root, text="        OK        ", font=("Segoe UI", "10"), command=root.destroy)
close.pack(padx=5, pady=5)

my_sound = pygame.mixer.Sound('files/sound.mp3')
my_sound.play()
my_sound.set_volume(0.8)

root.mainloop()