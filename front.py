import tkinter as tk
from tkinter import *
from tkinter import messagebox
import keygen
import winsound

window = tk.Tk()
window.title("KeyGen")
window.geometry("900x600")
window.resizable(False, False)

bg_image = tk.PhotoImage(file="assets/background.png")
bg = tk.Label(window, image=bg_image)
bg.place(x=0, y=0, relwidth=1, relheight=1)



frame = tk.Frame(window, bg="#101010") #
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="DEC-число (3 цифры)", bg="#101020", fg="white").pack(pady=(4, 4))

entry_input = tk.Entry(frame, width=8, justify="center")
entry_input.insert(0, "123")
entry_input.pack()

tk.Label(frame, text="Ключ", bg="#101020", fg="white").pack(pady=(14, 4))

entry_key = tk.Entry(frame, width=24, justify="center", state="readonly")
entry_key.pack(ipady=10)

btn = tk.Button(frame, text="Сгенерировать", width=18)
btn.pack(pady=10)

def validate(text):
    text = text.strip()
    if not text:
        return False
    if not text.isdigit():
        return False
    if len(text) != 3:
        return False
    return True

def on_generate():
    raw = entry_input.get()
    ok = validate(raw)
    if not ok:  return

    key = keygen.keygen(raw.strip())

    entry_key.configure(state="normal")
    entry_key.delete(0, "end")
    entry_key.insert(0, key)
    entry_key.configure(state="readonly")
    
btn.configure(command=on_generate)

music = "assets/music.wav"
winsound.PlaySound(music,winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

lbl_title = tk.Label(frame, text="KEYGEN", bg="#101020", fg="#39ff9e")
lbl_title.pack(pady=10)

colors = ["#39ff9e", "#2ee6ff", "#ff3bd4", "#ffd166"]
color_index = 0

def animate():
    global color_index
    color_index = (color_index + 1) % 4
    lbl_title.configure(fg=colors[color_index])
    window.after(300, animate)

animate()

window.mainloop()