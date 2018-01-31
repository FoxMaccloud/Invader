#Invader

#importerer moduler
import turtle
import os
import math
import time

#Setter opp skjermen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Invaders")

#Tegner kanten
#setter navn
border_pen = turtle.Turtle()
#velger tegne hastighet. Siden den er 0 så går den så fort den kan
border_pen.speed(0)
#velger farge
border_pen.color("white")
#løfter "blyant")
border_pen.penup()
#flytter pen til -300 -300
border_pen.setposition(-300,-300)
#tar ned blyant igjen
border_pen.pendown()
#størelse på blyant
border_pen.pensize(3)
#tenger en firkant. 600 pixler frem så 90 grader 4 ganger
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
#gjemmer blyant
border_pen.hideturtle


#lager spilleren
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#lager finden
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-275, 250)







#flytte spilleren
playerspeed = 15

def move_left():
    x = player.xcor()
    x -= playerspeed
    #vi lager en if statement for å begrense spilleomerådet
    if x < -280:
            x = -280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
            x = 280
    player.setx(x)

def fire_weapon():
    #definere våpenstatus som global
    global weaponstate
    if weaponstate == "ready":
        weaponstate = "fire"
        #flytte skuddet til over spiller
        x = player.xcor()
        y = player.ycor()
        weapon.setposition(x, y + 10)
        weapon.showturtle()

#Hvis skuddet er så langt unna finden, så blir det et treff
def hit(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False





#lage keyboard binds
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkey(fire_weapon, "space")

#flytte finden
enemyspeed = 15

#lager våpen til spilleren
weapon = turtle.Turtle()
weapon.color("yellow")
weapon.shape("triangle")
weapon.penup()
weapon.speed(0)
weapon.setheading(90)
weapon.shapesize(0.5, 0.5)
weapon.hideturtle()

#fart på skutt
weaponspeed = 20

#definerer skudd status
weaponstate = "ready"

#poeng

score = 0

#mainloop
while True:
    #flytter finden
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #resette skuddet
    if weapon.ycor() > 275:
        weapon.hideturtle()
        weaponstate = "ready"

    #Sjekke om en treffer
    if hit(weapon, enemy):
        weapon.hideturtle()
        weaponstate = "ready"
        weapon.setposition(0, -400)
        #resette finden
        enemy.setposition(-200,250)
        #legge til poeng
        score += 1

    #vinn mekanikk
    if score == 100:
        print("DU VINNER!")
        break

    #Døds mekanikk..
    if hit(enemy, player):
        player.hideturtle()
        print("Game Over!")
        print("your score is:", score)
        break




    #reversere og flytte et hakk ned når finden når kanten
    #snur når xx er nådd
    if enemy.xcor() > 280:
            enemyspeed *= -1
            #flytter ned når xy er nådd
            y = enemy.ycor()
            y -= 45
            enemy.sety(y)

    if enemy.xcor() < -280:
            enemyspeed *= -1
            y = enemy.ycor()
            y -= 45
            enemy.sety(y)



    #flytte skuddet
    y = weapon.ycor()
    y += weaponspeed
    weapon.sety(y)





turtle.mainloop()






#delay = input("Press any key to finnish")
