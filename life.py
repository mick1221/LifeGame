


def dead_state(width, height):
    life_space=[]

    for i in range(height):
        n = []
        life_space.append(n)
        for j in range(width):
            
            life_space[i].append(0)
    
    return life_space

width = 4
height = 5

print(dead_state(width,height))