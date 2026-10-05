from turtle import*


#we want to paint a house

#step 1: draw a square
speed(20)
width(3)
color("purple")
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)

color("purple")

forward(80)   #left window
color("brown")
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(35) 
left(90)
forward(35)
left(90)
pendown()
goto(70,  155)
right(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
right(90)
forward(35)
right(90)
forward(45)
penup()
goto(200, 120)
pendown()

left(90)  #right window
forward(70)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
penup()
goto(200, 155)
pendown()
right(90)
forward(35)
left(90)
forward(70)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)













exitonclick()