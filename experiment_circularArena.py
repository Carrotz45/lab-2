from view import *
from model import *
import math

n = 20
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta), math.sin(theta))
    pos = 10 * u
    vel = -1 * u 
    particles.append(Particle(1,pos,vel,0.2))

def no_force(dt,particles):
    return Vec(0,0)

def circular_arena(dt, particles, k, R):
    for particle in particles:
        vector_from_O = particle.position
        r = vector_from_O.norm() + particle.radius
        if r < R:
            force = Vec(0, 0)
        else:
            force_0 = vector_from_O.__rmul__(1/r)
            force = force_0.__rmul__(k*(R-r))
            particle.apply_force(dt, force)

simulation_loop(circular_arena, 0.000005, particles)
