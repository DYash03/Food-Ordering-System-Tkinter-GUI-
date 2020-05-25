from tkinter import *
import random as rand
import os.path
import smtplib
import base64
class food:
    scr=Tk()
    global i1,i2,i3,i4,i5,i6,i7,i8
    i1=IntVar()
    i2=IntVar()
    i3=IntVar()
    i4=IntVar()
    i5=IntVar()
    i6=IntVar()
    i7=IntVar()
    i8=IntVar()
    scr.title("FOOD NATION")
    canvas = Canvas(width=2000,height=2000)
    canvas.pack()
    photo = PhotoImage(file='C:\\Users\\hp\\Desktop\\tkinter\\food.png')
    canvas.create_image(250,1 , image=photo ,anchor=NW)
    
    l=Label(scr,text="EMAIL",bg="blue",fg="black",font=('time','20','bold'))
    l.place(x=357,y=548)
    l1=Label(scr,text="Ph No.",bg="blue",fg="black",font=('time','20','bold'))
    l1.place(x=357,y=598)
    l2=Label(scr,text="OTP",bg="red",fg="black",font=('time','15','bold'))
    l2.place(x=417,y=678)
    e=Entry(scr,bg="silver",fg="black")
    e.config(font=('Time','20','bold'))
    e.place(x=477,y=548)
    e1=Entry(scr,bg="silver",fg="black")
    e1.config(font=('time','20','bold'))
    e1.place(x=477,y=598)
    e2=Entry(scr,bg="silver",fg="black")
    e2.config(font=('Time','15','bold'))
    e2.place(x=517,y=678)
    b=Button(scr,text="SEND OTP",bg="powder blue",fg="black")
    b.place(x=815,y=598)
    b.config(font=('Time','12','bold'))
    b1=Button(scr,text="VERIFY",bg="Green",fg="black")
    b1.place(x=815,y=678)
    b1.config(font=('Time','12','bold'))
    b.config(command=lambda:food.otp())
    b1.config(command=lambda:food.verify())

    def otp():
        food.x=food.e.get()
        b=""
        for i in range(0,6):
            b=b+str(rand.randint(0,9))
            food.b=b
        content="GREETINGS!!"+"\n"+"THIS IS FOOD NATION " + "\n\n" +"Your OTP is :" + b
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('sender email','password')
        mail.sendmail('sender email',food.x,content)
        mail.close()

    def verify():
        a=food.e2.get()
        c="INVALID OTP"
        if(a==food.b):
            scr1=Toplevel()
            scr1.configure(bg="#9400D3")
            l=Label(scr1,text="FOOD NATION",bg="indigo",fg="yellow",font=('time','70','bold'))
            l.place(x=400,y=1)
            l1=Label(scr1,text="Pizza & Burger",bg="indigo",fg="aqua",font=('time','25','bold'))
            l1.place(x=580,y=130)
            l2=Label(scr1,text="SMALL",bg="indigo",fg="blue",font=('time','20','bold'))
            l2.place(x=450,y=200)
            l3=Label(scr1,text="LARGE",bg="indigo",fg="blue",font=('time','20','bold'))
            l3.place(x=850,y=200)
            l4=Label(scr1,text="QUANTITY",bg="indigo",fg="blue",font=('time','20','bold'))
            l4.place(x=1250,y=200)
            l5=Label(scr1,text="Cheese n Tomato",bg="indigo",fg="red",font=('time','15','bold'))
            l5.place(x=5,y=280)
            l6=Label(scr1,text="Cheese n Corn",bg="indigo",fg="red",font=('time','15','bold'))
            l6.place(x=5,y=320)
            l7=Label(scr1,text="Cheese n Capsicum",bg="indigo",fg="red",font=('time','15','bold'))
            l7.place(x=5,y=360)
            l8=Label(scr1,text="Fresh Veggie",bg="indigo",fg="red",font=('time','15','bold'))
            l8.place(x=5,y=400)
            l9=Label(scr1,text="Veg Paradise",bg="indigo",fg="red",font=('time','15','bold'))
            l9.place(x=5,y=440)
            l10=Label(scr1,text="Veg Burger",bg="indigo",fg="silver",font=('time','15','bold'))
            l10.place(x=5,y=520)
            l11=Label(scr1,text="Cheese Burger",bg="indigo",fg="silver",font=('time','15','bold'))
            l11.place(x=5,y=560)
            l11=Label(scr1,text="Paneer Burger",bg="indigo",fg="silver",font=('time','15','bold'))
            l11.place(x=5,y=600)
            l12=Label(scr1,text="Delivery Address",bg="indigo",fg="aqua",font=('time','40','bold'))
            l12.place(x=5,y=650)
            l13=Label(scr1,text="NAME",bg="indigo",fg="aqua",font=('time','30','bold'))
            l13.place(x=600,y=730)
            text=Text(scr1,width=50,height=2,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
            text.place(x=500,y=650)
            text1=Text(scr1,width=21,height=1,wrap=WORD,font=('Time','30','bold'),selectbackground="grey")
            text1.place(x=787,y=730)
            b=Button(scr1,text="ORDER",bg="yellow",fg="Black",font=('Time','25','bold'),command=lambda:order())
            b.place(x=1320,y=650)
            b1=Button(scr1,text="SEE BILL",bg="green",fg="Black",font=('Time','18','bold'),command=lambda:food.bill())
            b1.place(x=1320,y=730)
            
            
            r1=Radiobutton(scr1, text="Rs.100",bg="black",fg="red",font=('Time','10','bold'),value=100,variable=i1)
            r1.place(x=460,y=270)
            r2=Radiobutton(scr1, text="Rs.180",bg="black",fg="red",font=('Time','10','bold'),value=180,variable=i1)
            r2.place(x=860,y=270)
            r3=Radiobutton(scr1, text="Rs.100",bg="black",fg="red",font=('Time','10','bold'),value=100,variable=i2)
            r3.place(x=460,y=310)
            r4=Radiobutton(scr1, text="Rs.180",bg="black",fg="red",font=('Time','10','bold'),value=180,variable=i2)
            r4.place(x=860,y=310)
            r5=Radiobutton(scr1, text="Rs.100",bg="black",fg="red",font=('Time','10','bold'),value=100,variable=i3)
            r5.place(x=460,y=350)
            r6=Radiobutton(scr1, text="Rs.180",bg="black",fg="red",font=('Time','10','bold'),value=180,variable=i3)
            r6.place(x=860,y=350)
            r7=Radiobutton(scr1, text="Rs.150",bg="black",fg="red",font=('Time','10','bold'),value=150,variable=i4)
            r7.place(x=460,y=390)
            r8=Radiobutton(scr1, text="Rs.280",bg="black",fg="red",font=('Time','10','bold'),value=280,variable=i4)
            r8.place(x=860,y=390)
            r9=Radiobutton(scr1, text="Rs.200",bg="black",fg="red",font=('Time','10','bold'),value=200,variable=i5)
            r9.place(x=460,y=430)
            r10=Radiobutton(scr1, text="Rs.380",bg="black",fg="red",font=('Time','10','bold'),value=380,variable=i5)
            r10.place(x=860,y=430)
            r11=Radiobutton(scr1, text="Rs.100",bg="black",fg="red",font=('Time','10','bold'),value=100,variable=i6)
            r11.place(x=660,y=510)
            r12=Radiobutton(scr1, text="Rs.120",bg="black",fg="red",font=('Time','10','bold'),value=120,variable=i7)
            r12.place(x=660,y=550)
            r13=Radiobutton(scr1, text="Rs.150",bg="black",fg="red",font=('Time','10','bold'),value=150,variable=i8)
            r13.place(x=660,y=590)
            food.s=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s.place(x=1270,y=270)
            food.s1=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s1.place(x=1270,y=310)
            food.s2=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s2.place(x=1270,y=350)
            food.s3=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s3.place(x=1270,y=390)
            food.s4=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s4.place(x=1270,y=430)
            food.s5=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s5.place(x=1270,y=510)
            food.s6=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s6.place(x=1270,y=550)
            food.s7=Scale(scr1,orient=HORIZONTAL,from_=0,to=20,resolution=1,length=100,width=10,bg="black",fg="red")
            food.s7.place(x=1270,y=590)
               
             
            
                
            def order():
                t=" "
                t1=" "
                t=text.get(0.0,"end")
                t1=text1.get(0.0,"end")
                completeName = os.path.join("D:\\Food nation",food.c+".txt")
                file= open(completeName, "r")
                det=file.read()
                file.seek(0)
                file.close()
                content="\n"+"New order received from "+t1+"\n"+"To:"+"\n"+t+"\n"+"Order id: "+food.c+"\n"+"Order Details are:"+"\n"+det
                content1="Order Received Successfully"+"\n"+"Order id: "+food.c+"\n"+"Order Details are:"+"\n"+det+"\n"+"Your order will be delivered as soon as possible. Hope you will enjoy our service and thanks for providing us a favour to help you ."+"\n"+"Have a great day Today."
                mail=smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('sender email','password')
                mail.sendmail('sender email',"email of company receving order",content)
                mail.close()
                mail1=smtplib.SMTP('smtp.gmail.com',587)
                mail1.ehlo()
                mail1.starttls()
                mail1.login('sender email','password')
                mail1.sendmail('sender email',food.x,content1)
                mail1.close()


            

        else:
            food.e2.delete(0,END)
            food.e2.insert(100,c)


    def bill():
        a=""
        for i in range(0,12):
            a=a+str(rand.randint(0,9))
            food.c=a
        cnt="Cheese and Tomato Pizza"
        cnc="Cheese and Corn Pizza"
        cnc1="Cheese and Capsicum Pizza"
        fv="Fresh Veggie"
        vp="Veg Paradise"
        vb="Veg Burger"
        cb="Cheese Burger"
        pb="Paneer Burger"
        slider=IntVar()
        slider=food.s.get()
        slider1=IntVar()
        slider1=food.s1.get()
        slider2=IntVar()
        slider2=food.s2.get()
        slider3=IntVar()
        slider3=food.s3.get()
        slider4=IntVar()
        slider4=food.s4.get()
        slider5=IntVar()
        slider5=food.s5.get()
        slider6=IntVar()
        slider6=food.s6.get()
        slider7=IntVar()
        slider7=food.s7.get()
        food.i1=IntVar()
        completeName = os.path.join("D:\\Food nation",a+".txt")
        file1 = open(completeName, "w")
        if(slider!=0)&((i1.get()==100)|(i1.get()==180)):
            file1.write(cnt)
            file1.write("\t\t")
            file1.write(str(slider))
            file1.write("\tx ")
            if(i1.get()==100):
                file1.write("\t100\n")
            elif(food.i1.get()==180):
                file1.write("\t180\n")
        if(slider1!=0)&((i2.get()==100)|(i2.get()==180)):
            file1.write(cnc)
            file1.write("\t\t")
            file1.write(str(slider1))
            file1.write("\tx ")
            if(i2.get()==100):
                file1.write("\t100\n")
            elif(i2.get()==180):
                file1.write("\t180\n")
        if(slider2!=0)&((i3.get()==100)|(i3.get()==180)):
            file1.write(cnc1)
            file1.write("\t")
            file1.write(str(slider2))
            file1.write("\tx ")
            if(i3.get()==100):
                file1.write("\t100\n")
            elif(i3.get()==180):
                file1.write("\t180\n")
        if(slider3!=0)&((i4.get()==150)|(i4.get()==280)):
            file1.write(fv)
            file1.write("\t\t\t")
            file1.write(str(slider3))
            file1.write("\tx ")
            if(i4.get()==150):
                file1.write("\t150\n")
            elif(i4.get()==280):
                file1.write("\t280\n")
        
        if(slider4!=0)&((i5.get()==200)|(i5.get()==380)):
            file1.write(vp)
            file1.write("\t\t\t")
            file1.write(str(slider4))
            file1.write("\tx ")
            if(i5.get()==200):
                file1.write("\t200\n")
            elif(i5.get()==380):
                file1.write("\t380\n")
        if(slider5!=0)&((i6.get()==100)):
            file1.write(vb)
            file1.write("\t\t\t")
            file1.write(str(slider5))
            file1.write("\tx ")
            if(i6.get()==100):
                file1.write("\t100\n")
        if(slider6!=0)&((i7.get()==120)):
            file1.write(cb)
            file1.write("\t\t\t")
            file1.write(str(slider6))
            file1.write("\tx ")
            if(i7.get()==120):
                file1.write("\t120\n")
        if(slider7!=0)&((i8.get()==150)):
            file1.write(pb)
            file1.write("\t\t\t")
            file1.write(str(slider7))
            file1.write("\tx ")
            if(i8.get()==150):
                file1.write("\t150\n")
        total=slider*i1.get()+slider1*i2.get()+slider2*i3.get()+slider3*i4.get()+slider4*i5.get()+slider5*i6.get()+slider6*i7.get()+slider7*i8.get()
        if(total<=500):
            total=total+50
            file1.write("DELIVERY CRGS: \t Rs.50\n")
        else:
            file1.write("DELIVERY CRGS: \t Rs.00\n")
        file1.write("TOTAL : \t\t Rs.")
        file1.write(str(total))
        file1.close() 
        completeName = os.path.join("D:\\Food nation",a+".txt")
        file= open(completeName, "r")
        bil=file.read()
        file.seek(0)
        file.close()
        scr2=Toplevel()
        l=Label(scr2,text=bil,bg="blue",fg="black",font=('time','40','bold'))
        l.place(x=25,y=100)    




    
