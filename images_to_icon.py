from tkinter import *
from tkinter import filedialog, Button
from PIL import Image

rat = Tk()
rat.title("Divine's images")
rat.geometry("400x400")



canvas1 = Canvas(rat, width=300, height=250, bg='gray', relief='raised')
canvas1.pack()

label1 = Label(rat, text='PNG TO ico ', bg='gray', font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getFile():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path).convert('RGB')


BrowseButton_File = Button(text="import file", command=getFile)
canvas1.create_window(150, 130, window=BrowseButton_File)


def convertToICO():
    global im1

    export_file_path = filedialog.asksaveasfile(defaultextension=".ico").name

    # print(export_file_path)
    im1.save(export_file_path)


saveAs_ICO = Button(text='convert image to ICO', command=convertToICO)
canvas1.create_window(150, 180, window=saveAs_ICO)


rat.mainloop()
