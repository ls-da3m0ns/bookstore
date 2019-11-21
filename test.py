from tkinter import *
import backend

#backend to front functions

def get_selected_row(event):
    try:
        index1=list.curselection()[0]
        index=list.get(index1)
        e1.delete(0,END)
        e1.insert(END,index[1])
        e2.delete(0,END)
        e2.insert(END,index[2])
        e3.delete(0,END)
        e3.insert(END,index[3])
        e4.delete(0,END)
        e4.insert(END,index[4])
    except IndexError:
        pass

def veiw_command():
    list.delete(0,END)
    for row in backend.veiw():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
        list.insert(END,row)

def insert_command():
    list.delete(0,END)
    backend.insert(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    list.insert(END,(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))

def delete_command():
    backend.delete(index[0])
    list.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    veiw_command()

def update_command():
    backend.update(index[0],Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    veiw_command()

#def close_command():

window=Tk()
window.wm_title("Bookstore v0.012")

#text feilds

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#value input

Title_text=StringVar()
e1=Entry(window,textvariable=Title_text)
e1.grid(row=0,column=1)

Author_text=StringVar()
e2=Entry(window,textvariable=Author_text)
e2.grid(row=0,column=3)

Year_text=StringVar()
e3=Entry(window,textvariable=Year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

#list and Scrollbar

list=Listbox(window,height=10,width=35)
list.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6)

list.configure(yscrollcommand=sb1.set)
sb1.configure(command=list.yview)
list.bind('<<ListboxSelect>>',get_selected_row)


#buttons

b0=Button(window,text="Veiw All",width=15,command=veiw_command)
b0.grid(row=2,column=3)

b1=Button(window,text="Search Entry",width=15,command=search_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Add Entry",width=15,command=insert_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Refresh",width=15,command=veiw_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update Selected",width=15,command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete",width=15,command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",width=15,command=window.destroy)
b6.grid(row=8,column=3)


window.mainloop()
