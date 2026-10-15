from tkinter import *
from model import *
## Add this to the imports
import time


# Task (7/12): Draw on canvas



# Task (8/12): Define a new function to_canvas_coords(canvas, x)
def to_canvas_coords(canvas, u):
    x, y = u.get_coords()
    height_origo = canvas.winfo_reqheight()/2
    width_origo = canvas.winfo_reqwidth()/2 #origo = (width/2; height/2)
    scale = canvas.winfo_reqheight() / 20
    scaled_x = x * scale + width_origo
    scaled_y = -y * scale + height_origo
    scaled_vector = Vec(scaled_x, scaled_y)
    return scaled_vector


#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(canvas, o, u1, u2):
    x1, y1 = to_canvas_coords(canvas, u1).get_coords()
    x2, y2 = to_canvas_coords(canvas, u2).get_coords()
    return canvas.coords(o,x1,y1,x2,y2)

# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):
    start_x, start_y = (0 , 0)

    bound_1 = (start_x-particle.radius, start_y+particle.radius)
    bound_2 = (start_x+particle.radius, start_y-particle.radius)

    x1, y1 = bound_1
    x2, y2 = bound_2
    oval = canvas.create_oval(x1,y1,x2,y2,fill="red")

    new_pos_bound1, new_pos_bound2 = particle.bounding_box()

    move_oval_to(canvas, oval, new_pos_bound1, new_pos_bound2)

root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()


# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):
    oval_list = []
    for particle in particles:
        new_oval = create_oval(canvas, particle)
        oval_list.append(new_oval)

    while True:
        for particle in particles:
            Particle.inertial_move(particle, timestep)
            for oval in oval_list:
                bound_1, bound_2 = particle.bounding_box()
                oval = move_oval_to(canvas, oval, bound_1, bound_2)
                canvas.update()