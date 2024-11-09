#GUI FOR ENCRYPT AND DECRYPT

from  tkinter import *
from tkinter import messagebox
import base64

screen=Tk()
screen.geometry("1080x1080")
screen.title("Encode And Decode")
screen.configure(bg="black")

def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("850x650")
        screen1.configure(bg="pink")
        
        #Encryption process.
        message=text1.get(1.0,END) #(1.0,END) means that fetch from  first line and 0 char to end char.
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        print(message)
        
        Label(screen1,text="Your text is encrypted ",font="impack 10 bold").place(x=5,y=6)
        Label(print(message))
        text2=Text(screen1,font="30",bd=4,wrap=WORD)
        print(message)
        text2.place(x=2,y=30,width=490,height=280)
        text2.insert(END,encrypt)
        print(message)
    elif(password==""):
        messagebox.showerror("ERROR","Please enter the secret key")
    elif(password!="1234"):
        messagebox.showerror("ERROR","Invalid secret key")
        
        
def decrypt():
    
    password=code.get()
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("850x650")
        screen2.configure(bg="black")
        
        #decryption process.
        message=text1.get(1.0,END) #(1.0,END) means that fetch from  first line and 0 char to end char.
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        encrypt=base64_bytes.decode("ascii")
        
        Label(screen2,text="Your text is decrypted ",font="impack 10 bold").place(x=5,y=6)
        text2=Text(screen2,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=490,height=280)
        text2.insert(END,encrypt)
        
    elif(password==""):
        messagebox.showerror("ERROR","Please enter the secret key")
    elif(password!="1234"):
        messagebox.showerror("ERROR","Invalid secret key")

def reset():
    text1.delete(1.0,END)
    code.set("")
        
#label
Label(screen,text="Enter the text for encode and decode",font="impack 30 bold",bg="red").place(x=50,y=25)
#text
text1=Text(screen,font="20")
text1.place(x=50,y=80,width=990,height=500)

#label
Label(screen,text="Enter secret key",font="impack 13 bold",bg="Yellow").place(x=520,y=600)

#entery
code=StringVar()
Entry(textvariable=code,bd=8,font="20",show="*").place(x=500,y=650)

#buttons
Button(screen,text="Encrypt",font="arial 15 bold",bg="green",fg="white",command=encrypt).place(x=350,y=750)
Button(screen,text="Decrypt",font="arial 15 bold",bg="green",fg="white",command=decrypt).place(x=550,y=750)
Button(screen,text="Reset",font="arial 15 bold",bg="green",fg="white",command=reset).place(x=720,y=750)

mainloop() 