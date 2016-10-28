#!/usr/bin/env python

""" Git difftool for visual diff of EagleCAD *.sch and *.brd files. """
import os
import sys
import imp
import Tkinter
import subprocess

try:
    imp.find_module('PIL')
    from PIL import Image
    from PIL import ImageTk
    from PIL import ImageChops
except ImportError:
    print "PIL missing"
    print "Install it from http://www.pythonware.com/products/pil/"
    sys.exit(1)


def main():
    """ Creates diff from 2 git versions of a *.sch or *.brd """
    eagle_path = get_eagle_path()
    generate_images(eagle_path)

    root = Tkinter.Tk()
    root.resizable(0, 0)

    image1 = Image.open('b1.png')
    img_width = 640
    ratio = float(image1.size[0]) / float(image1.size[1])
    img_height = int(img_width / ratio)

    image1 = image1.resize((img_width, img_height), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(image1)
    image2 = Image.open('b2.png')
    image2 = image2.resize((img_width, img_height), Image.ANTIALIAS)
    tkimage2 = ImageTk.PhotoImage(image2)
    diff = ImageChops.difference(image1, image2)
    diff = diff.resize((img_width, img_height), Image.ANTIALIAS)
    tk_diff = ImageTk.PhotoImage(diff)
    overlay = ImageChops.screen(image1, image2)
    overlay = overlay.resize((img_width, img_height), Image.ANTIALIAS)
    tk_overlay = ImageTk.PhotoImage(overlay)

    root.geometry('%dx%d' % (image1.size[0] * 2, image1.size[1] * 2))

    Tkinter.Label(root, image=tkimage1)\
           .place(x=0, y=0, width=img_width, height=img_height)
    Tkinter.Label(root, image=tkimage2)\
           .place(x=img_width, y=0, width=img_width, height=img_height)
    Tkinter.Label(root, image=tk_diff)\
           .place(x=0, y=img_height, width=img_width, height=img_height)
    Tkinter.Label(root, image=tk_overlay)\
           .place(x=img_width, y=img_height, width=img_width, height=img_height)

    root.title("Image diff")
    root.mainloop()
    os.system('del b1.png b2.png')


def get_eagle_path():
    """ Returns the path for Eagle.exe """
    path_prefix = "/EAGLE-7."
    path_suffix = ".0/bin/eagle.exe"
    path = ""
    for minor_version in range(9, 0, -1):
        eagle_root = path_prefix + str(minor_version) + path_suffix
        path_on_c = "C:" + eagle_root
        path_x86 = "C:/Program Files" + eagle_root
        path_x64 = "C:/Program Files (x86)" + eagle_root
        if os.path.exists(path_on_c):
            path = path_on_c
            break
        if os.path.exists(path_x64):
            path = path_x64
            break
        if os.path.exists(path_x86):
            path = path_x64
            break
    print "Using " + path
    return path


def generate_images(eagle_path):
    """ Generate images given a path to eagle.exe """
    cmd = eagle_path + " -C \"export image b1.png 400;quit\" " + sys.argv[1]
    subprocess.call(cmd)
    cmd = eagle_path + " -C \"export image b2.png 400;quit\" " + sys.argv[2]
    subprocess.call(cmd)

if __name__ == "__main__":
    main()
