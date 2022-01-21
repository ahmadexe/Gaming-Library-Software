from tkinter import *
from tkinter.messagebox import showinfo, showerror
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import webbrowser
import smtplib
import random
import sys


box = Tk()
box.geometry("800x450")

lp = ['Valorant', 'Valorant', 'Valorant', 'COD Modern Warfare 2', 'GTA 5', 'GTA 5', 'Watchdogs', 'NFS The Run', 'NFS The Run', 'Battlefiel 1', 'Far Cry 5', 'Far Cry 5', 'Forza Horizon 4', 'Fortnite', 'Fortnite']


l_show = ('Valorant: 3 copies', 'COD Modern Warfare 2: 1 copy','GTA 5: 2 copies', "Watchdogs: 1 copy", 'NFS The Run: 2 copies','Battlefield 1: 1 copy', 'Far Cry 5: 2 copies', 'Forza Horizon 4: 1 copy', 'Fortnite: 2 copies')


futuregames = ("Assassin's Creed Valhalla (2021)", "Resident Evil Village (2021)", "Returnal (2021)", "Far Cry 6 (2022)", "Halo Infinite (2022)")


fgames_backend = ["assassin's creed valhalla", "resident evil village", "returnal", "far cry 6", "halo infinite"]

pc_specs = { 
                "PC Specs" : ["RAM 32gb, 300 Hz Monitor, Processor i7 10th gen or above, Graphic Card 8gb, Available Space 10tb",
                "RAM 16gb, Monitor 100-200 Hz, Processor i5 10th gen or equal, Graphics 4gb, Available Space 1tb",
                "RAM 8gb Monitor 100-200 Hz, Processor i5 10th gen or above, Graphics 2gb, Available Space 1tb",
                "RAM 8gb Monitor 60 Hz, Processor i5 6th generation or equal, Graphics 1-2gb, Available Space 1tb",
                "Lower specs"],


                "Playable Games" : ["All Available Games and future games", 
                "All available games, future games might not be playable",
                "Valorant (High settings), Watchdogs, NFS The Run, Battlefield 1, Fortnite (High settings), future games maybe playable",
                "Valorant (Mid Settings), Watchdogs, NFS The Run, Battlefield 1, Fortnite (High Settings), future games maybe playable",
                "NFS The Run, Watchdogs, Battlefield, no online competitive game and no future game can be played"]}





def sub():
    
    
    f = open("logins.txt", 'a')
    f.write(f"\n{e3v.get()} : {e4v.get()} : {e6v.get()}")
    f.close()
    showinfo("Registration Complete", "Congratulations! Registration was successful. You can now login.\nHappy Gaming.")


def getin():
    f = open('logins.txt', 'r')
    l = f.readlines()
    f.close()
    for line in l:
        if line.split(':')[0].strip() == e1v.get() and line.split(':')[1].strip() == e2v.get() and  line.split(":")[2].strip() == e5v.get():
            global img, imgload, imlbl, pc_specs
            top = Toplevel()
            top.minsize(800,450)
            img = Image.open('back2.png')
            imgload = ImageTk.PhotoImage(img)
            imglbl = Label(top, image = imgload)
            imglbl.place(x = 0, y = 0)


            







            def agame():
                for item in l_show:
                    lt = Label(top, text =f"AVAILABLE {item}", bg = 'black', fg = 'cyan', pady = 3)
                    lt.pack(side = BOTTOM)

            def fgame():
                
                for item in futuregames:
                    l2 = Label(top, text = f"FUTURE GAMES {item}", bg = 'black', fg = 'cyan', pady = 3)
                    l2.pack(side = BOTTOM)
                    

            def dic():
                global pc_specs
                ex = pd.DataFrame(pc_specs)
                
                ex.to_csv("specification.csv")

                showinfo("Task Done!", "You may close the program to view the excel sheet of Games playable on different devices.")
                
    
            def purchase():
                
                if entval.get() in lp:    
                    lp.remove(entval.get())
                    showinfo("Note", "Purchase Complete. Check your email for confirmation.")
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("muahmad710@gmail.com", "incorrect299")
                    server.sendmail("muahmad710@gmail.com", e5.get(), f'''Thanks for purchasing {ent.get()}, 
                    We hope you enjoyed your experience.
                    Please feel free to respond to this email for feedbacks.
                    We value your suggestions.
                    
                    
                    
                    Happy Gaming!
                    Regards,
                    Team PHOB1A Gaming.''')
                    
                
                    
                        
                
                elif entval.get().lower() in fgames_backend:
                    bokcod = random.randint(10000, 99999)
                    x = open('bookingcode.txt', 'a')
                    x.write(f"\n{bokcod}")
                    fgames_backend.remove(entval.get().lower())
                    showinfo('Done', '''Game has been booked, please wait for the official release.
                    A booking code has been sent to your email.''')
                    serverf = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    serverf.login('muahmad710@gmail.com', 'incorrect299')
                    serverf.sendmail('muahmad710@gmail.com', e5.get(), f'''{ent.get()} has been booked!
                    Please wait for the official release.
                    Your booking code is {bokcod}
                    On the official release you can show your booking code.
                    Thank you for shooping.
                    HAPPY GAMING!
                    Regards, 
                    Team PHOB1A Gaming.''')

                else: 
                    showerror("Error", "Either the game isn't available or you typed the name wrong.")
                    server2 = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server2.login('muahmad710@gmail.com', 'incorrect299')
                    server2.sendmail('muahmad710@gmail.com', e5.get(), f'''Sorry {ent.get()} is not availaable at the moment.
                    We apologize!
                    Please purchase something else.
                    Regard's,
                    Team PHOB1A Gaming.''')                   
                
            
            
            def hpc():
                global pc_specs
                hpc_df = pd.DataFrame(pc_specs)
                myval = hpc_df['Playable Games'][0]
                showinfo("Playable Games", f"{myval}, You can view the available games from the top menus")


            def lpc():
                global pc_specs
                lpc_df = pd.DataFrame(pc_specs)
                myvall = lpc_df['Playable Games'][4]
                showinfo("Playable Games", f"{myvall}")



            def mpc():
                global pc_specs
                mpc_df = pd.DataFrame(pc_specs)
                myvalll = mpc_df['Playable Games'][2]
                showinfo("Playable Games", f"{myvalll}")


            def log_out():
                exit()



            def gsearch():
                webbrowser.open('https://google.com/search?q=' + entb.get())



            def ysearch():
                webbrowser.open('https://www.youtube.com/results?search_query=' + entb.get())



            lent = Label(top, text = "Get A Game", bg = 'black', fg = 'cyan', pady = 5)
            lent.place(x = 220, y = 100)
            entval = StringVar()
            ent = Entry(top, textvariable = entval, bg = 'black', fg = 'cyan')
            ent.place(x = 190, y = 130)
            entb_btn = Button(top, text = "BUY GAME!", bg = 'black', fg = 'cyan', borderwidth = 3, command = purchase)
            entb_btn.place(x = 215, y = 160)


            lentb = Label(top, text = "Search A Game", bg = 'black', fg = 'cyan', pady = 5)
            lentb.place(x = 1080, y = 100)
            entvalb = StringVar()
            entb = Entry(top, textvariable = entvalb, bg = 'black', fg = 'cyan')
            entb.place(x = 1060, y = 130)
            entbtna = Button(top, text = "Google Search", bg = 'black', fg = 'cyan', borderwidth = 3, command = gsearch)
            entbtna.place(x = 990, y = 160)
            entbtnb = Button(top, text = "Youtube Search", bg = 'black', fg = 'cyan', borderwidth = 3, command = ysearch)
            entbtnb.place(x = 1165, y = 160)





            btop1 = Button(top, bg = 'black', fg = 'cyan', borderwidth = 0, text = "View Available Games!", command = agame)
            btop1.place(x = 165, y = 10)
            btop2 = Button(top, bg = 'black', fg = 'cyan', borderwidth = 0, text = "View Future Games!", command = fgame)
            btop2.place(x = 320, y = 10)
            btop3 = Button(top, bg = 'black', fg = 'cyan', borderwidth = 0, text = "What can I play?", command =  dic)
            btop3.place(x = 478, y = 10)
            btop4 = Button(top, bg = 'black', fg = 'cyan', borderwidth = 0, text = "Games for high end pc", command = hpc)
            btop4.place(x = 618, y = 10)
            btop5 = Button(top, bg = 'black', fg = 'cyan', borderwidth = 0, text = "Games for mid-spec pc", command = mpc)
            btop5.place(x = 800, y = 10)
            btop6 = Button(top, bg = 'black', fg = 'cyan', borderwidth = 0, text = "Games for low end PC", command = lpc)
            btop6.place(x = 980, y = 10)
            btn7 = Button(top, bg='black',fg='cyan',borderwidth=0,text = 'Logout', command = log_out)
            btn7.place(x=1140, y = 10)




    else:
        pass
            



myimg = Image.open('back1.png')
myimgload = ImageTk.PhotoImage(myimg)
imglabel = Label(box, image = myimgload)
imglabel.place(x = 0, y = 0)


e1v = StringVar()
e2v = StringVar()
e3v = StringVar()
e4v = StringVar()
e5v = StringVar()
e6v = StringVar()


e1 = Entry(box, textvariable = e1v)
e1.place(x = 200, y = 262)
e2 = Entry(box, textvariable = e2v, show = "*")
e2.place(x = 200, y = 318)
e3 = Entry(box, textvariable = e3v)
e3.place(x = 1150, y = 254)
e4 = Entry(box, textvariable = e4v, show = "*")
e4.place(x = 1150, y = 308)
e5 = Entry(box, textvariable = e5v)
e5.place(x = 200, y = 370)
e6 = Entry(box, textvariable = e6v)
e6.place(x=1150, y = 360)



Label(box, text = "E-mail:", font = "lucida 14 bold", bg = 'black', fg = 'white').place(x = 10, y = 370)
Label(box, text = "E-mail:", font = "lucida 14 bold", bg = 'black', fg = 'white').place(x = 973, y = 360)


btn_1 = Button(box, text = "GO!", borderwidth = 4, bg = 'black', fg = 'white', command = getin)
btn_1.place(x = 120 , y = 410)
btn_2 = Button(box, text = "Submit", borderwidth = 4, bg = 'black', fg = 'white', command = sub)
btn_2.place(x = 1100 , y = 410)
box.title("Phobia Gaming")








box.mainloop()




            