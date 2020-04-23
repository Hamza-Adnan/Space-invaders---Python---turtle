##Hamza Adnan, Panav Goyal
##january 21, 2020
##PanavHamzaGAME.py
##Space invaders in turtle python
##Game may be laggy do to the single threaded nature of python and turtle!




import turtle
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.setup(width = 700, height =  700)
##wn.tracer(0)
wn.bgcolor("black")
wn.bgpic("background.gif")
wn.title("Space Invaders")



sc = turtle.Turtle()
sc.hideturtle()
sc.penup()
sc.sety(600)
sc.home()
sc.color("red")
sc.write("Space Invaders!", False, align="center", font=("Comic Sans MS", 24, "normal"))

startup = turtle.Turtle()
startup.hideturtle()
startup.speed(3)
startup.home()
for p in range(5):
        startup.clear()
        startup.color("red")
        startup.write("Get Ready!", False, align="center", font=("Arial", 24, "normal"))
        startup.color("yellow")
        startup.clear()
        startup.write("Get Ready!", False, align="center", font=("Arial", 24, "normal"))

#Draw border
sc.clear()
border_pen = turtle.Turtle()
border_pen.speed(4)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
border_pen.hideturtle()
for side in range(8):
        border_pen.fd(600)
        border_pen.lt(90)
border_pen.hideturtle() 
startup.clear()
#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#register player shapes
wn.register_shape("Ship.gif")
wn.register_shape("Alien.gif")
wn.register_shape("Sans.gif")
wn.register_shape("Papyrus.gif")
player = turtle.Turtle()
player.color("blue")
player.shape("Ship.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
        #Create the enemy
        enemies.append(turtle.Turtle())

for enemy in enemies:
        enemy.color("red")
        enemy.shape("Alien.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

enemyspeed = 4
bosses = []
for i in range(5):
        bosses.append(turtle.Turtle())
for boss in bosses:
        boss.shape("Papyrus.gif")
        boss.penup()
        boss.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        boss.setposition(x, y)
        boss.hideturtle()

bossspeed = 4
bosshit = 0

bosses2 = []
for i in range(5):
        bosses2.append(turtle.Turtle())
for boss2 in bosses2:
        boss2.shape("Sans.gif")
        boss2.penup()
        boss2.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        boss2.setposition(x, y)
        boss2.hideturtle()

bossspeed2 = 6
bosshit2 = 0


#Create the player's bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 50


#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
                x = - 280
        player.setx(x)
        
def move_right():
        x = player.xcor()
        x += playerspeed
        if x > 280:
                x = 280
        player.setx(x)
        
def fire_bullet():
        #Declare bulletstate as a global if it needs changed
        global bulletstate
        if bulletstate == "ready":
                bulletstate = "fire"
                #Move the bullet to the just above the player
                x = player.xcor()
                y = player.ycor() + 10
                bullet.setposition(x, y)
                bullet.showturtle()

def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 30:
                return True
        else:
                return False
def bossCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 45:
                return True
        else:
                return False
def esc():
        wn.bye()
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
##turtle.onkey(esc, "")
#Main game loop
while True:
        
        for enemy in enemies:
                #Move the enemy
                x = enemy.xcor()
                x += enemyspeed
                enemy.setx(x)

                #Move the enemy back and down
                if enemy.xcor() > 280:
                        #Move all enemies down
                        for e in enemies:
                                y = e.ycor()
                                y -= 40
                                e.sety(y)
                        #Change enemy direction
                        enemyspeed *= -1
                
                if enemy.xcor() < -280:
                        #Move all enemies down
                        for e in enemies:
                                y = e.ycor()
                                y -= 40
                                e.sety(y)
                        #Change enemy direction
                        enemyspeed *= -1
                        
                #Check for a collision between the bullet and the enemy
                if isCollision(bullet, enemy):
                        #Reset the bullet
                        bullet.hideturtle()
                        bulletstate = "ready"
                        bullet.setposition(0, -400)
                        #Reset the enemy
                        x = random.randint(-200, 200)
                        y = random.randint(100, 250)
                        enemy.setposition(x, y)
                        #Update the score
                        score += 10
                        scorestring = "Score: %s" %score
                        score_pen.clear()
                        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                
                if isCollision(player, enemy):
                        player.hideturtle()
                        enemy.hideturtle()
                        print ("Game Over")
                        wn.bye()
                        break

                if score >= 100:
                        sc.home()
                        sc.write("a new foe appears!")
                        wn.delay(40)
                        sc.clear()
                        wn.delay(0)
                        enemy.hideturtle()
                        enemy.setpos(700,700)
                        boss.showturtle()
                        #Move the enemy
                        x = boss.xcor()
                        x += bossspeed
                        boss.setx(x)

                        #Move the enemy back and down
                        if boss.xcor() > 280:
                                #Move all enemies down
                                
                                y = boss.ycor()
                                y -= 40
                                boss.sety(y)
                        #Change enemy direction
                                bossspeed *= -1
                
                        if boss.xcor() < -280:
                                #Move all enemies down
                                
                                y = boss.ycor()
                                y -= 40
                                boss.sety(y)
                                #Change enemy direction
                                bossspeed *= -1
                        
                        #Check for a collision between the bullet and the enemy
                        if bossCollision(bullet, boss):
                                #Reset the bullet
                                bullet.hideturtle()
                                bulletstate = "ready"
                                bullet.setposition(0, -400)
                                
                                bosshit += 1
                                if bosshit == 5:
                                #Reset the enemy
                                        x = random.randint(-200, 200)
                                        y = random.randint(100, 250)
                                        boss.setposition(x, y)
                                        bosshit = 0
                                #Update the score
                                score += 30
                                scorestring = "Score: %s" %score
                                score_pen.clear()
                                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                
                        if bossCollision(player, boss):
                                player.hideturtle()
                                boss.hideturtle()
                                print ("Game Over")
                                wn.bye()
                                break
                if score >= 200:
                        enemy.hideturtle()
                        boss2.showturtle()
                        #Move the enemy
                        x = boss2.xcor()
                        x += bossspeed2
                        boss2.setx(x)

                        #Move the enemy back and down
                        if boss2.xcor() > 280:
                                #Move all enemies down
                                
                                y = boss2.ycor()
                                y -= 40
                                boss.sety(y)
                        #Change enemy direction
                                bossspeed2 *= -1
                
                        if boss2.xcor() < -280:
                                #Move all enemies down
                                    
                                y = boss2.ycor()
                                y -= 40
                                boss2.sety(y)
                                #Change enemy direction
                                bossspeed2 *= -1
                        
                        #Check for a collision between the bullet and the enemy
                        if bossCollision(bullet, boss2):
                                #Reset the bullet
                                bullet.hideturtle()
                                bulletstate = "ready"
                                bullet.setposition(0, -400)
                                
                                bosshit += 1
                                if bosshit2 == 5:
                                #Reset the enemy
                                    x = random.randint(-200, 200)
                                    y = random.randint(100, 250)
                                    boss2.setposition(x, y)
                                    bosshit2 = 0
                                #Update the score
                                score += 30
                                scorestring = "Score: %s" %score
                                score_pen.clear()
                                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            
                        if bossCollision(player, boss2):
                            player.hideturtle()
                            boss2.hideturtle()
                            print ("Game Over")
                            wn.bye()
                            break
        
                        
        #Move the bullet
        if bulletstate == "fire":
                y = bullet.ycor()
                y += bulletspeed
                bullet.sety(y)
        
        #Check to see if the bullet has gone to the top
        if bullet.ycor() > 275:
                bullet.hideturtle()
                bulletstate = "ready"
