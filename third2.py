import tkinter as tk
# Animation parameters
x_speed = 3 
y_speed = 4 
BALL_SIZE = 40 
CANVAS_W = 400 
CANVAS_H = 300
def animate():
    global x_speed, y_speed
    # 1. Move the ball by x_speed and y_speed
    canvas.move(ball, x_speed, y_speed)
    # 2. Get the current bounding box of the ball [x1, y1, x2, y2]
    pos = canvas.coords(ball)
    # 3. Check for collisions with walls and reverse direction 
    if pos[0] <= 0 or pos[2] >= CANVAS_W: # Left or Right wall
        x_speed = -x_speed
    if pos[1] <= 0 or pos[3] >= CANVAS_H: # Top or Bottom wall
        y_speed = -y_speed
    root.after(8, animate)

root = tk.Tk()
root.title("Bouncing Ball Animation")
canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white") canvas.pack()
# Create the ball object
ball = canvas.create_oval(10, 10, 10 + BALL_SIZE, 10 + BALL_SIZE, fill="orange", outline="red") # Start the animation loop
animate()
# Enter the main event loop
root.mainloop()