
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

def print_life(life_space):
    length = len(life_space)
    string = ""
    for i in range(length+2):
        string = string + "-"
    print(string)

    for i in life_space:
        line = "|"
        for j in i:
            if j == 1:
                line = line + "#"
            else:
                line = line + " "
        line = line + "|"
        print(line)
    
    print(string)




width = 4
height = 5

test = dead_state(width,height)
test2 = random_state(width,height)

print_life(test)
print_life(test2)