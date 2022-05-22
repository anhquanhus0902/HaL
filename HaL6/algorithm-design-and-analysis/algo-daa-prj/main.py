from tkinter import *
from PIL import Image, ImageTk
import os

f = open('path.txt', 'r')
path = f.read()
imgs = os.listdir(path)
f.close()
f = open('steps.txt', 'r')
steps_data = f.readlines()
f.close()
count = 0

def parse():
    global idx
    splitted = [img.split('.') for img in imgs]
    idx = [int(el[0]) for el in splitted]
    idx.sort()
parse()

def show_image(path=path + '/'+ imgs[0]):
    global canvas1, im
    im = ImageTk.PhotoImage(Image.open(path).resize((800, 600)))
    canvas1.create_image(800, 320, image=im)

def go_back():
    global count, canvas1
    if count > 0:
        count -= 1
        if count > 0:
            text_genr()
        show_image('{}/{}.jpg'.format(path, count))

def go_next():
    global count, canvas1
    if count < max(idx):
        count += 1
        text_genr()
        show_image('{}/{}.jpg'.format(path, count))

def text_genr():
    global canvas1
    if count == max(idx):
        canvas1.delete('current_vertex')
        canvas1.create_text(140, 200, text='DONE! :)', font=('Arial', '20'), fill='red', tags=('current_vertex'))
        return
    font = ('Arial', '14')
    i = 4*count
    current_vertex = steps_data[i]
    d = steps_data[i+1][4:-2].split(', ')
    p = steps_data[i+2][4:-2].split(', ')
    visited = steps_data[i+3][len('visited: {'):-2].split(', ')
    d.insert(0, 'd')
    d_text = '\n'.join(d)
    p.insert(0, 'p')
    p_text = '\n'.join(p)
    visited.insert(0, 'is visited?')
    visited_text = '\n'.join(visited)
    canvas1.delete('current_vertex')
    canvas1.delete('d_text')
    canvas1.delete('p_text')
    canvas1.delete('visited_text')
    canvas1.create_text(140, 200, text=current_vertex, font=('Arial', '20'), fill='red', tags=('current_vertex'))
    canvas1.create_text(60, 300, text=d_text, font=font, tags=('d_text'))
    canvas1.create_text(160, 300, text=p_text, font=font, tags=('p_text'))
    canvas1.create_text(280, 300, text=visited_text, font=font, tags=('visited_text'))

def auto_run():
    global count
    count = 0
    auto_run2()

def auto_run2(waitTime=1000):
    global count, window
    if count < max(idx)+1:
        text_genr()
        show_image('{}/{}.jpg'.format(path, count))
        count += 1
        window.after(waitTime, auto_run2)

# window
window = Tk()
window.title('Visualize Dijkstra Algorithm')
window.geometry('1280x720')
window.resizable(0,0)

# frame
mainFrame = Frame(window)
mainFrame.pack(side=TOP, fill='both', expand=True)

# canvas
canvas1 = Canvas(mainFrame, bg='#D1D1D1')
canvas1.pack(side=TOP, fill='both', expand=True)
text_genr()
show_image()

# font
font = ('Arial', '18')

# buttons
# previous image
backbtn = Button(mainFrame, text='Back', font=font, command=go_back)
# auto run
autobtn = Button(mainFrame, text='Auto', font=font, command=auto_run)
# next image
nextbtn = Button(mainFrame, text='Next', font=font, command=go_next)

# set place
rely1 = 0.92
backbtn.place(relx=0.4, rely=rely1, anchor=CENTER)
autobtn.place(relx=0.5, rely=rely1, anchor=CENTER)
nextbtn.place(relx=0.6, rely=rely1, anchor=CENTER)

window.mainloop()
