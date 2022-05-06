

from tkinter import *



root= Tk()
root.title("Clerk Dashboard")
root.geometry("600x600+0+0")
root.configure(bg="#d7dae2")



label_1 = Label(root, text = "Welcome!", font = ("Calibri", 16), padx = 20, pady = 30,bg="#d7dae2")
label_1.pack()


frame = Frame(root)

def check_in():
    
    top=Toplevel()
    top.geometry("500x500")
    top.title('check-in')
    Button(top, width=20, text = 'Save',pady=10,fg="blue",command = assign_tribes).pack()


def assign_bunks():
    top=Toplevel()
    top.title('assign-bunks')

def assign_tribes():
    top=Toplevel()
    top.title('assign-tribes')

def save():
    top=Toplevel()
    top.title('Save')

def logout():
    root.destroy()
Button(frame,width =20, text = 'Check In',pady =10,fg="red", command = check_in).pack(side = LEFT)
Button(frame,width =20, text = 'Assign Bunks',pady=10,fg="green",command = assign_bunks).pack(side = LEFT)
Button(frame,width=20, text = 'Assign Tribes',pady=10,fg="blue",command = assign_tribes).pack(side = LEFT)
Button(frame, width=20, text = 'Log out',pady=10,fg="blue",command = assign_tribes).pack(side = LEFT)

frame.pack()




root.mainloop()










