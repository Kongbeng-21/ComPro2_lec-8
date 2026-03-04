import tkinter as tk 
import math
root = tk.Tk()
root.title("Canvas Drawing")
canvas = tk.Canvas(root, width=800, height=800, bg="white") 
canvas.pack()
w=800
h=600
def create_regular_polygon(canvas,center_x,center_y,radius,sides,color):
    points=[]
    for i in range(sides):
        angle=2*math.pi*i/sides
        x=center_x+radius*math.cos(angle)
        y=center_y+radius*math.sin(angle)
        points.extend([x,y])
    canvas.create_polygon(points,fill=color,outline="black")
colors = ["red","orange","yellow","green","blue","purple","pink"]
start_x = 150
y_level = 150
spacing = 180
radius = 70
for i,sides in enumerate(range(3,10)):
    create_regular_polygon(canvas,start_x+i*spacing,y_level,radius,sides,colors[i])
        
line = canvas.create_line(50,400,400,400,fill="red",width=3)
line = canvas.create_line(50,450,400,450,fill="red",width=3)
line = canvas.create_line(50,500,400,500,fill="red",width=3)
rec = canvas.create_rectangle(600,600,700,700,fill="blue",width=3)
cir = canvas.create_oval(400,700,600,800,fill="red",width=3)
recc=canvas.create_rectangle(w*0.5,h*0.5,w*0.8,h*0.8,fill="green",width=3)
root.mainloop()