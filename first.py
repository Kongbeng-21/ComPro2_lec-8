import tkinter as tk
from tkinter import ttk

def btn_clicked():
    global click_count
    click_count += 1
    lbl.config(text=f"Button clicked: {click_count} times", font=("Helvetica", 42), bg="white", fg="black")
    
def btn_decrease():
    global click_count
    click_count -= 1
    lbl.config(text=f"Button clicked: {click_count} times", font=("Helvetica", 42), bg="white", fg="black")
    
click_count = 0


count = 0
root = tk.Tk() 
root.title("Event‐Driven Example") 
root.geometry("800x400")

style = ttk.Style()
style.theme_use("clam")

lbl = tk.Label(root, text="Button clicked: 0 times", font=("Helvetica", 42), bg="white", fg="black") 
lbl.pack(pady=20)
btn = tk.Button(root, text="Click Me!", command=btn_clicked, bg="white", fg="black", highlightbackground="white")
btn.pack(pady=10)
btn = tk.Button(root, text="Click Me!", command=btn_decrease, bg="white", fg="black", highlightbackground="white")
btn.pack(pady=10)
root.mainloop()