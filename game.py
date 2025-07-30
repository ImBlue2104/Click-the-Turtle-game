import random
import turtle
import time
#asks user for desired length of game
desired_time = int(input("Enter how long you want your game to be: "))
def screen_setup(): 
#creates bg
    pen = turtle.Turtle()
    screen = turtle.Screen()#initiates screen
    screen.setup(1000, 1000)#sets size
    screen.bgcolor("DarkSeaGreen3") #sets color
    pen.hideturtle()
    style = ("Courier", 50)
    pen.penup()#so line is not made
    pen.goto(0, 300)
    pen.write("Click The Turtle!!!", font = style, align = 'center')#displays text
    
    return screen


def turtle_shape():
    game_turtle = turtle.Turtle() #stores library functionalities
    game_turtle.fillcolor("DarkSeaGreen4")
    game_turtle.shape("turtle") #creates turtle shape
    game_turtle.end_fill()
    game_turtle.shapesize(3,3) #creates turtle shape
    return game_turtle

score = 0
def move_when_clicked(_x,_y):#parameters not required but only there to accept x and y coordinates from onclick
    global score
    global game_turtle
    randx = random.randint(-300, 300)#generates rand x value
    randy = random.randint(-300, 300)#generates rand y value
    game_turtle.goto(randx,randy)
    score = score +100
    print (score)



pen = turtle.Turtle()

#displays a timer on turtle screen
def screen_timer():
    global desired_time #acceses the global var
    pen.clear()
    style = ("Courier", 35)
    style2 = ("Courier", 75)
    pen.penup()
    pen.hideturtle()
    pen.goto(-255,-400)
    if desired_time > 0:
        pen.write(f"Time Left:{desired_time}secs", font = style, align = 'center')
        desired_time -= 1
        screen.ontimer(screen_timer, 1000)#halts execution for 1 sec which is 100 millisec

    else:
        pen.goto(0,0)
        pen.write(f"GAME OVER",font = style2, align = "center" )
        game_turtle.clear()
        pen.goto(0,250)
        pen.write(f"Final Score: {score}", font=style, align="center")
        game_turtle.hideturtle()
        screen.ontimer(screen.bye, 2000)  # Wait 2 seconds then close


score_pen = turtle.Turtle()
def print_score():
    global desired_time, score_pen #acceses the global var
    score_pen.clear()
    style = ("Courier", 35)
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.goto(255,-400)
    if desired_time != 0:
        score_pen.write(f"Score: {score}", font=style, align="center")
        screen.ontimer(print_score, 500)
    



screen = screen_setup() #screen is created
game_turtle = turtle_shape()#turtle object or shape is created
screen_timer()
print_score()



game_turtle.onclick(move_when_clicked)#move when clicked function gives rand x and y and moves it there and gameturte is the actual turtle

turtle.done()

