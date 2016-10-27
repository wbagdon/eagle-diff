#!/usr/bin/env python
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
    eagle_path = getEaglePath()

    cmd = eagle_path + " -C \"export image b1.png 400;quit\" " + sys.argv[1]
    subprocess.call(cmd)
    cmd = eagle_path + " -C \"export image b2.png 400;quit\" " + sys.argv[2]
    subprocess.call(cmd)

    root = Tkinter.Tk()
    root.resizable(0, 0)

    im_size = 640

    image1 = Image.open('b1.png')
    ratio = float(image1.size[0]) / float(image1.size[1])
    image1 = image1.resize((im_size, int(im_size / ratio)), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(image1)
    image2 = Image.open('b2.png')
    image2 = image2.resize((im_size, int(im_size / ratio)), Image.ANTIALIAS)
    tkimage2 = ImageTk.PhotoImage(image2)
    diff = ImageChops.difference(image1, image2)
    diff = diff.resize((im_size, int(im_size / ratio)), Image.ANTIALIAS)
    tk_diff = ImageTk.PhotoImage(diff)
    overlay = ImageChops.screen(image1, image2)
    overlay = overlay.resize((im_size, int(im_size / ratio)), Image.ANTIALIAS)
    tk_overlay = ImageTk.PhotoImage(overlay)

    root.geometry('%dx%d' % (image1.size[0] * 2, image1.size[1] * 2))
    label_image1 = Tkinter.Label(root, image=tkimage1)
    label_image2 = Tkinter.Label(root, image=tkimage2)
    label_diff = Tkinter.Label(root, image=tk_diff)
    label_overlay = Tkinter.Label(root, image=tk_overlay)

    label_image1.place(x=0, y=0,
                       width=im_size, height=int(im_size/ratio))
    label_image2.place(x=im_size, y=0,
                       width=im_size, height=int(im_size/ratio))
    label_diff.place(x=0, y=int(im_size/ratio),
                     width=im_size, height=int(im_size/ratio))
    label_overlay.place(x=im_size, y=int(im_size/ratio),
                        width=im_size, height=int(im_size/ratio))

    root.title("Image diff")
    root.mainloop()
    os.system('del b1.png b2.png')


def getEaglePath():
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

if __name__ == "__main__":
    main()
