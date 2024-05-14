import turtle as t

STARTING_INDEX = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]
        self.head.color("red")

    def create_snake(self):
        for snake_box in STARTING_INDEX:
            self.add_box(snake_box)

    def add_box(self, snake_box):
        new_box = t.Turtle(shape = "square")
        new_box.penup()
        new_box.color("white")
        new_box.goto(snake_box)
        new_box.speed("fastest")
        self.boxes.append(new_box) 

    def extend(self):
        self.add_box(self.boxes[-1].position())           

    def move(self):
        for box in range(len(self.boxes)-1, 0, -1):
           new_x = self.boxes[box - 1].xcor()
           new_y = self.boxes[box - 1].ycor()
           self.boxes[box].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)     

    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)  

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT) 

    def reset_snake(self):
        for i in self.boxes:
            i.goto(999, 999)
        self.boxes.clear()
        self.create_snake()
        self.head = self.boxes[0] 
        self.head.color("red")                     