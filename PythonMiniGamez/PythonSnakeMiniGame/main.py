from tkinter import *
import time
import random

Game_Width = 700
Game_Height = 700
speed = 60
space_size = 50
body_parts= 3
snake_colour="#C946F7"
food_colour="#7CF30C"
background_colour="#000000"


class Snake:
    def __init__(self):
        self.body_size=body_parts
        self.coordinates=[]
        self.squares=[]

        for i in range (0,body_parts):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y , x+space_size, y+space_size, fill=snake_colour, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0,(Game_Width/space_size)-1) * space_size
        y = random.randint(0,(Game_Height/space_size)-1) * space_size

        self.coordinates=[x,y]
        canvas.create_oval(x,y, x+space_size,y+space_size,fill=food_colour, tag="food")


def change_direction(new_direction):
    global direction

    if new_direction=='left':
        if direction != 'right':
            direction = new_direction

    elif new_direction=='right':
        if direction != 'left':
            direction = new_direction

    elif new_direction=='up':
        if direction != 'down':
            direction = new_direction

    elif new_direction=='down':
        if direction != 'up':
            direction = new_direction

def next_turn(snake, food):

    x,y=snake.coordinates[0]

    if direction=="up":
        y-=space_size
    elif direction=="down":
        y+=space_size
    elif direction == "left":
        x-=space_size
    elif direction=="right":
        x+=space_size

    snake.coordinates.insert(0,(x,y))

    square=canvas.create_rectangle(x,y,x+space_size,y+space_size, fill=snake_colour)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))
        canvas.delete("food")

        food = Food()




    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
         game_over()
    else:
        window.after(speed,next_turn,snake,food)


def check_collision(snake):
    x,y= snake.coordinates[0]
    if x < 0 or x >=Game_Width:
        return True

    elif y < 0 or y>=Game_Height:
        print("GAME OVER")
    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=("consolas",70), text="GAME OVER", fill="red",tag="game over")

# here i am making the window
window = Tk()
window.title="snakle"

# adding score text to the window
score = 0
direction= "down"
label= Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# giving the window colour
canvas= Canvas(window, bg=background_colour, height=Game_Height, width=Game_Width)
canvas.pack()


window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake,food)
window.mainloop()
