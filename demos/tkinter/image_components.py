from tkinter import *
import os

# NOTE: This demo assumes the file "x.png" is in
# the tkinter directory

root = Tk()

Label(root, text='Image Component Demo',
      font=('Verdana', 15)).pack(side=TOP, pady=10)

# LOAD PHOTO
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, "x.png")
photo = PhotoImage(file=image_path)

# RESIZE PHOTO
photo_resized = photo.subsample(20, 20)

# BUTTON W/ IMAGE
Button(root, text='Click Me!',
       image=photo_resized).pack(side=TOP)

# BUTTON W/ IMAGE AND TEXT
Button(root, text='Click Me!',
       image=photo_resized, compound=LEFT).pack(side=TOP)

# CANVAS W/ IMAGE
canvas = Canvas(root, width=40, height=40, bg='white')
canvas.pack(side=TOP)
canvas.create_image(0, 0, anchor=NW, image=photo_resized) #0, 0 = x, y

mainloop()


