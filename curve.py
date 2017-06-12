#importing libraries
import sound  #own
import time  #in
import os  #in
import turtle  #in
import tkinter
import math  #in
import PIL.Image
import filemanager  #own
import export #own

#starting timer
start = time.time()

#input values
# noinspection PyShadowingBuiltins,PyPep8Naming
class input:
    p = open("pitch.txt", "r+")
    maxpitch1 = p.read()
    p.close()
    
    l = open("length.txt", "r+")
    maxlen = l.read()
    l.close()
    
    b = open("path.txt", "r+")
    path = b.read()
    b.close()
    
    x = 0
    side = PIL.Image.open(str(path))
    sidelength = side.size[1]
    side.close()
    size = (math.log(sidelength, 2)) + 1
    screensize = sidelength * 10
    if not math.log(sidelength, 2).is_integer():
        root = tkinter.Tk()
        b = tkinter.Text(root, height=1, font="font, 50", width=22)
        b.insert(tkinter.INSERT, "File is not a multiple of 2^x!")
        b.pack()
        tkinter.mainloop()
        exit()

#resizing image
img = PIL.Image.open(str(input.path))
img2 = img.resize((input.sidelength * 20, input.sidelength * 20), PIL.Image.ANTIALIAS)
dir_path = os.getcwd()
dir_path = dir_path.replace("\\\\", "/")
img2.save(str(dir_path) + "/temp.gif")
img2 = PIL.Image.open(str(dir_path) + "/temp.gif")
bwget = img2.load()

#other values
# noinspection PyPep8Naming
class values:
    bwlist = []
    bw = 0
    pitch = []
    volume = []
    raw_pitch = []
    output = [(0, 0)]
    maxpitch = int(input.maxpitch1)

#turtle setup
turtle.tracer(0, 0)
turtle.setup(input.screensize * 2, input.screensize * 2 + 16)
turtle.screensize(input.screensize * 2 - 25, input.screensize * 2 - 50)
turtle.setx(input.screensize - 5)
turtle.sety(input.screensize - 5)
values.bwlist.append(bwget[int(-turtle.xcor()) + input.screensize, int(turtle.ycor()) + input.screensize])

#defining functions
def a1(angle):
    turtle.dot(5, "red")
    turtle.left(angle)
def a2(angle):
    turtle.dot(5, "red")
    turtle.right(angle)
def a3(angle):
    turtle.forward(angle)
    input.x += 1
    if values.bw > 2:
        values.bw = 0
        values.bwlist.append(bwget[int(-turtle.xcor()) + input.screensize, int(turtle.ycor()) + input.screensize])
    else:
        values.bw += 1

#defining hilbert curve function
# noinspection PyShadowingNames
def hilbert2(step, rule, angle, depth):
    if depth > 0:
        a = lambda: hilbert2(step, "a", angle, depth - 1)
        b = lambda: hilbert2(step, "b", angle, depth - 1)
        left = lambda: a1(angle)
        right = lambda: a2(angle)
        forward = lambda: a3(-step)
        if rule == "a":
            left()
            b()
            forward()
            right()
            a()
            forward()
            a()
            right()
            forward()
            b()
            left()
        if rule == "b":
            right()
            a()
            forward()
            left()
            b()
            forward()
            b()
            left()
            forward()
            a()
            right()

hilbert2(10, "b", -90, input.size)

#getting variables ready for playing
for x in range(0, len(values.bwlist)):
    values.raw_pitch.append(100 / len(values.bwlist) * x)
    values.volume.append(((5000 / 100) * values.bwlist[x]) + 37)
    if not max(values.bwlist) == 0:
      # noinspection PyTypeChecker
      values.pitch.append(int(((int(((5000 / 100) * values.maxpitch)) / 255) * (255 - (100 / max(values.bwlist)) * abs((values.bwlist[x] - max(values.bwlist)))))))
    else:
        values.pitch.append(int(((int(((5000 / 100) * values.maxpitch)) / 255) * (255 - 255) * abs((values.bwlist[x] - max(values.bwlist))))))
    # noinspection PyTypeChecker
    values.output.append([(values.pitch[x]), (values.volume[x])])

#stopping timer
end = time.time()

#writing debug
def write():
    filemanager.write(input.screensize, input.size, input.sidelength, end, start,
                  values.bwlist, values.raw_pitch, values.pitch, values.volume)

#done message
turtle.bye()
root = tkinter.Tk()

def exportmain():
    export.export(values.pitch)
    b = tkinter.Text(root, height=1, font="font, 20", width=34)
    b.insert(tkinter.INSERT, "Your file was succesfully exported")
    b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
    b.pack()
    b = tkinter.Text(root, height=1, font="font, 15", width=63)
    b.insert(tkinter.INSERT, "It should be located under in the exports folder of the program")
    b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
    b.pack()
    b = tkinter.Text(root, height=1, font="font, 15", width=41)
    b.insert(tkinter.INSERT, "This is usually C:/Program Files(x86)/StS")
    b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
    b.pack()

def quit1():
    root.destroy()
    root.quit()
img2.close()
b = tkinter.Text(root, height=1, font="font, 25", width=19)
b.insert(tkinter.INSERT, "Your file was converted")
b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
b.pack()
b = tkinter.Button(root, text="Play", command=quit1, font="font, 25")
b.pack()
b = tkinter.Button(root, text="Export", command=exportmain, font="font, 25")
b.pack()
tkinter.mainloop()

#playing sound
for x in range(0, len(values.bwlist)):
    sound.play(int(values.pitch[x]), int(input.maxlen))
filemanager.delete()