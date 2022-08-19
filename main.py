# Tkinter for 2.7; tkinter for 3.3/3.4 (and above I assume)
# TODO: replace import with a more precise one
import tkinter.simpledialog
from tkinter import *
import tkinter.filedialog as file_dialog
from tkinter import messagebox


root = Tk(baseName="Text editor")
text = Text(root)
text.grid()


def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = file_dialog.asksaveasfilename(title="Save file",
                                                  defaultextension=".txt")
    with open(save_location, "w+") as file:
        file.write(t)


# TODO: Make error appear on top of the file_dialog window
def open_file():
    global text
    file_location = file_dialog.askopenfilename(title="Open file")
    try:
        with open(file_location, "r") as file:
            file_content = file.read()
        text.delete("1.0", "end-1c")
        text.insert("1.0", file_content)
    except (OSError, TypeError):
        messagebox.showerror("File error", "Couldn't read/open file")


def set_font(f=None, sz=None):
    global text
    if isinstance(f, str):
        fnt = f
    if isinstance(sz, int):
        s = sz
    try:
        f
    except NameError:
        f = "Arial"
    try:
        s
    except NameError:
        s = 12
    text.config(font=fnt + " " + str(s))


def font_helvetica():
    set_font("Helvetica")


def font_courier():
    set_font("Courier")


def set_font_size():
    size = tkinter.simpledialog.askinteger(title="Set font size",
                                           prompt="Enter desired font size")
    if 8 <= size <= 72:
        set_font(None, size)
    else:
        messagebox.showerror("Font size error", "Font size not"
                                                "supported")


font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,
                          command=font_courier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
                          command=font_helvetica)


save_button = Button(root, text="Save", command=save_as)
save_button.grid()
open_button = Button(root, text="Open", command=open_file)
open_button.grid()
font_size_button = Button(root, text="Set font size", command=set_font_size)
font_size_button.grid()
root.mainloop()
