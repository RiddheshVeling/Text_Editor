from tkinter import *
from tkinter import filedialog
from tkinter import font

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            my_text.delete(1.0, END)
            my_text.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(my_text.get(1.0, END))

def new_file():
    my_text.delete(1.0, END)

root = Tk()
root.title("CodeClause - TextPad")
root.iconbitmap("C:/Users/ASUS/OneDrive/Desktop/Codeclause/Text Editor/Notepad icon.ico")
root.geometry("1200x660")

my_frame = Frame(root)
my_frame.pack(pady = 5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)

my_text = Text(my_frame, width = 97, height = 25, font = ("Helvetica", 16), selectbackground = "Yellow", selectforeground = "black", undo = True, yscrollcommand = text_scroll.set)
my_text.pack()

text_scroll.config(command = my_text.yview)

my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff = False)
my_menu .add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Paste")
edit_menu.add_command(label = "Undo")
edit_menu.add_command(label = "Redo")

status_bar = Label(root, text = "Ready", anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)


root.mainloop()