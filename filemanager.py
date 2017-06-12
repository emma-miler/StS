#TODO: find a better way to transfer variables between files
#TODO: clean this up

import os  #in

def wpitch(x):
    if os.path.isfile("pitch.txt"):
        os.remove("pitch.txt")
    f = open("pitch.txt", 'w+')
    f.write(str(x + 1))
    f.close()

def wlength(x):
    if os.path.isfile("length.txt"):
        os.remove("length.txt")
    f = open("length.txt", 'w+')
    f.write(str(x))
    f.close()

def wpath(x):
    if os.path.isfile("path.txt"):
        os.remove("path.txt")
    f = open("path.txt", 'w+')
    f.write(str(x.replace("\\", "/")))
    f.close()


def write(screensize, size, sidelength, end, start, bwlist, raw_pitch, pitch, volume):
    if os.path.isfile("debug.txt"):
      os.remove("debug.txt")
    f = open("debug.txt", "w+")
    f.write("screensize ")
    f.write(str(screensize))
    f.write("\n")
    f.write("size of curve ")
    f.write(str(size))
    f.write("\n")
    f.write("sidelength of curve ")
    f.write(str(sidelength))
    f.write("\n")
    f.write("processing time was ")
    f.write(str(end - start))
    f.write(" second(s)")
    f.write("\n")
    f.write("the brightest pixel had value ")
    f.write(str(max(bwlist)))
    f.write("\n")
    f.write("\n\n\n")
    f.write("---debug info---")
    f.write("\n\n")
    f.write("bw values ")
    f.write(str(bwlist))
    f.write("\n\n")
    f.write("pixel percentage on pitchline ")
    f.write(str(raw_pitch))
    f.write("\n\n")
    f.write("pixel pitch ")
    f.write(str(pitch))
    f.write("\n\n")
    f.write("pixel volume")
    f.write(str(volume))
    f.close()

def delete():
    try:
        os.remove("pitch.txt")
        os.remove("length.txt")
        os.remove("path.txt")
    except:
        pass