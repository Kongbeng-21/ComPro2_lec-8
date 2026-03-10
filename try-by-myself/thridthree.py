import tkinter as tk
import random
# Animation parameters
x_speed = []
y_speed = []
balls = []
BALL_SIZE = 40 
CANVAS_W = 400 
CANVAS_H = 300

def animate():
    for i in range(len(balls)):
        # 1. Move the ball by x_speed and y_speed
        canvas.move(balls[i], x_speed[i], y_speed[i])
        # 2. Get the current bounding box of the ball [x1, y1, x2, y2]
        pos = canvas.coords(balls[i])
        # 3. Check for collisions with walls and reverse direction 
        if pos[0] <= 0 or pos[2] >= CANVAS_W: # Left or Right wall
            x_speed[i] = -x_speed[i]
        if pos[1] <= 0 or pos[3] >= CANVAS_H: # Top or Bottom wall
            y_speed[i] = -y_speed[i]
    root.after(8, animate)

root = tk.Tk()
root.title("Bouncing Ball Animation")
canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white") 
canvas.pack()
colors = ["red","blue","green","orange","purple"]
# Create the ball object
for i in range(5):
    x = random.randint(0,CANVAS_W - BALL_SIZE)
    y = random.randint(0,CANVAS_H - BALL_SIZE)
    
    ball = canvas.create_oval(x,y,x+BALL_SIZE,y+BALL_SIZE,fill=random.choice(colors))
    balls.append(ball)
    
    vx = random.randint(-5,5)
    vy = random.randint(-5,5)
    
    if vx ==0:
        vx=3
    if vy==0:
        vy=3
    
    x_speed.append(vx)
    y_speed.append(vy)
animate()
# Enter the main event loop
root.mainloop()