from turtle import Turtle
MOVE_SPEED = 20
X_COORDINATES_SNAKE = [0, -20, -40, -60]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SNAKE_SIZE = [1, 0.8, 0.7, 0.6]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("turtle")

    def create_snake(self):
        for number in range(4):

            snake = Turtle("circle")
            snake.color("white")
            snake.penup()
            snake.shapesize(SNAKE_SIZE[number])
            snake.goto(x=X_COORDINATES_SNAKE[number], y=0)
            self.segments.append(snake)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
            self.segments[seg_number].setheading(self.head.heading())
        self.head.fd(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def add_tail(self):
        snake = Turtle("circle")
        snake.color("white")
        snake.penup()
        snake.shapesize(0.5)
        snake.goto(self.segments[-1].position())
        self.segments.append(snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("turtle")

