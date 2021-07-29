import tkinter as tk
from tkinter import filedialog as fd
import moviepy.editor # pip install moviepy

root = tk.Tk()
root.title("Video To Audio Converter")
root.geometry("400x500")
root.resizable(0, 0)
root.configure(background="#d4ebf2")
root.columnconfigure(0,weight=1)

def select_file():
    global filename
    filename = fd.askopenfilename(title="Open file")
    l5 = tk.Label(root, text=filename, fg="black",bg="#d4ebf2", font=("Garamond", 10, "bold")).grid(row=3, column=0, pady=15, padx=15, sticky="w")


def save():
    global savename
    savename = fd.asksaveasfilename(initialfile = 'Untitled.mp3',
    defaultextension=".mp3", filetypes=[("Music","*.mp3"), ("All Files","*.*")])
    l6 = tk.Label(root, text=savename, fg="black", bg="#d4ebf2", font=("Garamond",10,"bold")).grid(row=7, column=0, pady=15, padx=15, sticky="w")


def convert():
    video = moviepy.editor.VideoFileClip(filename)
    audio = video.audio

    audio.write_audiofile(savename)
    l7 = tk.Label(root,text="Completed Successfully!", fg="black", bg="#d4ebf2", font=("Garamond", 12, "bold")).grid(row=9, column=0, pady=10, padx=5)


l1 = tk.Label(root, text="Video To Audio Converter", fg="black", bg="#d4ebf2", borderwidth=4, relief="solid", font=("Rockwell",18,"bold")).grid(row=0, column=0, padx=10, pady=20, ipadx=10)
l2 = tk.Label(root, text="Select The File To Be Converted", fg="black", bg="#d4ebf2", font=("Garamond", 15, "bold")).grid(row=1, column=0, pady=10, padx=5, sticky="w")
b1 = tk.Button(root, width=10, bg="#add8e6", fg="#0a0a0a", text="Choose Path", command=select_file).grid(row=2, column=0, pady=3, padx=15, sticky="w")

l4 = tk.Label(root, text="Select The Save Path", fg="black", bg="#d4ebf2", font=("Garamond", 15, "bold")).grid(row=5, column=0, pady=10, padx=5, sticky="w")
l5 = tk.Label(root, text=" ", bg="#d4ebf2", font=("Garamond", 10, "bold")).grid(row=3, column=0, pady=15, padx=15, sticky="w")
l6 = tk.Label(root, text=" ", bg="#d4ebf2", font=("Garamond", 10,"bold")).grid(row=7, column=0, pady=15, padx=15, sticky="w")
l7 = tk.Label(root, text=" ", bg="#d4ebf2", font=("Garamond", 12,"bold")).grid(row=9, column=0, pady=10, padx=5)

b2 = tk.Button(root, width=10, bg="#add8e6", fg="#0a0a0a", text="Save As", command=save).grid(row=6, column=0, pady=3, padx=15, sticky="w")
b2 = tk.Button(root, width=10, bg="#add8e6", fg="#0a0a0a", text="Convert", command=convert).grid(row=8, column=0, pady=30, padx=15)


root.mainloop()


