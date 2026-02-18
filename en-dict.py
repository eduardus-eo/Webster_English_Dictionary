#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import os.path

def return_function(event):
    search_word()

def search_word():
    defn = ""
    found = False
    enigo = entry_word.get().strip()
    if enigo:    
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(base_dir,"en-dictionary",f"en-{enigo[:2].lower()}.txt")
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
        except (FileNotFoundError, NameError):
            messagebox.showerror("Error!","File not found...!")
            lines = []
        try:
            for i,line in enumerate(lines):
                if line.strip() == entry_word.get().strip().upper():
                    text = []
                    for j in range(200):
                        try:
                            if lines[i+j].strip().isupper() and j != 0 and lines[i+j].strip().split()[0].isalpha():
                                break
                            text.append(lines[i+j])
                        except IndexError:
                            pass
                    found = True
                    linio_nombro = i
                    break  
                elif ';' in line.strip():
                    for linio in line.split(';'):
                        if linio.strip() == entry_word.get().strip().upper():
                            text = []
                            for j in range(200):
                                try:
                                    if lines[i+j].strip().isupper() and j != 0 and lines[i+j].strip().split()[0].isalpha():
                                        break
                                    text.append(lines[i+j])
                                except IndexError:
                                    pass
                            found = True
                            linio_nombro = i
                            break
            if not found:
                messagebox.showinfo("Info","Word not Found...!")
            else:
                sukceso = False
                try:
                    for _ in range(5):
                        for i in range(linio_nombro + 1,linio_nombro + 500):
                            if lines[i].strip() == entry_word.get().strip().upper():
                                text_2 = []
                                for j in range(200):
                                    try:
                                        if lines[i+j].strip().isupper() and j != 0 and lines[i+j].strip().split()[0].isalpha():
                                            break
                                        text_2.append(lines[i+j])
                                    except IndexError:
                                        pass
                                linio_nombro = i
                                text.extend(text_2)
                                teksto.delete("1.0", tk.END)
                                teksto.insert(tk.END,"".join(text))                        
                                sukceso = True
                                break
                except IndexError:
                        pass
                if not sukceso:
                    teksto.delete("1.0", tk.END)
                    teksto.insert(tk.END,"".join(text))
            entry_word.set("")
        except IndexError:
            pass
    else:
        messagebox.showwarning("Warning!","No word entered....!")



root = tk.Tk()
root.title("Dictionary")
root.bind("<Return>", return_function)

entry_word = tk.StringVar()

kadro = tk.Frame(root)
kadro.pack()

# Aldoni nova Enigilo
enigilo = tk.Entry(kadro,textvariable=entry_word)
enigilo.grid(row=0,column=0)

# Aldoni nova Butono
butono = tk.Button(kadro,text="Search",command=search_word)
butono.grid(row=0,column=1)


teksto = tk.Text(root,width=70,height=20,font=("Courier New", 14),wrap="word")
teksto.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
scrollbar = tk.Scrollbar(root,command=teksto.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
teksto.config(yscrollcommand=scrollbar.set)

root.mainloop()
