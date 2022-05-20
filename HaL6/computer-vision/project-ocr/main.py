#!/usr/bin/env python

from platform import python_branch
import traceback
import preprocessing
import cv2
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def cv2pil(im):
    if len(im.shape) == 3:
        b,g,r = cv2.split(im)
        im = cv2.merge((r,g,b))
    return Image.fromarray(im)

def show_image(x, y, im, fixed_h=640, fixed_w=480):
    global canvas1, tk_im
    pillow_im = cv2pil(im)
    w, h = pillow_im.size
    while True:
        if h <= fixed_h and w <= fixed_w:
            break
        old_ratio  = h/w if h > w else w/h
        if h > fixed_h:
            h = fixed_h
            w = int(w/old_ratio)
        elif w > fixed_w:
            w = fixed_w
            h = int(h/old_ratio)
    pillow_im = pillow_im.resize((w, h), Image.ANTIALIAS)
    tk_im = ImageTk.PhotoImage(pillow_im)
    canvas1.create_image(x, y, image=tk_im)

def choose_file():
    global im, choosen
    filetypes = (
        ('All files', '*.*'),
        ('JPEG files', '*.jpg'),
        ('PNG files', '*.png')
    )
    filename = filedialog.askopenfilename(title='Choose an image', initialdir='./', filetypes=filetypes)
    if filename:
        im = cv2.imread(filename)
        choosen = True
        show_image(640, 360, im)

def auto_crop():
    global im, choosen
    if choosen:
        drawed_contours = preprocessing.preprocess(im)
        # im2pdf(im)
        show_image(640, 360, drawed_contours)
    else:
        messagebox.showwarning(title=None, message='Please choose an image')
        
def im2pdf(im):
    pillow_im = cv2pil(im)
    im_p = pillow_im.convert('RGB')
    im_p.save(r'test.pdf')

im = None
choosen = False
window = Tk()
window.title('Document Scanning - CV')
window.geometry('1280x720')
window.resizable(0,0)
frame1 = Frame(window)
frame1.pack(side=TOP, fill='both', expand=True)

canvas1 = Canvas(frame1, bg='#D1D1D1')
canvas1.pack(side=TOP, fill='both', expand=True)
# canvas1.create_line(640, 0, 640, 720)
# canvas1.create_line(0, 360, 1280, 360)
choose_file_btn = Button(frame1, text='Pick', font=('Arial', '18'), command=choose_file)
choose_file_btn.place(relx=0.2, rely=0.4, anchor=CENTER)
auto_crop_btn = Button(frame1, text='Crop', font=('Arial', '18'), command=auto_crop)
auto_crop_btn.place(relx=0.2, rely=0.5, anchor=CENTER)

if __name__ == "__main__":
    try:
        window.mainloop()
    except Exception:
        traceback.print_exc()