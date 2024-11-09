from tkinter import *
from tkinter import messagebox
import base64
import threading

screen = Tk()
screen.geometry("1080x1080")
screen.title("Encode And Decode")
screen.configure(bg="black")

def encrypt():
    password = code.get()
    if password == "123":
        # Start a new thread for encryption
        threading.Thread(target=perform_encryption).start()
    elif password == "":
        messagebox.showerror("ERROR", "Please enter the secret key")
    else:
        messagebox.showerror("ERROR", "Invalid secret key")

def perform_encryption():
    message = text1.get(1.0, END).strip()  # Fetch the text and strip whitespace
    if not message:
        messagebox.showerror("ERROR", "No text to encrypt")
        return

    # Encryption process.
    encode_message = message.encode("ascii")
    base64_bytes = base64.b64encode(encode_message)
    encrypt = base64_bytes.decode("ascii")
    
    # Update the GUI in the main thread
    screen1 = Toplevel(screen)
    screen1.title("Encryption")
    screen1.geometry("850x650")
    screen1.configure(bg="pink")
    
    Label(screen1, text="Your text is encrypted:", font="impact 10 bold").place(x=5, y=6)
    text2 = Text(screen1, font="30", bd=4, wrap=WORD)
    text2.place(x=2, y=30, width=490, height=280)
    text2.insert(END, encrypt)
    
    text1.focus()

def decrypt():
    password = code.get()
    if password == "1234":
        # Start a new thread for decryption
        threading.Thread(target=perform_decryption).start()
    elif password == "":
        messagebox.showerror("ERROR", "Please enter the secret key")
    else:
        messagebox.showerror("ERROR", "Invalid secret key")

def perform_decryption():
    message = text1.get(1.0, END).strip()  # Fetch the text and strip whitespace
    if not message:
        messagebox.showerror("ERROR", "No text to decrypt")
        return

    # Decryption process.
    decode_message = message.encode("ascii")
    try:
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")
    except Exception as e:
        messagebox.showerror("ERROR", "Decryption failed: " + str(e))
        return

    # Update the GUI in the main thread
    screen2 = Toplevel(screen)
    screen2.title("Decryption")
    screen2.geometry("850x650")
    screen2.configure(bg="black")
    
    Label(screen2, text="Your text is decrypted:", font="impact 10 bold").place(x=5, y=6)
    text2 = Text(screen2, font="30", bd=4, wrap=WORD)
    text2.place(x=2, y=30, width=490, height=280)
    text2.insert(END, decrypt)
    
    text1.focus()

def reset():
    text1.delete(1.0, END)
    code.set("")
    
    text1.focus()

# Label
Label(screen, text="Enter the text for encode and decode", font="impact 30 bold", bg="red").place(x=50, y=25)

# Text
text1 = Text(screen, font="20")
text1.place(x=50, y=80, width=990, height=500)
text1.focus()  # Set focus to the text widget

# Label
Label(screen, text="Enter secret key", font="impact 13 bold", bg="pink").place(x=520, y=600)

# Entry
code = StringVar()
Entry(screen, textvariable=code, bd=8, font="20", show="*").place(x=500, y=650)

# Buttons
Button(screen, text="Encrypt", font="arial 15 bold", bg="green", fg="white", command=encrypt).place(x=350,y=750)
Button(screen, text="Decrypt", font="arial 15 bold", bg="green", fg="white", command=decrypt).place(x=550, y=750)
Button(screen, text="Reset", font="arial 15 bold", bg="green", fg="white", command=reset).place(x=720, y=750)

# Start the main event loop
screen.mainloop()
