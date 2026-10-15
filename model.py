import math

# Task (2/12): Define a class Vec
class Vec:
    def __init__(self, x, y): #initialize the vector self at the given coordinates.
        self.x = x
        self.y = y
        
    def __repr__(self): #return a string which is a suitable representation of the vector.
        return f"({self.x}, {self.y})"

    def __rmul__(self, factor): #return a new vector scaled by the given factor
        mul_x = self.x * factor
        mul_y = self.y * factor
        vectors_rmul_xy = Vec(mul_x, mul_y)
        return vectors_rmul_xy
        
    def __add__(self, other): 
        added_x = self.x + other.x
        added_y = self.y + other.y
        vectors_added_xy = Vec(added_x, added_y)
        return vectors_added_xy
    
    def __sub__(self, other):
        subbed_x = self.x - other.x
        subbed_y = self.y - other.y
        vectors_subbed_xy = Vec(subbed_x, subbed_y)
        return vectors_subbed_xy
    
    def norm(self):
        self_norm_form = math.sqrt(self.x**2 + self.y**2)
        return self_norm_form
    
    def get_coords(self):
        return (self.x, self.y)
    

# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
    dot_product = (u.x * v.x) + (u.y * v.y)
    return dot_product


# Task (4/12): Create a class Particle
class Particle:
    def __init__(self, mass, position, velocity, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).

    def inertial_move(self, dt):
        velocity = self.velocity
        position = self.position

        multiply_dt_velocity = velocity.__rmul__(dt)
        add_pos_with_dtvelocity = position.__add__(multiply_dt_velocity) # dt * velocity + position
        self.position = add_pos_with_dtvelocity
        return add_pos_with_dtvelocity

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)

    def apply_force(self, dt, f):
        velocity = self.velocity
        mass = 1/self.mass
        acceleration = f.__rmul__(mass)

        dt_mul_a = acceleration.__rmul__(dt)
        result = velocity.__add__(dt_mul_a)
        self.velocity = result
        return result

##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)
    def bounding_box(self):
        x, y = self.position.get_coords()
        bound_1 = Vec(x-self.radius, y+self.radius)
        bound_2 = Vec(x+self.radius, y-self.radius)
        return (bound_1, bound_2)


###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################


# Feature Task: Define a function circular_arena
# def circular_arena(dt, particles, k, R):
#     for particle in particles:
#         pass
#     pass