
import random


def dead_state(width, height):
    life_space = []

    for i in range(height):
        n = []
        life_space.append(n)
        for j in range(width):
            
            life_space[i].append(0)
    
    return life_space

def random_state(width,height):
    life_space=[]

    for i in range(height):
        n = []
        life_space.append(n)
        for j in range(width):

            life = random.random()
            if life >= 0.5:
                state = 1
            else:
                state = 0
            life_space[i].append(state)
    
    return life_space




width = 4
height = 5

print(dead_state(width,height))
print(random_state(width,height))