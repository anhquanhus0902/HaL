import cv2
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import PIL.Image, PIL.ImageTk
from time import sleep
from threading import Thread

window = Tk()
window.title("OpenCV Tkinter")

video = cv2.VideoCapture(0)
photo = None
count = 0

def send_to_server():
    sleep(10)
    return

# canvas_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)//2
# canvas_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)//2

canvas_width = 640
canvas_height = 480

canvas = Canvas(window, width=canvas_width, height=canvas_height, bg="red")
canvas.pack()

bw = 0
def handleBW():
    global bw
    bw = 1-bw

button1 = Button(window, text="Black & White", command=handleBW)
button1.pack()

def update_frame():
    global canvas, photo, bw, count
    # Đọc từ camera
    ret, frame = video.read()
    # Chỉnh sửa lại kích thước của frame cho dễ nhìn hơn
    frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
    # Chuyển đổi hệ màu
    if bw == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    window.after(15, update_frame)
    count += 1
    if count == 10:
        # send_to_server()
        thread = Thread(target=send_to_server)
        thread.start()

update_frame()
window.mainloop()