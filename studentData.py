import sys
import mysql.connector
import sys
import math
import smtplib
from tkinter import END
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import studentData_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    studentData_support.set_Tk_var()
    top = Toplevel1 (root)
    studentData_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    studentData_support.set_Tk_var()
    top = Toplevel1 (w)
    studentData_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    

    def showDetails(self):

        math_checked = str(studentData_support.che51.get())
        coa_checked = str(studentData_support.che52.get())
        aoa_checked = str(studentData_support.che53.get())
        cg_checked = str(studentData_support.che54.get())
        os_checked = str(studentData_support.che55.get())
        
        if int(math_checked) == 1:
            self.Listbox1.delete(0,END)
            self.mycursor.execute("SELECT roll_no,name,ut_avg FROM maths WHERE ut_avg<=9")
            self.mydb.commit()
            numrows = int(self.mycursor.rowcount)
            for x in range(0,numrows):
                row = self.mycursor.fetchone()
                self.Listbox1.insert(END, row)
            
        elif int(coa_checked) == 1:
            self.Listbox1.delete(0,END)
            self.mycursor.execute("SELECT roll_no,name,ut_avg FROM coa WHERE ut_avg<=9")
            self.mydb.commit()
            numrows = int(self.mycursor.rowcount)
            for x in range(0,numrows):
                row = self.mycursor.fetchone()
                self.Listbox1.insert(END, row)

        elif int(aoa_checked) == 1:
            self.Listbox1.delete(0,END)
            self.mycursor.execute("SELECT roll_no,name,ut_avg FROM aoa WHERE ut_avg<=9")
            self.mydb.commit()
            numrows = int(self.mycursor.rowcount)
            for x in range(0,numrows):
                row = self.mycursor.fetchone()
                self.Listbox1.insert(END, row)

        elif int(cg_checked) == 1:
            self.Listbox1.delete(0,END)
            self.mycursor.execute("SELECT roll_no,name,ut_avg FROM cg WHERE ut_avg<=9")
            self.mydb.commit()
            numrows = int(self.mycursor.rowcount)
            for x in range(0,numrows):
                row = self.mycursor.fetchone()
                self.Listbox1.insert(END, row)

        elif int(os_checked) == 1:
            self.Listbox1.delete(0,END)
            self.mycursor.execute("SELECT roll_no,name,ut_avg FROM os WHERE ut_avg<=9")
            self.mydb.commit()
            numrows = int(self.mycursor.rowcount)
            for x in range(0,numrows):
                row = self.mycursor.fetchone()
                self.Listbox1.insert(END, row)

        else:
            messagebox.showinfo("Error", "Please check 1 subject ")


    def addDetails(self):
        
        roll_no=int(self.Entry2.get())
        ut1=int(self.Entry3.get())
        ut2=int(self.Entry4.get())
        ut_avg=math.ceil((ut1+ut2)/2)

        math_checked = str(studentData_support.che51.get())
        coa_checked = str(studentData_support.che52.get())
        aoa_checked = str(studentData_support.che53.get())
        cg_checked = str(studentData_support.che54.get())
        os_checked = str(studentData_support.che55.get())

        if int(math_checked) == 1 :
            self.mycursor.execute ("""
           UPDATE maths
           SET ut1=%s, ut2=%s, ut_avg=%s
           WHERE roll_no=%s
            """, (ut1, ut2, ut_avg, roll_no))

            self.mycursor = self.mydb.cursor(dictionary=False, buffered=True)
            self.mycursor.execute("""select * from maths where roll_no=%s""", (roll_no,))
            record = self.mycursor.fetchone()
            name=record[1]
            email_id=record[5]
                
            self.mydb.commit()
            messagebox.showinfo("Success", "Entry done for roll number: " + str(roll_no)) #message

            roll_no=roll_no+1
            self.Entry2.delete("0",END)
            self.Entry2.insert(0,roll_no)
            self.Entry3.delete("0",END)
            self.Entry4.delete("0",END)


            from email.mime.text import MIMEText
            body="Hello "+str(name)+", your score is: "+str(ut_avg)
            msg=MIMEText(body)
            fromaddr="vestudizteam@gmail.com"
            toaddr=email_id
            msg['From']=fromaddr
            msg['To']=toaddr
            msg['subject']="Your Maths UT average score"
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(fromaddr,"17/18fejuniors")
            server.send_message(msg)
            print('Mail sent to: '+str(name))
            server.quit()

        elif int(coa_checked) == 1:
            
            self.mycursor.execute ("""
            UPDATE coa
            SET ut1=%s, ut2=%s, ut_avg=%s
            WHERE roll_no=%s
            """, (ut1, ut2, ut_avg, roll_no))

            self.mycursor = self.mydb.cursor(dictionary=False, buffered=True)
            self.mycursor.execute("""select * from coa where roll_no=%s""", (roll_no,))
            record = self.mycursor.fetchone()
            name=record[1]
            email_id=record[5]
            
            self.mydb.commit()
            messagebox.showinfo("Success", "Entry done for roll number: " + str(roll_no)) #message

            roll_no=roll_no+1
            self.Entry2.delete("0",END)
            self.Entry2.insert(0,roll_no)
            self.Entry3.delete("0",END)
            self.Entry4.delete("0",END)


            from email.mime.text import MIMEText
            body="Hello "+str(name)+", your score is: "+str(ut_avg)
            msg=MIMEText(body)
            fromaddr="vestudizteam@gmail.com"
            toaddr=email_id
            msg['From']=fromaddr
            msg['To']=toaddr
            msg['subject']="Your COA UT average score"
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(fromaddr,"17/18fejuniors")
            server.send_message(msg)
            print('Mail sent....')
            server.quit()
            

        elif int(aoa_checked) == 1:
            self.mycursor.execute ("""
           UPDATE aoa
           SET ut1=%s, ut2=%s, ut_avg=%s
           WHERE roll_no=%s
            """, (ut1, ut2, ut_avg, roll_no))

            self.mycursor = self.mydb.cursor(dictionary=False, buffered=True)
            self.mycursor.execute("""select * from aoa where roll_no=%s""", (roll_no,))
            record = self.mycursor.fetchone()
            name=record[1]
            email_id=record[5]
                
            self.mydb.commit()
            messagebox.showinfo("Success", "Entry done for roll number: " + str(roll_no)) #message

            roll_no=roll_no+1
            self.Entry2.delete("0",END)
            self.Entry2.insert(0,roll_no)
            self.Entry3.delete("0",END)
            self.Entry4.delete("0",END)


            from email.mime.text import MIMEText
            body="Hello "+str(name)+", your score is: "+str(ut_avg)
            msg=MIMEText(body)
            fromaddr="vestudizteam@gmail.com"
            toaddr=email_id
            msg['From']=fromaddr
            msg['To']=toaddr
            msg['subject']="Your AOA UT average score"
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(fromaddr,"17/18fejuniors")
            server.send_message(msg)
            print('Mail sent....')
            server.quit()
                

        elif int(cg_checked) == 1:
            self.mycursor.execute ("""
           UPDATE cg
           SET ut1=%s, ut2=%s, ut_avg=%s
           WHERE roll_no=%s
            """, (ut1, ut2, ut_avg, roll_no))

            self.mycursor = self.mydb.cursor(dictionary=False, buffered=True)
            self.mycursor.execute("""select * from cg where roll_no=%s""", (roll_no,))
            record = self.mycursor.fetchone()
            name=record[1]
            email_id=record[5]
                
            self.mydb.commit()
            messagebox.showinfo("Success", "Entry done for roll number: " + str(roll_no)) #message

            roll_no=roll_no+1
            self.Entry2.delete("0",END)
            self.Entry2.insert(0,roll_no)
            self.Entry3.delete("0",END)
            self.Entry4.delete("0",END)


            from email.mime.text import MIMEText
            body="Hello "+str(name)+", your score is: "+str(ut_avg)
            msg=MIMEText(body)
            fromaddr="vestudizteam@gmail.com"
            toaddr=email_id
            msg['From']=fromaddr
            msg['To']=toaddr
            msg['subject']="Your CG UT average score"
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(fromaddr,"17/18fejuniors")
            server.send_message(msg)
            print('Mail sent....')
            server.quit()
            

        elif int(os_checked) == 1:
            self.mycursor.execute ("""
           UPDATE os
           SET ut1=%s, ut2=%s, ut_avg=%s
           WHERE roll_no=%s
            """, (ut1, ut2, ut_avg, roll_no))

            self.mycursor = self.mydb.cursor(dictionary=False, buffered=True)
            self.mycursor.execute("""select * from os where roll_no=%s""", (roll_no,))
            record = self.mycursor.fetchone()
            name=record[1]
            email_id=record[5]
                
            self.mydb.commit()
            messagebox.showinfo("Success", "Entry done for roll number: " + str(roll_no)) #message

            roll_no=roll_no+1
            self.Entry2.delete("0",END)
            self.Entry2.insert(0,roll_no)
            self.Entry3.delete("0",END)
            self.Entry4.delete("0",END)


            from email.mime.text import MIMEText
            body="Hello "+str(name)+", your score is: "+str(ut_avg)
            msg=MIMEText(body)
            fromaddr="vestudizteam@gmail.com"
            toaddr=email_id
            msg['From']=fromaddr
            msg['To']=toaddr
            msg['subject']="Your OS UT average score"
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(fromaddr,"17/18fejuniors")
            server.send_message(msg)
            print('Mail sent....')
            server.quit()
            

        else:
            messagebox.showinfo("Error", "Please check 1 subject")

        
            
            
    def __init__(self, top=None):
        self.mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="",
              database="pythonproject",
              
            )
        
        self.mycursor = self.mydb.cursor(dictionary=False, buffered=True)
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 10"
        font16 = "TkDefaultFont"
        font9 = "-family {Segoe UI} -size 9"

        top.geometry("643x696+363+0")
        top.title("Internal Assessment Record by Kunal & Anish")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.configure(takefocus="1")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.124, rely=0.029, relheight=0.366
                , relwidth=0.801)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=515)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.078, rely=0.706, height=25, width=94)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Century} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''UT 1 Marks''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.524, rely=0.706, height=25, width=94)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Century} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''UT 2 Marks''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.252, rely=0.392, height=25, width=112)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Century} -size 13")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Roll Number''')

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.505, rely=0.392,height=25, relwidth=0.117)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.311, rely=0.706,height=20, relwidth=0.117)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=64)

        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry4.place(relx=0.757, rely=0.706,height=20, relwidth=0.117)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=84)

        self.maths_checked = tk.Checkbutton(self.Frame1)
        self.maths_checked.place(relx=0.155, rely=0.078, relheight=0.098
                , relwidth=0.12)
        self.maths_checked.configure(activebackground="#ececec")
        self.maths_checked.configure(activeforeground="#000000")
        self.maths_checked.configure(background="#ffffff")
        self.maths_checked.configure(disabledforeground="#a3a3a3")
        self.maths_checked.configure(foreground="#000000")
        self.maths_checked.configure(highlightbackground="#d9d9d9")
        self.maths_checked.configure(highlightcolor="black")
        self.maths_checked.configure(justify='left')
        self.maths_checked.configure(text='''AM-IV''')
        self.maths_checked.configure(variable=studentData_support.che51)
        '''if(self.maths_checked.select()):
            studentData_support.che52.set(False)
            studentData_support.che53.set(False)
            studentData_support.che54.set(False)
            studentData_support.che55.set(False)'''
        

        self.coa_checked = tk.Checkbutton(self.Frame1)
        self.coa_checked.place(relx=0.33, rely=0.078, relheight=0.098
                , relwidth=0.103)
        self.coa_checked.configure(activebackground="#ececec")
        self.coa_checked.configure(activeforeground="#000000")
        self.coa_checked.configure(background="#ffffff")
        self.coa_checked.configure(disabledforeground="#a3a3a3")
        self.coa_checked.configure(foreground="#000000")
        self.coa_checked.configure(highlightbackground="#d9d9d9")
        self.coa_checked.configure(highlightcolor="black")
        self.coa_checked.configure(justify='left')
        self.coa_checked.configure(text='''COA''')
        studentData_support.che52.set(False)
        self.coa_checked.configure(variable=studentData_support.che52)

        self.aoa_checked = tk.Checkbutton(self.Frame1)
        self.aoa_checked.place(relx=0.485, rely=0.078, relheight=0.098
                , relwidth=0.103)
        self.aoa_checked.configure(activebackground="#ececec")
        self.aoa_checked.configure(activeforeground="#000000")
        self.aoa_checked.configure(background="#ffffff")
        self.aoa_checked.configure(disabledforeground="#a3a3a3")
        self.aoa_checked.configure(foreground="#000000")
        self.aoa_checked.configure(highlightbackground="#d9d9d9")
        self.aoa_checked.configure(highlightcolor="black")
        self.aoa_checked.configure(justify='left')
        self.aoa_checked.configure(text='''AOA''')
        studentData_support.che53.set(False)
        self.aoa_checked.configure(variable=studentData_support.che53)

        self.cg_check = tk.Checkbutton(self.Frame1)
        self.cg_check.place(relx=0.66, rely=0.078, relheight=0.098
                , relwidth=0.085)
        self.cg_check.configure(activebackground="#ececec")
        self.cg_check.configure(activeforeground="#000000")
        self.cg_check.configure(background="#ffffff")
        self.cg_check.configure(disabledforeground="#a3a3a3")
        self.cg_check.configure(foreground="#000000")
        self.cg_check.configure(highlightbackground="#d9d9d9")
        self.cg_check.configure(highlightcolor="black")
        self.cg_check.configure(justify='left')
        self.cg_check.configure(text='''CG''')
        studentData_support.che54.set(False)
        self.cg_check.configure(variable=studentData_support.che54)

        self.os_checked = tk.Checkbutton(self.Frame1)
        self.os_checked.place(relx=0.816, rely=0.078, relheight=0.098
                , relwidth=0.083)
        self.os_checked.configure(activebackground="#ececec")
        self.os_checked.configure(activeforeground="#000000")
        self.os_checked.configure(background="#ffffff")
        self.os_checked.configure(disabledforeground="#a3a3a3")
        self.os_checked.configure(foreground="#000000")
        self.os_checked.configure(highlightbackground="#d9d9d9")
        self.os_checked.configure(highlightcolor="black")
        self.os_checked.configure(justify='left')
        self.os_checked.configure(text='''OS''')
        studentData_support.che55.set(False)
        self.os_checked.configure(variable=studentData_support.che55)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.295, rely=0.46, height=35, width=74)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Century} -size 13")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(takefocus="0")
        self.Button1.configure(command=self.addDetails,text='''Submit''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.171, rely=0.546, relheight=0.409
                , relwidth=0.677)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=435)

        self.Listbox1 = tk.Listbox(self.Frame2)
        self.Listbox1.place(relx=0.023, rely=0.035, relheight=0.919
                , relwidth=0.952)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font16)
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=414)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.591, rely=0.46, height=35, width=100)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Century} -size 13")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.showDetails,text='''Failed List''')

        self.menubar = tk.Menu(top, font=('Segoe UI', 9, ), bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.che51 = tk.IntVar()
        self.che52 = tk.IntVar()
        self.che53 = tk.IntVar()
        self.che54 = tk.IntVar()
        self.che55 = tk.IntVar()

if __name__ == '__main__':
    vp_start_gui()





