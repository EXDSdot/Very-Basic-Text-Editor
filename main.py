# Tkinter for 2.7; tkinter for 3.3/3.4 (and above I assume)
# TODO: replace import with a more precise one
from tkinter import *
import tkinter.filedialog as file_dialog

root = Tk(baseName="Text editor")
text = Text(root)
text.grid()


def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = file_dialog.asksaveasfilename()
    with open(save_location, "w+") as file:
        file.write(t)

# TODO: Handle exceptions
def open_file():
    global text
    file_location = file_dialog.askopenfilename()
    with open(file_location, "r") as file:
        file_content = file.read()
    text.delete("1.0", "end-1c")
    text.insert("1.0", file_content)


def font_helvetica():
    global text
    text.config(font="Helvetica")


def font_courier():
    global text
    text.config(font="Courier")


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
root.mainloop()
