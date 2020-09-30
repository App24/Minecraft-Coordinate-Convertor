import tkinter #Tkinter is a module that comes with python
from tkinter.font import * #Prevents doing tkinter.font.Font

def popup(title,_text,_fg="black"):
    toplevel = tkinter.Toplevel()
    #Setting Icon
    icon=tkinter.PhotoImage(file="icon.gif")
    toplevel.tk.call("wm","iconphoto", toplevel._w, icon)
    #Setting Size and prevent the window being resized
    toplevel.title(title)
    toplevel.resizable(width=False, height=False)
    helv24 = Font(family='Helvetica', size=20, weight='bold')
    label1=tkinter.Label(toplevel, text=_text,font=helv24, anchor="center",fg=_fg)
    ok=tkinter.Button(toplevel, text="Ok", command=toplevel.destroy)
    label1.pack()
    ok.pack()

def convert(_x, _z, _dim, _name):
    if _name=="":
        popup("Error","You must input a name!","red")
        return
    if _x == "":
        _x="0"
    if _z == "":
        _z="0"
    #Let 'x' and 'z' be used for overworld coords and 'tempX' and 'tempZ' be for nether coords
    x=float(_x)
    z=float(_z)
    tempX=x
    tempZ=z
    dim=int(_dim)
    if dim==0:
        tempX=x/8
        tempZ=z/8
    elif dim==1:
        x=tempX*8
        z=tempZ*8
    popup("Completion","Done!")
    lines="Overworld:\nX: "+str(x)+"\nZ: "+str(z)+"\nNether:\nX: "+str(tempX)+"\nZ: "+str(tempZ)
    """Stitches all of the variabled together with pretty text
       '\n' means new line"""
    with open(_name+" coords.txt", "w") as f:
        """Opens the file that contains the variable '_name' plus ' coords.txt' in writting mode
           this mode allows for the creation of the file if there is non and rewrites over it
           Look up the different modes for a better understanding"""
        f.writelines(lines)

def validate(char, entry_value):
    chars=entry_value[:-1] #Selects all the text in the textbox except the last character
    if (not char.isdigit() and not "." in char and not "-" in char) or ("." in chars and "." in char) or ("-" in chars and "-" in char):
        """if entered char is not a digit or is not "." or is not "-" then return false.
           If the entered char is "." and there is already a "." in text, return false.
           If the entered char is "-" and there is already a "-" in text, return false"""
        return False
    else:
        return True

def converter():
    root = tkinter.Tk()
    #Setting Icon
    icon=tkinter.PhotoImage(file="icon.gif")
    root.tk.call("wm","iconphoto", root._w, icon)
    #Setting Title
    root.title("Minecraft Coordinates Convertor")
    #Setting Size and prevent the window being resized
    root.geometry('{}x{}'.format(535, 250))
    root.resizable(width=False, height=False)
    #Used to check the inputs for 'entry_x' and 'entry_z'
    vcmd = (root.register(validate), '%S', '%P')
    #Setting font up
    helv24 = Font(family='Helvetica', size=24, weight='bold')

    label_name = tkinter.Label(root, text="Name:", font=helv24)
    label_x = tkinter.Label(root, text="X coord:", font=helv24)
    label_z = tkinter.Label(root, text="Z coord:", font=helv24)
    entry_name = tkinter.Entry(root, font=helv24)
    entry_x = tkinter.Entry(root, validate = 'key', validatecommand = vcmd, font=helv24)
    entry_z = tkinter.Entry(root, validate = 'key', validatecommand = vcmd, font=helv24)
    var=tkinter.IntVar()
    dim = tkinter.Checkbutton(root, text="Nether",variable=var, font=helv24)
    convertB = tkinter.Button(root, text="Convert", command=lambda:convert(entry_x.get(),entry_z.get(),var.get(),entry_name.get()), font=helv24)
    #In this case lambda is used to allow parsing of arguments

    #Placing the different widgets into their place
    label_name.grid(row=0, padx=(42, 10))
    label_x.grid(row=1, padx=(10, 10))
    label_z.grid(row=2, padx=(10, 10))

    entry_name.grid(row=0,column=1, padx=(10,10))
    entry_x.grid(row=1,column=1, padx=(10,10))
    entry_z.grid(row=2,column=1, padx=(10, 10))

    dim.grid(columnspan=3)
    convertB.grid(columnspan=4)

    root.mainloop()

def viewer():
    pass

converter()