
# coding: utf-8

# In[4]:


from carel import Carel
from carelgrid import CarelGrid
from gamecanvas import GameCanvas


# In[16]:


class CarelCounter(Carel):
    
    def initiate_counter(self):
        self.counter = 0

    def fill_field(self):
        while True:
            self.fill_to_wall()
            self.turn_right()
            if not self.is_front_clear():
                break
            self.move()
            self.turn_right()
            self.fill_to_wall()
            self.turn_left()
            if not self.is_front_clear():
                break
            self.move()
            self.turn_left()
            
    def fill_to_wall(self):
        while True:
            self.drop_beeper()
            if not self.is_front_clear():
                break
            self.move()
    
    def turn_right(self):
        self.turn_left()
        self.turn_left()
        self.turn_left()
    
    def collect_beeper(self):
        super().collect_beeper()
        self.counter = self.counter + 1


# In[17]:


field = [[0 for x in range(6)] for y in range(4)]

field[0][1] = 1
field[1][0] = 2
field[3][2] = 1

grid = CarelGrid(field)
canvas = GameCanvas(speed=3);
carel = CarelCounter(canvas, grid);

carel.initiate_counter()

def move():
    carel.move()
def turn_left():
    carel.turn_left()
def drop_beeper():
    carel.drop_beeper()
def collect_beeper():
    carel.collect_beeper()
def is_beeper():
    return carel.is_beeper()
def is_front_clear():
    return carel.is_front_clear()
def fill_field():
    carel.fill_field()
def show():
    carel.show()


# In[18]:


# New methods go here

# Example

def turn_around():
    turn_left()
    turn_left()

def clear_to_wall():
    while True:
        clear_cell()
        if not is_front_clear():
            break
        move()

def clear_cell():
    while is_beeper():
        collect_beeper()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# In[14]:


while True:
    clear_to_wall()
    turn_right()
    if not is_front_clear():
        break
    move()
    turn_right()
    clear_to_wall()
    turn_left()
    if not is_front_clear():
        break
    move()
    turn_left()

for i in range(carel.counter):
    drop_beeper()


# In[15]:


carel.fill_field()


# In[19]:


show()


# In[20]:


fill_field()

