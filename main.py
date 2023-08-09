from tkinter import *
import tkinter
import random
import pyglet
import time


tk = Tk()
tk.title("Zero Gravity Ball")
tk.geometry("800x600")
tk.resizable(False, False)
tk.wm_attributes('-topmost', 1)


canvas = Canvas(tk, width=800, height=600, bg='#302655')
canvas.pack()

pls = []
x=100
y=500
r=20
yv=5
xv=-5
still = False
mus = pyglet.resource.media('ir.mp3')
mus.play()
img = tkinter.PhotoImage(file='bg.png')
image = canvas.create_image(0, 0, anchor='nw',image=img)
player = canvas.create_oval(x-r,y-r,x+r,y+r,fill="red",width=2,outline="black")


def new_platfom():
    global pls
    x = random.randint(0, 800-120)
    y = 10
    w = 120
    h = 12
    color = "khaki2"
    platform = canvas.create_rectangle(x, y, x+w, y+h, fill=color, width=2, outline="white")
    pls.append(platform)
    canvas.after(1750, new_platfom)


scorrr = 0
canvas = canvas
id = canvas.create_text(200, 20, text=scorrr, font=('Arial', 20), fill='black')
id_text = canvas.create_text(100, 19, text='Текущий счёт:', font=('Arial', 20), fill='black')


def move_platform():
    global pls, still,yv,xv
    x, y, _, _, = canvas.coords(player)
    for platform in pls:
        canvas.move(platform,0,2)
        if platform_check(platform):
            break
        px, py, _, _, = canvas.coords(platform)
        if py - 2 * r <= y - r / 3 <= py:
            if px <= x <= px + 120:
                if not still:
                    yv=0
                    canvas.coords(player, px - r + 60, py - r - 22, px + r + 60, py + r - 22)
                    still=True


def platform_check(platform):
    global pls
    px, py, _, _ = canvas.coords(platform)
    if py > 620:
        pls.remove(platform)
        print('Платформа удалена')
        return True
    return False


def player_move():
    global player,x,y,x2,y2,r,yv,xv
    x, y, _, _, = canvas.coords(player)

    if still:
        yv=2
    else:
        yv+=2

    if still:
        xv*=0.5
    else:
        xv*=0.94

    y+=yv
    x+=xv

    if x <=0 - 2*r:
        xv=-xv
    if x >=800-2*r:
        xv=-xv
    if y <=0 - 2*r:
        yv=-yv
    if y >=600-2*r:
        yv=-yv

    canvas.move(player, xv, yv)


def click(event):
    global yv,xv,still
    still = False
    activ = True
    x,y,_,_=canvas.coords(player)
    xv=(event.x-x)/15
    yv=(event.y-y)/9
    print(event.x, event.y)

canvas.bind_all("<1>",click)

new_platfom()

while True:
    move_platform()
    player_move()
    canvas.update()
    canvas.update_idletasks()
    time.sleep(0.01)

# def new_platform():
#     global pls
#     x = random.randint(0,800-120)
#     y = 10
#     w=120
#     h=20
#     color="khaki2"
#     platform=canvas.create_rectangle(x,y,x+w,y+h,fill=color,width=2,outline="white")
#     pls.append(platform)
#     canvas.after(1750, new_platform)
#
#
# def move_platform():
#     global pls,still,yv,xv
#     x, y, _, _, = canvas.coords(ball_player)
#     for platform in pls:
#         canvas.move(platform,0,2)
#         px, py, _, _, = canvas.coords(ball_player)
#         if py - 2 * r <= y - r / 3 <= py:
#             if px <= x <= px + 120:
#                 if not still:
#                     yv=0
#                     canvas.coords(ball_player, px - r + 60, py - r - 22, px + r + 60, py + r - 22)
#                     still=True
#
#
# def player_move():
#     global player,x,y,x2,y2,r,yv,xv
#     x, y, _, _, = canvas.coords(ball_player)
#     y+=yv
#     x+=xv
#
#     if x <=0 - 2*r:
#         xv=-xv
#     if x >=800-2*r:
#         xv=-xv
#     if y <=0 - 2*r:
#         yv=-yv
#     if y >=600-2*r:
#         yv=-yv
#
#     canvas.move(ball_player, xv, yv)
#
#
# def click(event):
#     global yv,xv,still
#     still = False
#     x,y,_,_=canvas.coords(ball_player)
#     xv=(event.x-x)/15
#     yv=(event.y-y)/9
#     print(event.x, event.y)
#
#
# canvas.bind_all('<1>', click)
#
# img = tkinter.PhotoImage(file='bg.png')
# image = canvas.create_image(0, 0, anchor='nw',image=img)
#
#
# ball_player = canvas.create_oval(x - r, y - r, x + r, y + r, fill='red', width=0)
#
# new_platform()
# while True:
#     player_move()
#     move_platform()
#     canvas.update()
#     canvas.update_idletasks()
#     time.sleep(0.01)