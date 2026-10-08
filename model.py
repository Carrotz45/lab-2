import math

# Task (2/12): Define a class Vec
class Vec:
    def __init__(self, x, y): #initialize the vector self at the given coordinates.
        self.x = x
        self.y = y
        
    def __repr__(self): #return a string which is a suitable representation of the vector.
        return f"{(self.x, self.y)}"

    def __rmul__(self, factor): #return a new vector scaled by the given factor
        mul_x = self.x * factor
        mul_y = self.y * factor
        vectors_rmul_xy = (mul_x, mul_y)
        return vectors_rmul_xy
        
    def __add__(self, other): 
        added_x = self.x + other.x
        added_y = self.y + other.y
        vectors_added_xy = (added_x, added_y)
        return vectors_added_xy
    
    def __sub__(self, other):
        subbed_x = self.x + other.x
        subbed_y = self.y + other.y
        vectors_subbed_xy = (subbed_x, subbed_y)
        return vectors_subbed_xy
    
    def norm(self):
        self_norm_form = math.sqrt(self.x**2 + self.y**2)
        return self_norm_form
    
    def get_coords(self):
        return (self.x, self.y)
    

# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
    product = 0
    sum_of_product = 0
    for i in range(len(u)):
        product = u[i] * v[i]
        sum_of_product += product
    return sum_of_product

# Task (4/12): Create a class Particle
class Particles:
    def __init__(self, mass, position, velocity, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).

    def inertial_move(self, dt):
        return dt * (self.velocity + self.position)

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)

    def apply_force(self, dt, f):
        acceleration = f // self.mass
        return dt * (acceleration + self.velocity)

##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################