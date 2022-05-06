from tkinter import *
from tkinter import messagebox
import os
import sqlite3 as sl

#PATH = r"C:/Users/koahn/Desktop/ITM360Sandbox/TermProjectArea"
#os.chdir(PATH)
#password_file = 'password.txt'

#connection = sl.connect('GilaBreathDB')

root =Tk()

rt = Tk()




# Application submission command
def submit_app():
    '''
     shows user successful messagebox for sucessfully submittin
    '''
    messagebox.showinfo('Application submitted successfully!')




def build_Application():
    '''
    gathering application data using GUI
    Requirements:
    - should only be able to gather up to 72 applications
    - should gather name, gender, age, bunking
    preferences, required forms filled , mailing date
    payment confirmation(or not)
    '''

    root.geometry("500x500")
    root.title("Gila Breath Camp Application")

    # Creating application form label
    label_applicaiton = Label(root, text='Gila Breath Applicaiton Form',
                              font=('Modern No. 20', 20), padx = 1, pady = 1)
    label_applicaiton.grid(row=1, column=4)

    #Creating application instructions
    instructions_txt = 'Please fill out the following information to \napply for the Gila Breath Camp. This form' \
                       ' should\n be completed at least two months prior to the camps start date. '
    label_app_instructions = Label(root, text=instructions_txt,
                                   font=('Calibri', 10))
    label_app_instructions.grid(row=2, column=4, padx=1, pady=1)

    # Create Frame for parent information

    ParentInfo_Section = Label(root, text='Enter Parental Information Here ----------------------')
    ParentInfo_Section.grid(row=3, column=1, padx=3, pady=3)

    #EmergencyContact_Section = Label(root, text='Enter  Emergency Contact Information Here ------------------')
    #EmergencyContact_Section.grid(row=7, column=1, padx=3, pady=3)

    #MedicalInfo_Section = Label(root, text='Enter  Emergency Contact Information Here --------------------')
    #MedicalInfo_Section.grid(row=10, column=1, padx=3, pady=3)

    ChildInfo_Section = Label(root, text='Enter Childs Information Here ------------------')
    ChildInfo_Section.grid(row=13, column=1, padx=1, pady=1)

    # Creating labels for entry fields
    ParentFName_entrylabel = Label(root, text= 'First Name: ')
    ParentFName_entrylabel.grid(row=4, column=1, padx=1, pady=1)

    ParentLName_entrylabel = Label(root, text='Last Name: ')
    ParentLName_entrylabel.grid(row=4, column=3, padx=1, pady=1)

    ParentSuffix_entrylabel = Label(root, text='Suffix: ')
    ParentSuffix_entrylabel.grid(row=4, column=5, padx=1, pady=1)

    ParentType_entrylabel = Label(root, text='Parent Type: ')
    ParentType_entrylabel.grid(row=5, column=1, padx=1, pady=1)

    ParentGender_entrylabel = Label(root, text='Parent Gender: ')
    ParentGender_entrylabel.grid(row=5, column=3, padx=1, pady=1)

    ParentEmail_entrylabel = Label(root, text='Parent Email: ')
    ParentEmail_entrylabel.grid(row=6, column=1, padx=1, pady=1)

    ParentPhoneNum_entrylabel = Label(root, text='Parent Phone Number: ')
    ParentPhoneNum_entrylabel.grid(row=6, column=3, padx=1, pady=1)

    ParentAddrNum_entrylabel = Label(root, text='Parent Street Address Number: ')
    ParentAddrNum_entrylabel.grid(row=6, column=5, padx=1, pady=1)

    ParentAddrStreet_entrylabel = Label(root, text='Parent Street Address Name: ')
    ParentAddrStreet_entrylabel.grid(row=7, column=5, padx=1, pady=1)
    '''
    EmerContFName_entryLabel = Label(root, text='First Name: ')
    EmerContFName_entryLabel.grid(row=8, column=1, padx=1, pady=1)

    EmerContLName_entryLabel = Label(root, text='Last Name: ')
    EmerContLName_entryLabel.grid(row=8, column=3, padx=1, pady=1)

    EmerContHPhone_entryLabel = Label(root, text='Home Phone #: ')
    EmerContHPhone_entryLabel.grid(row=9, column=1, padx=1, pady=1)

    EmerContWPhone_entryLabel = Label(root, text='Work Phone: ')
    EmerContWPhone_entryLabel.grid(row=9, column=3, padx=1, pady=1)

    EmerContRelation_entryLabel = Label(root, text='Relation to Child:  ')
    EmerContRelation_entryLabel.grid(row=9, column=5, padx=1, pady=1)

    InsCoName_entryLabel = Label(root, text='Insurance Company Name: ')
    InsCoName_entryLabel.grid(row=11, column=1, padx=1, pady=1)

    InsPolicyNum_entryLabel = Label(root, text='Insurance Policy Number: ')
    InsPolicyNum_entryLabel.grid(row=11, column=3, padx=1, pady=1)

    PrimaryPhysician_entryLabel = Label(root, text='Primary Physician: ')
    PrimaryPhysician_entryLabel.grid(row=11, column=5, padx=1, pady=1)

    PhysicianPhoneNum_entryLabel = Label(root, text='Physcian Phone Number: ')
    PhysicianPhoneNum_entryLabel.grid(row=12, column=1, padx=1, pady=1)

    MedicalIssues_entryLabel = Label(root, text='Medical Issues: ')
    MedicalIssues_entryLabel.grid(row=12, column=3, padx=1, pady=1)
    '''
    ChildFName_entryLabel = Label(root, text='First Name: ')
    ChildFName_entryLabel.grid(row=14, column=1, padx=1, pady=1)

    ChildLName_entryLabel = Label(root, text='Last Name: ')
    ChildLName_entryLabel.grid(row=14, column=3, padx=1, pady=1)

    ChildSex_entryLabel = Label(root, text='Sex: ')
    ChildSex_entryLabel.grid(row=14, column=5, padx=1, pady=1)

    ChildBirthDate_entryLabel = Label(root, text='Birth Date (dd-mm-yyyy): ')
    ChildBirthDate_entryLabel.grid(row=15, column=1, padx=1, pady=1)

    ChildGroupPref_entryLabel = Label(root, text='Grouping Preferences: ')
    ChildGroupPref_entryLabel.grid(row=15, column=3, padx=1, pady=1)

    # Creating input fields
    FName_Entry = Entry(root)
    FName_Entry.grid(row=4, column=2, padx=1, pady=1)

    LName_Entry = Entry(root)
    LName_Entry.grid(row=4, column=4, padx=1, pady=1)

    Suffix_Entry = Entry(root)
    Suffix_Entry.grid(row=4, column=6, padx=1, pady=1)

    ParentType_Entry = Entry(root)
    ParentType_Entry.grid(row=5, column=2, padx=1, pady=1)

    ParentGender_Entry = Entry(root)
    ParentGender_Entry.grid(row=5, column=4, padx=1, pady=1)

    ParentEmail_Entry = Entry(root)
    ParentEmail_Entry.grid(row=6, column=2, padx=1, pady=1)

    ParentPhone_Entry = Entry(root)
    ParentPhone_Entry.grid(row=6, column=4, padx=1, pady=1)

    ParentAddyNum_Entry = Entry(root)
    ParentAddyNum_Entry.grid(row=6, column=6, padx=1, pady=1)

    ParentAddyStreet_Entry = Entry(root)
    ParentAddyStreet_Entry.grid(row=7, column=6, padx=1, pady=1)
    '''
    EmerContFName_Entry = Entry(root)
    EmerContFName_Entry.grid(row=8, column=2, padx=1, pady=1)

    EmerContLName_Entry = Entry(root)
    EmerContLName_Entry.grid(row=8, column=4, padx=1, pady=1)

    EmerContHPhone_Entry = Entry(root)
    EmerContHPhone_Entry.grid(row=9, column=2, padx=1, pady=1)

    EmerContWPhone_Entry = Entry(root)
    EmerContWPhone_Entry.grid(row=9, column=4, padx=1, pady=1)

    EmerContRelation_Entry = Entry(root)
    EmerContRelation_Entry.grid(row=9, column=6, padx=1, pady=1)

    InsCoName_Entry = Entry(root)
    InsCoName_Entry.grid(row=11, column=2, padx=1, pady=1)

    InsCoPolicyNum_Entry = Entry(root)
    InsCoPolicyNum_Entry.grid(row=11, column=4, padx=1, pady=1)

    PrimaryPhysician_Entry = Entry(root)
    PrimaryPhysician_Entry.grid(row=11, column=6, padx=1, pady=1)

    PhysicianPhoneNum_Entry = Entry(root)
    PhysicianPhoneNum_Entry.grid(row=12, column=2, padx=1, pady=1)

    MedicalIssues_Entry = Entry(root)
    MedicalIssues_Entry.grid(row=12, column=4, padx=1, pady=1)
    '''
    ChildFName_Entry = Entry(root)
    ChildFName_Entry.grid(row=14, column=2, padx=1, pady=1)

    ChildLName_Entry = Entry(root)
    ChildLName_Entry.grid(row=14, column=4, padx=1, pady=1)

    ChildSex_Entry = Entry(root)
    ChildSex_Entry.grid(row=14, column=6, padx=1, pady=1)

    ChildBirthDate_Entry = Entry(root)
    ChildBirthDate_Entry.grid(row=15, column=2, padx=1, pady=1)

    ChildGroupPref_Entry = Entry(root)
    ChildGroupPref_Entry.grid(row=15, column=4, padx=1, pady=1)

    # Create the form buttons

    Next_Button = Button(root, text='Next Page', height='4', width='10')
    Next_Button.grid(row=18, column=5, padx=2, pady=2)

    Save_Button = Button(root, text='Save', height=4, width='10')
    Save_Button.grid(row=18, column=6, padx=2, pady=2)

    Submit_Button = Button(root, text='Submit \nApplication', height=4, width=10)
    Submit_Button.grid(row=18, column=7, padx=2, pady=2)
#Devin Greenhalgh's code--------------------------------------------

def build_CustomerDash():
    '''
    a
    '''

    root = Tk()
    #maybe you have to create your own variable for Tk()
    root.geometry('500x500')
    root.title('Customer Dashboard')

    load=Image.open('Users\devin\Pictures\Tatooart\Tatoo.jpg')
    render= ImageTk.PhotoImage(load)
    img=Label(root, image= render)
    img.place(x=0, y=0)


    CustDash_frame = LabelFrame(root, text='Dashboard', font=('Modern No. 20', 20))
    CustDash_frame.grid(row=1, column=3)

    def logout():
        root.destroy()

    def info_page():
        build_Application()
    def status():
        top=Toplevel()
        top.title('Your Status')


    Apply_button = Button(root, text='Apply Here', relief='ridge', bd=5, height=3, width=10, padx=2, pady=4, command=info_page)
    Apply_button.place(x=150, y=100)

    logout_but = Button(root, text='logout', relief='ridge', bd=5, height=3, width=10, padx=2, pady=4, command=logout)
    logout_but.place(x=265, y=100)

# figure out how to apply database to results-------------------
    frame_1=LabelFrame(root, text='Number of campers needed')
    frame_1.place(x=175, y=250)

    inside=Label(frame_1, text='Hi there pal')
    inside.pack()


build_CustomerDash()

root.mainloop()
#DG---------------------------------------------------------------------------------------------------------------

# Ruth Clerk Dashboard code


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


