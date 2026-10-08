from tkinter import *
from model import *

root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()

o = canvas.create_oval(80, 30, 140, 150, fill="blue")

# Task (7/12): Draw on canvas
input()


# Task (8/12): Define a new function to_canvas_coords(canvas, x)
def to_canvas_coords(canvas, u):
    scale = canvas.winfo_reqheight() // 20
    scaled_vector = (u.x*scale, -(u.y*scale))

    return scaled_vector
    
    

#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(canvas, o, u1, u2):
    pass

# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):
    pass

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):
    pass