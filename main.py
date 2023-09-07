from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msb
from PIL import Image, ImageTk
from getpass import getuser

class Window(Tk):
    file=''
    outfile=''
    filetypes=list((("Joint Photographic Experts Group (JPEG)", "*.jpg"), 
                ("Portable Network Graphics (PNG)", "*.png"), ("Icon (ICO)", "*.ico"), 
        ("Tag Image File Format (TIFF)", "*.tiff"), ("Bitmap (BMP)", "*.bmp"), 
        ("DirectDraw Surface (DDS)", "*.dds"), ("Encapsulated PostScript (EPS)", "*.eps"), 
        ("Picture exchange (PCX)", "*.pcx"), ("Web Image (WEBP)", "*.webp")))

    def __init__(self):
        Tk.__init__(self)
        self.title("Image Converter")
        self.iconbitmap(r"P:\Python Projects\Image Converter\icon.ico")
        self.geometry("550x410")
        self.resizable(0, 0)

    def convert(self):
        if not self.file:
            msb.showerror("File not given", "Please enter the input filename.")
            return
        if not self.outfile:
            msb.showerror("File not given", "Please enter the output filename.")
            return
        img=Image.open(self.file)
        img.save(self.outfile)
        msb.showinfo("Converted Successfully", "File "+self.file.split("\\")[-1]
        +" converted successfully.")

    def inputfile(self):
        self.file=filedialog.askopenfilename(defaultextension=".jpg", 
        filetypes=self.filetypes, title="Open File Name", 
        initialdir=rf"C:\Users\{getuser()}\Pictures").replace("/","\\")
        if self.file:
            self.text1.delete(0, END)
            self.text1.insert(0, self.file)
            self.ext1.config(state=NORMAL)
            self.ext1.delete(0, END)
            if self.file[-4:]==".jpg":
                self.ext1.insert(0, "JPEG File")
            elif self.file:
                self.ext1.insert(0, self.file[-3:].upper()+" File"
                if "tiff" or "webp" not in self.file else "TIFF File")
            self.ext1.config(state=DISABLED)
        else:
            msb.showerror("File not given", "Please input a file.")

    def outputfile(self):
        self.filetypes1=list(self.filetypes)
        for i in self.filetypes1:
            if self.file[-3:] in i[1]:
                self.filetypes1.remove(i)
        self.outfile=filedialog.asksaveasfilename(title="Save As Filename", 
                initialdir='\\'.join(self.file.split("\\")[:-1]),
                confirmoverwrite=True, defaultextension="",
                filetypes=self.filetypes1,
                initialfile=self.file.split("\\")[-1][:-4]
                if "tiff" or "webp" not in self.file else self.file.split("\\")[-1][:-5]).replace("/","\\")
        if self.outfile:
            self.text2.delete(0, END)
            self.text2.insert(0, self.outfile)
            self.ext2.config(state=NORMAL)
            self.ext2.delete(0, END)
            if self.outfile[-4:]==".jpg":
                self.ext2.insert(0, "JPEG File")
            elif self.outfile:
                self.ext2.insert(0, self.outfile[-3:].upper()+" File"
                if "tiff" not in self.outfile else "TIFF File")
            self.ext2.config(state=DISABLED)
        else:
            msb.showerror("File not given", "Please input a file.")

    def reset(self):
        self.text1.delete(0, END)
        self.text2.delete(0, END)
        self.ext1.config(state=NORMAL)
        self.ext1.delete(0, END)
        self.ext1.config(state=DISABLED)
        self.ext2.config(state=NORMAL)
        self.ext2.delete(0, END)
        self.ext2.config(state=DISABLED)
        self.file=''
        self.outfile=''

    def createwidgets(self):
        self.background=PhotoImage(file=r"P:\Python Projects\Image Converter\background.png")
        self.canvas=Canvas(self, width=550, height=420)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.create_image(-5,-5, anchor=NW, image=self.background)

        self.canvas.create_text(280, 30,text="Image Converter", font="Arial 30", 
        fill="white")

        self.canvas.create_text(65, 80,text="Input File:", font="Arial 19", 
        fill="white")
        self.text1=ttk.Entry(self.canvas, width=28, font="Arial 17")
        self.text1.place(x=10, y=100)
        self.ext1=Entry(self.canvas, width=10, font="Arial 17", 
                    state=DISABLED, relief="flat", disabledbackground="white",
                    disabledforeground="black", highlightthickness=1, 
                    highlightcolor="black", highlightbackground="black")
        self.ext1.place(x=390, y=100)

        self.canvas.create_text(75, 230,text="Output File:", font="Arial 19", 
        fill="white")
        self.browseborder1=Frame(self.canvas, highlightbackground="black",
                        highlightcolor="black", highlightthickness=2,
                        bd=0, relief="solid")
        self.browseborder1.place(x=395, y=150)
        self.browse1=Button(self.browseborder1, font="Arial 15", text="Browse", cursor="hand2", 
                    relief="flat", highlightthickness=1, highlightcolor="black", 
                    highlightbackground="black", border=2, background="white",
                    command=self.inputfile)
        self.browse1.pack(fill=BOTH, ipadx=20)
        self.browse1.bind("<Enter>", lambda _: enter(self.browse1))
        self.browse1.bind("<Leave>", lambda _: leave(self.browse1))

        self.text2=ttk.Entry(self.canvas, width=28, font="Arial 17")
        self.text2.place(x=10, y=250)
        self.ext2=Entry(self.canvas, width=10, font="Arial 17", 
                    state=DISABLED, relief="flat", disabledbackground="white",
                    disabledforeground="black", highlightthickness=1, 
                    highlightcolor="black", highlightbackground="black")
        self.ext2.place(x=390, y=250)
        self.browseborder2=Frame(self.canvas, highlightbackground="black",
                        highlightcolor="black", highlightthickness=2,
                        bd=0, relief="solid")
        self.browseborder2.place(x=395, y=290)
        self.browse2=Button(self.browseborder2, font="Arial 15", text="Browse", cursor="hand2", 
                    relief="flat", highlightthickness=1, highlightcolor="black", 
                    highlightbackground="black", border=2, background="white",
                    command=self.outputfile)
        self.browse2.pack(fill=BOTH, ipadx=20)
        self.browse2.bind("<Enter>", lambda _: enter(self.browse2))
        self.browse2.bind("<Leave>", lambda _: leave(self.browse2))

        self.browseborder3=Frame(self.canvas, highlightbackground="black",
                        highlightcolor="black", highlightthickness=2,
                        bd=0, relief="solid")
        self.browseborder3.place(x=75, y=350)
        self.convertbtn=Button(self.browseborder3, font="Arial 18", text="Convert", cursor="hand2", 
                    relief="flat", highlightthickness=1, highlightcolor="black", 
                    highlightbackground="black", border=2, background="white", 
                    command=self.convert)
        self.convertbtn.pack(fill=BOTH, ipadx=20)
        self.convertbtn.bind("<Enter>", lambda _: enter(self.convertbtn))
        self.convertbtn.bind("<Leave>", lambda _: leave(self.convertbtn))
        self.browseborder4=Frame(self.canvas, highlightbackground="black",
                        highlightcolor="black", highlightthickness=2,
                        bd=0, relief="solid")
        self.browseborder4.place(x=320, y=350)
        self.resetbtn=Button(self.browseborder4, font="Arial 18", text="Clear", cursor="hand2", 
                    relief="flat", highlightthickness=1, highlightcolor="black", 
                    highlightbackground="black", border=2, background="white", 
                    command=self.reset)
        self.resetbtn.pack(fill=BOTH, ipadx=27)
        self.resetbtn.bind("<Enter>", lambda _: enter(self.resetbtn))
        self.resetbtn.bind("<Leave>", lambda _: leave(self.resetbtn))

        def enter(button):
            button.config(background="#01D9FF", relief="raised")

        def leave(button):
            button.config(background="white", relief="flat")

if __name__=="__main__":
    root=Window()
    root.createwidgets()
    root.mainloop()
