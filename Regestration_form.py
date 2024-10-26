from linecache import checkcache
import tkinter as tk 
root=tk.Tk()
root.geometry("500x300")
tk.Label(root,text="Regestration Form",font="arial 15 bold").grid(row=0,column=3)

def getvals():
    print("Accepted")

Name=tk.Label(root,text="Enter your name ")
Email=tk.Label(root,text=" Enter your email ")
Phonne_No=tk.Label(root,text="Enter your phone number")
Gender=tk.Label(root,text="Gender")

Name.grid(row=1,column=2)
Email.grid(row=2,column=2)
Phonne_No.grid(row=3,column=2)
Gender.grid(row=4,column=2)

Namevalue=tk.StringVar
Emailvalue=tk.StringVar
Phonne_Novalue=tk.StringVar
Gendervalue=tk.StringVar

Nameentry=tk.Entry(root,textvariable=Namevalue)
Emailentry=tk.Entry(root,textvariable=Emailvalue)
Phonne_Noentry=tk.Entry(root,textvariable=Phonne_Novalue)
Genderentry=tk.Entry(root,textvariable=Gendervalue)

Nameentry.grid(row=1,column=3)
Emailentry.grid(row=2,column=3)
Phonne_Noentry.grid(row=3,column=3)
Genderentry.grid(row=4,column=3)


# checkbutton=tk.Checkbutton(root, text="Remember me?",variable=checkvariable)
checkbutton = tk.Checkbutton(root, text="Remember me?", variable=checkcache)
checkbutton.grid(row=6,column=3)

tk.Button(text="Submit",command=getvals).grid(row=7,column=3)







root.mainloop()