from tkinter import *
from PIL import Image, ImageTk
import os

f = open('path.txt', 'r')
paths = [line.rstrip() for line in f.readlines()]
path_of_dir = paths[0]
imgs = os.listdir(path_of_dir)
f.close()
f = open('steps.txt', 'r')
steps_data = f.readlines()
f.close()
count = 0
rely1 = 0.92

def parse():
    global idx
    splitted = [img.split('.') for img in imgs]
    idx = [int(el[0]) for el in splitted]
    idx.sort()

def show_image(path=path_of_dir + '/'+ imgs[0]):
    global canvas1, im
    im = ImageTk.PhotoImage(Image.open(path).resize((800, 600)))
    canvas1.create_image(800, 320, image=im)

def show_paths():
    try:
        canvas1.delete('paths')
    except:
        pass
    paths_text = 'Paths:\n' + '\n'.join(paths[1:])
    canvas1.create_text(120, 550, text=paths_text, font=('Arial', '14'), tags=('paths'))

def go_back():
    global count, canvas1
    if count > 0:
        count -= 1
        if count > 0:
            text_genr()
        show_image('{}/{}.jpg'.format(path_of_dir, count))

def go_next():
    global count, canvas1
    if count < max(idx):
        count += 1
        text_genr()
        show_image('{}/{}.jpg'.format(path_of_dir, count))

def text_genr():
    global canvas1
    if count == max(idx):
        canvas1.delete('current_vertex')
        canvas1.create_text(140, 200, text='DONE! :)', font=('Arial', '20'), fill='red', tags=('current_vertex'))
        show_paths()
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
    show_mid_btn(2)
    auto_run2()
    
def stop():
    show_mid_btn(3)
    auto_run2(False)
    
def continue1():
    show_mid_btn(2)
    auto_run2()

def auto_run2(flag=True, waitTime=1000):
    global count, window, b
    if flag == False:
        window.after_cancel(b)
        count -= 1
        return
    if count < max(idx)+1:
        text_genr()
        show_image('{}/{}.jpg'.format(path_of_dir, count))
        count += 1
        b = window.after(waitTime, auto_run2)
    if count == max(idx)+1:
        show_mid_btn(1)
        
def show_mid_btn(flag):
    global autobtn
    try:
        autobtn.destroy()
    except:
        pass
    if flag == 1:
        autobtn = Button(mainFrame, text='Auto', font=font, command=auto_run)
    elif flag == 2:
        autobtn = Button(mainFrame, text='Stop', font=font, command=stop)
    elif flag == 3:
        autobtn = Button(mainFrame, text='Continue', font=font, command=continue1)
    autobtn.place(relx=0.5, rely=rely1, anchor=CENTER)

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

parse()
text_genr()
show_image()

# font
font = ('Arial', '18')

# buttons
# previous image
backbtn = Button(mainFrame, text='Back', font=font, command=go_back)
# auto run
show_mid_btn(True)
# next image
nextbtn = Button(mainFrame, text='Next', font=font, command=go_next)

# set place
backbtn.place(relx=0.4, rely=rely1, anchor=CENTER)
nextbtn.place(relx=0.6, rely=rely1, anchor=CENTER)

window.mainloop()
