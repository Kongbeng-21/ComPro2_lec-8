import tkinter as tk
import math 
root = tk.Tk()
root.title("Canvas Drawing")
# Create a Canvas widget
canvas = tk.Canvas(root, width=2000, height=1000, bg="white") 
canvas.pack()
# Draw a red line
line_id = canvas.create_line(60, 50, 600, 50, fill="blue", width=3)
line_id = canvas.create_line(60, 100, 600, 10, fill="blue", width=3)
line_id = canvas.create_line(60, 150, 600, 15, fill="blue", width=3)
line_id = canvas.create_line(60, 200, 600, 20, fill="blue", width=3)
line_id = canvas.create_line(60, 250, 600, 25, fill="blue", width=3)
line_id = canvas.create_line(60, 300, 600, 30, fill="blue", width=3)
line_id = canvas.create_line(60, 350, 600, 35, fill="blue", width=3)
line_id = canvas.create_line(60, 400, 600, 40, fill="blue", width=3)
line_id = canvas.create_line(60, 450, 600, 45, fill="blue", width=3)
line_id = canvas.create_line(60, 500, 600, 50, fill="blue", width=3)
# Draw a blue rectangle
rect_id = canvas.create_rectangle(260, 250, 400, 150, fill="black", )
rect_id = canvas.create_rectangle(60, 150, 250, 50, fill="green", )
rect_id = canvas.create_rectangle(360, 250, 600, 450, fill="red", )# Draw a green oval (circle if bounded by a square)
oval_id = canvas.create_oval(100, 260, 200, 360, fill="orange") 
oval_id = canvas.create_oval(200, 260, 300, 360, fill="orange") # Draw some text# Draw an orange polygon (triangle)

def create_regular_polygon(canvas, center_x, center_y, radius, sides, color):
    points = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.extend([x, y])
    return canvas.create_polygon(points, fill=color, outline="black")

start_x = 100
y_level = 420
spacing = 120
radius = 40

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

for i, sides in enumerate(range(3, 10)):  # 3 to 9 sides
    create_regular_polygon(
        canvas,
        start_x + i * spacing,
        y_level,
        radius,
        sides,
        colors[i]
    )
root.mainloop()