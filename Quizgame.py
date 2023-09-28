from tkinter import *
win=Tk()
win.title("Quiz Game")

name=StringVar()
ch=StringVar()

class Score:
    total=20
    score=0
    unsolve=0
    def increase(self,scr):
        self.score=self.score+scr
    def unsolvequest(self,scr):
        self.unsolve=self.unsolve+scr

def start():
    if ((ch.get()=='y' or ch.get()=='Y') and name.get()!=""):
        win.destroy()

        win2=Tk()
        a=IntVar()
        b=IntVar()
        c=IntVar()
        d=IntVar()
        e=IntVar()
        fv=IntVar()
        g=IntVar()
        
        Label(win2,text="Please wait Quiz game will start............",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=8,relief=RAISED).pack(side=TOP,fill=X,pady=9)
        f=Frame(win2,bg="black")
        f.pack(fill=X)
        Label(f,text="Who among the following considered as the 'father of artificial intelligence'?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X)
        Radiobutton(f,text="Charles Babbage",variable=a,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,anchor="w",padx=10)
        Radiobutton(f,text="Lee De Forest",variable=a,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f,text="John McCarthy",variable=a,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        
        f2=Frame(win2,bg="black")
        f2.pack(fill=X)
        Label(f2,text="Select the example of application software of computer:",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X)
        Radiobutton(f2,text="Ms Word",variable=b,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,anchor="w",padx=10)
        Radiobutton(f2,text="Ms Excel",variable=b,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f2,text="Both A and B",variable=b,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

        f3=Frame(win2,bg="black")
        f3.pack(fill=X)
        Label(f3,text="In terms of Computer Networks, what does VPN stands for: ",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
        Radiobutton(f3,text="Verbal Private News",variable=c,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f3,text="virtual Private Network",variable=c,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f3,text="vertical personal network",variable=c,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

        f4=Frame(win2,bg="black")
        f4.pack(fill=X)
        Label(f4,text="What is Oracle?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
        Radiobutton(f4,text="an operating system",variable=d,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f4,text="word processor software",variable=d,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f4,text="Database software",variable=d,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

        f5=Frame(win2,bg="black")
        f5.pack(fill=X)
        Label(f5,text="Which command is used to remove a table from the database in SQL?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
        Radiobutton(f5,text="DELETE TABLE",variable=e,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f5,text="DROP TABLE",variable=e,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f5,text="UNATTACH TABLE",variable=e,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

        f6=Frame(win2,bg="black")
        f6.pack(fill=X)
        Label(f6,text=" Which of the following is not an example of an Operating System?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
        Radiobutton(f6,text=" BSD Unix",variable=fv,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f6,text="Microsoft Office XP",variable=fv,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f6,text="Red Hat Linux",variable=fv,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

        f7=Frame(win2,bg="black",pady=12)
        f7.pack(fill=X)
        Label(f7,text="Which of the following is an example of non-volatile memory?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
        Radiobutton(f7,text="RAM",variable=g,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f7,text="ROM",variable=g,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
        Radiobutton(f7,text="None of the above",variable=g,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)


        def Next():
            win2.destroy()
            win3=Tk()

            h=IntVar()
            i=IntVar()
            j=IntVar()
            k=IntVar()
            l=IntVar()
            m=IntVar()
            n=IntVar()
            o=IntVar()

            f8=Frame(win3,bg="black")
            f8.pack(fill=X)
            Label(f8,text=" bit stands for",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f8,text=" binary digit",variable=h,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f8,text="binary tree  ",variable=h,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f8,text="binary information term ",variable=h,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)


            f9=Frame(win3,bg="black")
            f9.pack(fill=X)
            Label(f9,text="The hexadecimal number system consists of the symbols",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f9,text="0 – 9 , A – F",variable=i,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f9,text=" 0 – 7, A – F",variable=i,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f9,text="None of the above",variable=i,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

            f10=Frame(win3,bg="black")
            f10.pack(fill=X)
            Label(f10,text="Which supercomputer is developed by the Indian Scientists?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f10,text="Param",variable=j,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f10,text="Super 301",variable=j,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f10,text="CRAY YMP",variable=j,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

            f11=Frame(win3,bg="black")
            f11.pack(fill=X)
            Label(f11,text="In binary code, the number 7 is written as -",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f11,text="110",variable=k,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f11,text="111",variable=k,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f11,text="100",variable=k,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

            f12=Frame(win3,bg="black")
            f12.pack(fill=X)
            Label(f12,text=" 'ALU' stands for?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f12,text="Arithmetic Long Unit",variable=l,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f12,text="Arithmetic and Logical Units",variable=l,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f12,text="Around Logical Units",variable=l,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

            f13=Frame(win3,bg="black")
            f13.pack(fill=X)
            Label(f13,text="Which one of the following is not a linear data structure?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f13,text="Array ",variable=m,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f13,text="Binary Tree",variable=m,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f13,text="Queue",variable=m,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

            f14=Frame(win3,bg="black")
            f14.pack(fill=X)
            Label(f14,text="The set of computer programs that manage the hardware/software of a computer is called",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f14,text="Compiler system",variable=n,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f14,text="Operating system",variable=n,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f14,text="None of these",variable=n,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

            f15=Frame(win3,bg="black",pady=12)
            f15.pack(fill=X)
            Label(f15,text="Storage mapping is done by",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
            Radiobutton(f15,text="Compiler",variable=o,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f15,text="Operating system",variable=o,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
            Radiobutton(f15,text="Loader ",variable=o,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)



            def Nextnew():
                win3.destroy()
                win4=Tk()

                p=IntVar()
                q=IntVar()
                r=IntVar()
                sv=IntVar()
                t=IntVar()


                f16=Frame(win4,bg="black")
                f16.pack(fill=X)
                Label(f16,text="Who is the first Indian to win a Nobel Prize?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
                Radiobutton(f16,text="Rabindranath Tagore",variable=p,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f16,text="Karnam Malleswari",variable=p,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f16,text="Rahul Tripathi",variable=p,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

                f17=Frame(win4,bg="black")
                f17.pack(fill=X)
                Label(f17,text="Which country is also known as the ‘Land of Rising Sun’?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
                Radiobutton(f17,text="Japan",variable=q,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f17,text="New Zealand",variable=q,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f17,text="China",variable=q,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

                f18=Frame(win4,bg="black")
                f18.pack(fill=X)
                Label(f18,text="In which country, white elephant is found?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
                Radiobutton(f18,text="India",variable=r,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f18,text="Sri Lanka",variable=r,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f18,text="Thailand",variable=r,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

                f19=Frame(win4,bg="black")
                f19.pack(fill=X)
                Label(f19,text="Which one is the biggest island in the World?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
                Radiobutton(f19,text="blackland",variable=sv,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f19,text="Greenland",variable=sv,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f19,text="Borneo",variable=sv,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)

                f20=Frame(win4,bg="black",pady=12)
                f20.pack(fill=X)
                Label(f20,text="Which one is the largest tropical rain forest in the world?",font="Cambria 12",bg="white",fg="#1E1E1E",borderwidth=5,relief=SUNKEN,padx=2,pady=2).pack(padx=10,pady=10,fill=X,side=TOP,anchor="nw")
                Radiobutton(f20,text="Amazon",variable=t,value=1,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f20,text="Bosawas",variable=t,value=2,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)
                Radiobutton(f20,text="Daintree Rain Forest",variable=t,value=3,font="Cambria 11",bg="#4169E1").pack(side=LEFT,padx=10)


                def Submit():
                    win4.destroy()
                    s=Score()
                    f=open("Game_database.txt","a")
                    f.write(f"{name.get()} \n")
                    if a.get()==3:
                        s.increase(1)
                    if b.get()==3:
                        s.increase(1)
                    if c.get()==2:
                        s.increase(1)
                    if d.get()==3:
                        s.increase(1)
                    if e.get()==2:
                        s.increase(1)
                    if fv.get()==2:
                        s.increase(1)
                    if g.get()==2:
                        s.increase(1)
                    if h.get()==1:
                        s.increase(1)
                    if i.get()==1:
                        s.increase(1)
                    if j.get()==1:
                        s.increase(1)
                    if k.get()==2:
                        s.increase(1)
                    if l.get()==2:
                        s.increase(1)
                    if m.get()==2:
                        s.increase(1)
                    if n.get()==2:
                        s.increase(1)
                    if o.get()==1:
                        s.increase(1)
                    if p.get()==1:
                        s.increase(1)
                    if q.get()==1:
                        s.increase(1)
                    if r.get()==3:
                        s.increase(1)
                    if sv.get()==2:
                        s.increase(1)
                    if t.get()==1:
                        s.increase(1)

                    if a.get()==0:
                        s.unsolvequest(1)
                    if b.get()==0:
                        s.unsolvequest(1)
                    if c.get()==0:
                        s.unsolvequest(1)
                    if d.get()==0:
                        s.unsolvequest(1)
                    if e.get()==0:
                        s.unsolvequest(1)
                    if fv.get()==0:
                        s.unsolvequest(1)
                    if g.get()==0:
                        s.unsolvequest(1)
                    if h.get()==0:
                        s.unsolvequest(1)
                    if i.get()==0:
                        s.unsolvequest(1)
                    if j.get()==0:
                        s.unsolvequest(1)
                    if k.get()==0:
                        s.unsolvequest(1)
                    if l.get()==0:
                        s.unsolvequest(1)
                    if m.get()==0:
                        s.unsolvequest(1)
                    if n.get()==0:
                        s.unsolvequest(1)
                    if o.get()==0:
                        s.unsolvequest(1)
                    if p.get()==0:
                        s.unsolvequest(1)
                    if q.get()==0:
                        s.unsolvequest(1)
                    if r.get()==0:
                        s.unsolvequest(1)
                    if sv.get()==0:
                        s.unsolvequest(1)
                    if t.get()==0:
                        s.unsolvequest(1)
                    win5=Tk()

                    win5.title("Result")
                    win5.configure(bg="black")
                    Label(win5,text="Score Board",font="Cambria 16 bold",bg="#FFD700",padx=5,pady=5,borderwidth=7,relief=RAISED).pack(pady=15,fill=X)
                    Label(win5,text="Your score",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=RAISED).pack(pady=15,fill=X)
                    l1=Label(win5,font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=SUNKEN)
                    l1.config(text=s.score)
                    f.write(f"{s.score}")
                    f.close()
                    l1.pack(pady=15)
                    Label(win5,text="Out of",font="Cambria 14 bold",bg="#ADFF2F",padx=5,pady=5,borderwidth=7,relief=RAISED).pack(pady=15,fill=X)
                    Label(win5,text="20",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=SUNKEN).pack(pady=15)
                    Label(win5,text=f"Number of questions you gave wrong answer",fg="white",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=RAISED).pack(pady=10,fill=X)
                    Label(win5,text=s.total-(s.unsolve+s.score),font="Cambria 14 bold",fg="white",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=SUNKEN).pack(pady=15)
                    Label(win5,text=f"Number of questions you did not attempt",fg="white",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=RAISED).pack(pady=10,fill=X)
                    Label(win5,text=s.unsolve,font="Cambria 14 bold",fg="white",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=SUNKEN).pack(pady=15)
                    
                    def close():
                        win5.destroy()
                    Button(win5,text="Close",command=close,font="Cambria 12 bold",bg="#4169E1",fg="white",width=16,height=2,borderwidth=4,relief=SUNKEN).pack()
                    win5.mainloop()

                Button(win4,text="Submit",command=Submit,font="Cambria 12 bold",bg="#4169E1",fg="white",width=16,height=2,borderwidth=4,relief=SUNKEN).pack()
                win4.configure(bg="#1F1F1F")
                win4.title("3rd Page")
                win4.mainloop()


            Button(win3,text="Next",command=Nextnew,font="Cambria 12 bold",bg="#4169E1",fg="white",width=16,height=2,borderwidth=4,relief=SUNKEN).pack()
            win3.configure(bg="#1F1F1F")
            win3.title("2nd Page")
            win3.mainloop()
        Button(win2,text="Next",command=Next,font="Cambria 14 bold",bg="#4169E1",fg="white",width=16,height=2,borderwidth=4,relief=SUNKEN).pack()

        win2.title("1st Page")
        win2.configure(bg="#1F1F1F")
        win2.mainloop()
    elif ch.get()=="n" or ch.get()=="N":
        win.destroy()
    else:
        win6=Tk()
        win6.title("Error Message !!!!")
        Label(win6,text="Plaese Enter your name and choice for play the game",font="Cambria 14 bold",bg="#54FF9F",fg="black",padx=5,pady=5,borderwidth=7,relief=SUNKEN).pack(pady=10)
        def close():
            win6.destroy()
        Button(win6,text="Close",command=close,font="Cambria 14 bold",bg="#FFD39B",width=16,height=2,borderwidth=4,relief=SUNKEN).pack()
        win6.configure(bg="black")
        win6.mainloop()

f1=Frame(win,bg="#00BFFF",borderwidth=7,relief="raised")
f1.pack(side=TOP,fill="x")
Label(f1,text="------------------------------- Welcome in Quiz ------------------------------",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=SUNKEN).pack(pady=10)

f2=Frame(win,bg="#00BFFF",padx=5,pady=5,borderwidth=7,relief="raised")
f2.pack(pady=35)
Label(f2,text="Enter your name",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=SUNKEN).grid(row=2,column=0,padx=5,pady=5)
Entry(f2,textvariable=name,fg="white",font="Cambria 14 bold",bg="#4169E1",borderwidth=7,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=5)
Label(f2,text="Do you want to play the game or not y/n",font="Cambria 14 bold",bg="#4169E1",padx=5,pady=5,borderwidth=7,relief=SUNKEN).grid(row=3,column=0,padx=5,pady=5)
Entry(f2,textvariable=ch,fg="white",font="Cambria 14 bold",bg="#4169E1",borderwidth=7,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=5)
Button(f2,text="Start",command=start,font="Cambria 14 bold",bg="#4169E1",fg="white",width=16,height=2,borderwidth=7,relief=SUNKEN).grid(row=4,column=0)

win.geometry("1200x1000")
win.title("Quiz Game")
win.configure(bg="#1F1F1F")
win.mainloop()