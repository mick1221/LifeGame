
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


def next_state(life_space):
    new_state = []

    for i in range(len(life_space)-1):
        t = []
        new_state.append(t)
        count = 0

        # checking the top row
        if i == 0:
            for j in range(len(life_space[i])-1):
                count = 0
                if j == 0:
                    if life_space[i][j+1] == 1:
                        count +=1
                    if life_space[i+1][j+1] == 1:
                        count +=1
                    if life_space[i+1][j] == 1:
                        count +=1
                    
                elif j == len(life_space[i]):
                    if life_space[i][j-1] == 1:
                        count +=1
                    if life_space[i+1][j-1] == 1:
                        count +=1
                    if life_space[i+1][j] == 1:
                        count +=1
                else:
                    if life_space[i][j-1] == 1:
                        count +=1
                    if life_space[i+1][j-1] == 1:
                        count +=1
                    if life_space[i+1][j] == 1:
                        count +=1
                    if life_space[i][j+1] == 1:
                        count +=1
                    if life_space[i+1][j+1] == 1:
                        count +=1
                #checking for new life value
                if life_space[i][j] == 0:
                    if count == 3:
                        new_state[i].append(1)
                    else:
                        new_state[i].append(0)
                else:
                    if count < 2:
                        new_state[i].append(0)
                    elif count > 3:
                        new_state[i].append(0)
                    else:
                        new_state[i].append(1)
        #checking bottom row
        elif i == len(life_space):
            for j in range(len(life_space[i])-1):
                count = 0 
                if j == 0:
                    if life_space[i][j+1] == 1:
                        count +=1
                    if life_space[i-1][j+1] == 1:
                        count +=1
                    if life_space[i-1][j] == 1:
                        count +=1
                elif j == len(life_space[i])-1:
                    if life_space[i][j-1] == 1:
                        count +=1
                    if life_space[i-1][j-1] == 1:
                        count +=1
                    if life_space[i-1][j] == 1:
                        count +=1

                else:
                    if life_space[i][j-1] == 1:
                        count +=1
                    if life_space[i-1][j-1] == 1:
                        count +=1
                    if life_space[i-1][j] == 1:
                        count +=1
                    if life_space[i][j+1] == 1:
                        count +=1
                    if life_space[i-1][j+1] == 1:
                        count +=1
                
                #checking for new life value
                if life_space[i][j] == 0:
                    if count == 3:
                        new_state[i].append(1)
                    else:
                        new_state[i].append(0)
                else:
                    if count < 2:
                        new_state[i].append(0)
                    elif count > 3:
                        new_state[i].append(0)
                    else:
                        new_state[i].append(1)
        #checking middle rows
        else:
            for j in range(len(life_space[i])-1):
                count = 0
                if j == 0:
                    if life_space[i][j+1] == 1:
                        count +=1
                    if life_space[i-1][j+1] == 1:
                        count +=1
                    if life_space[i-1][j] == 1:
                        count +=1
                    if life_space[i+1][j+1] == 1:
                        count +=1
                    if life_space[i+1][j] == 1:
                        count +=1

                elif j == len(life_space[i]):
                    if life_space[i][j-1] == 1:
                        count +=1
                    if life_space[i-1][j-1] == 1:
                        count +=1
                    if life_space[i-1][j] == 1:
                        count +=1
                    if life_space[i+1][j-1] == 1:
                        count +=1
                    if life_space[i+1][j] == 1:
                        count +=1

                else:
                    if life_space[i][j-1] == 1:
                        count +=1
                    if life_space[i-1][j-1] == 1:
                        count +=1
                    if life_space[i-1][j] == 1:
                        count +=1
                    if life_space[i+1][j-1] == 1:
                        count +=1
                    if life_space[i+1][j] == 1:
                        count +=1
                    if life_space[i][j+1] == 1:
                        count +=1
                    if life_space[i-1][j+1] == 1:
                        count +=1
                    if life_space[i+1][j+1] == 1:
                        count +=1

                #checking for new life value
                if life_space[i][j] == 0:
                    if count == 3:
                        new_state[i].append(1)
                    else:
                        new_state[i].append(0)
                else:
                    if count < 2:
                        new_state[i].append(0)
                    elif count > 3:
                        new_state[i].append(0)
                    else:
                        new_state[i].append(1)
    return new_state



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




width = 20
height = 20

test = dead_state(width,height)
test2 = random_state(width,height)
print_life(test2)
test3 = next_state(test2)
print_life(test3)

print_life(test)
