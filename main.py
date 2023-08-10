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
score = 1
x=100
y=500
r=20
yv=5
xv=-5
still = False
active = False
mus = pyglet.resource.media('k.mp3')
mus.play()
img = tkinter.PhotoImage(file='bg.png')
image = canvas.create_image(0, 0, anchor='nw',image=img)
player = canvas.create_oval(x-r,y-r,x+r,y+r,fill="red",width=2,outline="black")


def new_platfom():
    global pls, score
    if active:
        score += 1
    canvas.itemconfig(id, text=f'Очки : {score}')
    x = random.randint(0, 800-120)
    y = 10
    w = 120
    h = 12
    color = "khaki2"
    platform = canvas.create_rectangle(x, y, x+w, y+h, fill=color, width=2, outline="white")
    pls.append(platform)
    canvas.after(1750, new_platfom)


id = canvas.create_text(50, 20, text=score, font=('Arial', 20), fill='purple')


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

    if y >= 600 - 2 * r and not active:
        vy = 0
    if y >= 600 - 2 * r and active:
        canvas.delete(player)
        canvas.delete(*pls)
        return True

    canvas.move(player, xv, yv)


def click(event):
    global yv,xv,still,active
    still = False
    active = True
    x,y,_,_=canvas.coords(player)
    xv=(event.x-x)/15
    yv=(event.y-y)/9
    print(event.x, event.y)


canvas.bind_all("<1>",click)

new_platfom()

while True:
    move_platform()
    lose = player_move()
    if lose:
        canvas.delete(score)
        canvas.create_text(400, 280, text=f'Ты проиграл!\n Результат : {score}', fill='purple', font=('TIMES NEW ROMAN', 18))
        canvas.update()
        time.sleep(3)
        break
    canvas.update()
    canvas.update_idletasks()
    time.sleep(0.01)