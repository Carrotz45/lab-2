from tkinter import *
from model import *

root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()

o = canvas.create_oval(80, 30, 140, 150, fill="blue")
x = canvas.create_oval(0,0,10,10, fill="red")

# Task (7/12): Draw on canvas



# Task (8/12): Define a new function to_canvas_coords(canvas, x)
def to_canvas_coords(canvas, u):
    x, y = u.get_coords()
    print(x,y)
    height_origo = canvas.winfo_reqheight()/2
    width_origo = canvas.winfo_reqwidth()/2 #origo = (width/2; height/2)
    scale = canvas.winfo_reqheight() / 20
    scaled_x = x * scale + width_origo
    scaled_y = -y * scale + height_origo
    scaled_vector = (scaled_x, scaled_y)
    return scaled_vector


vec = Vec(0,0)
print(vec.__repr__)
scale_vec = to_canvas_coords(canvas, vec)
x = scale_vec[0]
y = scale_vec[1]

origo = canvas.create_oval(x-10,y+10,x+10,y-10, fill="red")

input()
#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(canvas, o, u1, u2):
    x1, y1 = to_canvas_coords(canvas, u1)
    x2, y2 = to_canvas_coords(canvas, u2)
    canvas.coords(o,x1,y1,x2,y2)

# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):
    bound_1, bound_2 = particle.bounding_box()
    x1, y1 = bound_1
    x2, y2 = bound_2
    oval = canvas.create_oval(x1,y1,x2,y2,fill="red")
    return oval
        #ANISAH FIXA!!!!!!! OMG OMDZ
# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):
    for particle in particles:
        create_oval